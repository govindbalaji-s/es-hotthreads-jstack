from typing import List

from antlr4 import FileStream, CommonTokenStream

from antlrgen.HotThreadsLexer import HotThreadsLexer
from antlrgen.HotThreadsParser import HotThreadsParser
from antlrgen.JStackDumpLexer import JStackDumpLexer
from antlrgen.JStackDumpParser import JStackDumpParser
from antlrgen.CatTasksParser import CatTasksParser
from antlrgen.CatTasksLexer import CatTasksLexer


class CatTask:

    def __init__(self, cat_task_context: CatTasksParser.CatTaskContext):
        if cat_task_context is None:
            return  # Only for testing
        self._row_context = cat_task_context
        if cat_task_context.detailed() is None:
            common = cat_task_context.nonDetailed()
            self._description = None
        else:
            common = cat_task_context.detailed().nonDetailed()
            self._description = cat_task_context.detailed().description().getText()
        self._id = common.task_id.text
        self._parent_id = common.parent_task_id.text
        self._type = common.typefield.text
        self._start_time = common.start_time.text
        self._timestamp = common.timestamp.text
        self._running_time = common.running_time.text
        self._ip = common.ip.text
        self._node = common.node.text

    @staticmethod
    def parse_cat_tasks(file_name) -> List['CatTask']:
        input_stream = FileStream(file_name)
        lexer = CatTasksLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CatTasksParser(stream)
        cat_tasks_context = parser.catTasks()

        cat_tasks = []
        for task_idx in range(context_list_length(cat_tasks_context.catTask)):
            cat_task_context = cat_tasks_context.catTask(task_idx)
            cat_task = CatTask(cat_task_context)
            cat_tasks.append(cat_task)
        return cat_tasks


class JStack:

    def __init__(self, thread_dump: JStackDumpParser.ThreadDumpContext, timestamp: str):
        thread_header = thread_dump.threadHeader()
        self._name: str = thread_header.name.text
        self._timestamp: str = timestamp
        self._contents: str = thread_dump.getText()

    # Parse jstacks from given file. Returns list of jstacks of threads whose name is in filter_thread_names
    # If filter_thread_names is None, returns all threads.
    @staticmethod
    def parse_jstacks(file_name, filter_thread_names) -> List['JStack']:
        input_stream = FileStream(file_name)
        lexer = JStackDumpLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = JStackDumpParser(stream)
        dump = parser.dump()
        timestamp = dump.bplate().timestamp.text

        jstacks = []
        for thread_idx in range(context_list_length(dump.threadDump)):
            thread_dump = dump.threadDump(thread_idx)
            jstack = JStack(thread_dump, timestamp)
            if filter_thread_names is None or jstack._name in filter_thread_names:
                jstacks.append(jstack)
        return jstacks


class HotThread:

    def __init__(self, thread_dump: HotThreadsParser.ThreadDumpContext, timestamp: str):
        thread_header = thread_dump.threadHeader()
        self._name: str = thread_header.name.getText()
        self._timestamp: str = timestamp
        self._usage_time: float = float(thread_header.usage.text)
        self._interval: float = float(thread_header.interval.text)
        self._time_units: str = thread_header.timeUnits.getText()
        self._task_id: str = ""
        self._shard: str = ""
        self._index: str = ""
        self.parse_shard_task()

    def percentage(self) -> float:
        return self._usage_time / self._interval

    def parse_shard_task(self) -> None:
        name = self._name
        ltask = name.rindex('[taskId=')
        rtask = name.rindex(']')
        self._task_id = name[ltask + 8: rtask]
        name = name[:ltask]
        lshard = name.rindex('[')
        rshard = name.rindex(']')
        self._shard = name[lshard + 1: rshard - 1]
        name = name[:lshard]
        lindex = name.rindex('[')
        rindex = name.rindex(']')
        self._index = name[lindex + 1: rindex]

    @staticmethod
    def parse_hot_threads(file_name) -> List['HotThread']:
        input_stream = FileStream(file_name)
        lexer = HotThreadsLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = HotThreadsParser(stream)
        dump = parser.dump()
        timestamp: str = dump.dumpHeader().timeStampLine().timestamp.getText()
        ret = []
        for thread_idx in range(context_list_length(dump.threadDump)):
            thread_dump: HotThreadsParser.ThreadDumpContext = dump.threadDump(thread_idx)
            ret.append(HotThread(thread_dump, timestamp))

        return ret


class ThreadInfo:

    def __init__(self, name: str):
        self._name: str = name
        self._task: CatTask or None = None
        self._jstacks: List[JStack] = []
        self._hot_threads: List[HotThread] = []

    def add_jstack(self, jstack):
        self._jstacks.append(jstack)

    def add_hot_thread(self, hot_thread):
        self._hot_threads.append(hot_thread)

    @property
    def task(self):
        return self._task

    @task.setter
    def task(self, value: CatTask):
        self._task: CatTask = value


# Returns the length(smallest index that returns null) of the list generated by callable context_list
def context_list_length(context_list):
    length = 0
    while context_list(length) is not None:
        length += 1
    return length
