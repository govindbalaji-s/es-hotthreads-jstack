import sys
from antlr4 import *
from antlrgen.HotThreadsLexer import HotThreadsLexer
from antlrgen.HotThreadsParser import HotThreadsParser
from antlrgen.JStackDumpLexer import JStackDumpLexer
from antlrgen.JStackDumpParser import JStackDumpParser

class HotThreadsJStack:

    def __init__(self, hot_threads_output_file, jstack_dump_file):
        # List of thread names returned by hot threads API
        self._hot_thread_names = []
        # Header info with % of CPU use from hot threads API
        self._hot_thread_headers = {}
        # Thread's dump from jstack
        self._threads_info = {}
        self._parse_hot_threads(hot_threads_output_file)
        self._parse_jstack_dump(jstack_dump_file)

    def _parse_hot_threads(self, file_name):
        input_stream = FileStream(file_name)
        lexer = HotThreadsLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = HotThreadsParser(stream)
        dump = parser.dump()

        thread_idx = 0
        while dump.threadDump(thread_idx) is not None :
            thread_dump = dump.threadDump(thread_idx)
            thread_header = thread_dump.threadHeader()
            thread_name = thread_header.NoQuote(1).getText()
            self._hot_thread_names.append(thread_name)
            self._hot_thread_headers[thread_name] = thread_header
            thread_idx += 1

    def _parse_jstack_dump(self, file_name):
        input_stream = FileStream(file_name)
        lexer = JStackDumpLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = JStackDumpParser(stream)
        dump = parser.dump()

        thread_idx = 0
        while dump.threadDump(thread_idx) is not None :
            thread_dump = dump.threadDump(thread_idx)
            thread_name = thread_dump.threadHeader().NoQuote(0).getText()
            if thread_name in self._hot_thread_names :
                self._threads_info[thread_name] = thread_dump
            thread_idx += 1

    def print_output(self):
        for thread_name in self._hot_thread_names:
            print(self._hot_thread_headers[thread_name].getText())
            print(self._threads_info[thread_name].getText())
            print("-------------------------------------------------")

def main(argv):
    if len(argv) != 3:
        print("Usage: python3 hotThreadsJStack.py <HotThreadsOutputFile> <JStackDumpFile>")
        sys.exit()
    hot_threads_jstack = HotThreadsJStack(argv[1], argv[2])
    hot_threads_jstack.print_output()

def print_all_hot_threads(file_name) :
    input_stream = FileStream(file_name)
    lexer = HotThreadsLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = HotThreadsParser(stream)
    dump = parser.dump()

    thread_idx = 0
    while dump.threadDump(thread_idx) is not None :
        thread_dump = dump.threadDump(thread_idx)
        print(thread_dump.threadHeader().NoQuote(1))
        thread_idx += 1

if __name__ == '__main__':
    main(sys.argv)