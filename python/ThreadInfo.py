import json
from typing import List, Dict

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
        self._parent = None
        self._type = common.typefield.text
        self._start_time = common.start_time.text
        self._timestamp = common.timestamp.text
        self._running_time = common.running_time.text
        self._ip = common.ip.text
        self._node = common.node.text

        self._cascading_description = None

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

    @property
    def id(self):
        return self._id

    @property
    def parent_id(self):
        return self._parent_id

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent: 'CatTask'):
        self._parent = parent

    @property
    def cascading_description(self) -> List[str]:
        # Memoized computation of all ancestors' descriptions
        if self._cascading_description is not None:
            return self._cascading_description

        ancestors_description = self._parent.cascading_description if self._parent is not None else []
        self._cascading_description = [self._description] + ancestors_description
        return self._cascading_description

    def __str__(self):
        ret = f'\tType: {self._type}\n'
        ret += f'\tStart Time: {self._start_time}\n'
        ret += f'\tRunning Time: {self._running_time}\n'
        ret += f'\tIP: {self._ip}\n'
        ret += f'\tNode: {self._node}\n'
        ret += f'\tDescriptions(including cascading parent tasks):\n'
        for description in self.cascading_description:
            ret += f'\t\t-{description}\n'
        return ret


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

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return self.__dict__.__str__()

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def contents(self):
        return self._contents


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
        return self._usage_time / self._interval * 100

    def parse_shard_task(self) -> None:
        name = self._name
        ltask = name.rfind('[taskId=')
        rtask = name.rfind(']')
        self._task_id = name[ltask + 8: rtask]
        name = name[:ltask]
        lshard = name.rfind('[')
        rshard = name.rfind(']')
        self._shard = name[lshard + 1: rshard - 1]
        name = name[:lshard]
        lindex = name.rfind('[')
        rindex = name.rfind(']')
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

    @property
    def name(self):
        return self._name

    @property
    def task_id(self):
        return self._task_id

    def __repr__(self):
        return json.dumps(self.__dict__, default=lambda o: o.__str__())

    @property
    def timestamp(self):
        return self._timestamp


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

    def sort_key(self) -> float:
        return sum([hot_thread.percentage() for hot_thread in self._hot_threads])

    @property
    def task(self):
        return self._task

    @task.setter
    def task(self, value: CatTask):
        self._task: CatTask = value

    @staticmethod
    def inner_join(hot_threads: List[HotThread], jstacks: List[JStack], cat_tasks: List[CatTask]) -> List['ThreadInfo']:
        thread_infos: Dict[str, ThreadInfo] = {}

        cat_tasks_lookup: Dict[str, CatTask] = {cat_task.id: cat_task for cat_task in cat_tasks}
        for task_id in cat_tasks_lookup:
            cat_task = cat_tasks_lookup[task_id]
            if cat_task.parent_id in cat_tasks_lookup:
                cat_task.parent = cat_tasks_lookup[cat_task.parent_id]

        for hot_thread in hot_threads:
            name = hot_thread.name
            thread_infos.setdefault(name, ThreadInfo(name)).add_hot_thread(hot_thread)
            if hot_thread.task_id in cat_tasks_lookup and thread_infos[name].task is None:
                thread_infos[name].task = cat_tasks_lookup[hot_thread.task_id]

        for jstack in jstacks:
            name = jstack.name
            if name in thread_infos:
                thread_infos[name].add_jstack(jstack)

        return list(thread_infos.values())

    @staticmethod
    def inner_join_files(hot_thread_files: List[str], jstack_files: List[str], cat_task_files: List[str]) -> List[
        'ThreadInfo']:
        hot_threads = [HotThread.parse_hot_threads(file) for file in hot_thread_files]
        hot_threads = [hot_thread for sublist in hot_threads for hot_thread in sublist]
        thread_names = [hot_thread.name for hot_thread in hot_threads]
        jstacks = [JStack.parse_jstacks(file, thread_names) for file in jstack_files]
        jstacks = [jstack for sublist in jstacks for jstack in sublist]
        cat_tasks = [CatTask.parse_cat_tasks(file) for file in cat_task_files]
        cat_tasks = [cat_task for sublist in cat_tasks for cat_task in sublist]
        return ThreadInfo.inner_join(hot_threads, jstacks, cat_tasks)

    def __str__(self) -> str:
        ret = f'Thread Name:"{self._name}"\n'
        if not self._hot_threads:
            return 'Skipped due to min-cpu: ' + ret
        ret += 'Task:\n'
        ret += self._task.__str__() + '\n'
        ret += "HotThreads CPU Usage:\n"
        for hot_thread in self._hot_threads:
            ret += f'\t- {hot_thread.percentage():.1f}% usage at {hot_thread.timestamp}\n'
        ret += '\n'
        ret += 'JStack dumps:\n'
        for jstack in self._jstacks:
            ret += f'Dump timestamp = {jstack.timestamp}\n'
            ret += jstack.contents
            ret += '-----------------------------------------------------------------------------------------------\n'
        ret += '\n==============================================================================================\n'
        return ret

    def filter_and_sort(self, min_cpu) -> None:
        self._hot_threads = list(filter(lambda hot_thread: hot_thread.percentage() >= min_cpu, self._hot_threads))
        self._hot_threads.sort(key=lambda hot_thread: hot_thread.percentage(), reverse=True)


# Returns the length(smallest index that returns null) of the list generated by callable context_list
def context_list_length(context_list):
    length = 0
    while context_list(length) is not None:
        length += 1
    return length
