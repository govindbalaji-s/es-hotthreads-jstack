import argparse
import sys
from antlr4 import *
from antlrgen.HotThreadsLexer import HotThreadsLexer
from antlrgen.HotThreadsParser import HotThreadsParser
from antlrgen.JStackDumpLexer import JStackDumpLexer
from antlrgen.JStackDumpParser import JStackDumpParser


class HotThreadsJStack:

    def __init__(self, hot_threads_output_files, jstack, top_stacks, min_cpu):
        self._hot_threads_output_files = hot_threads_output_files
        self._jstacks = jstack
        self.top_stacks = top_stacks
        self.min_cpu = min_cpu
        # List of thread names returned by hot threads API
        self._hot_thread_names = []
        # Header info with % of CPU use from hot threads API
        self._hot_thread_headers = {}
        # Thread's dump from jstack
        self._threads_stack = {}

        self._parse_hot_threads()
        self._parse_jstacks()

    def context_list_length(context_list):
        length = 0
        while context_list(length) is not None:
            length += 1
        return length

    def _parse_hot_threads(self):
        for file_name in self._hot_threads_output_files :
            input_stream = FileStream(file_name)
            lexer = HotThreadsLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = HotThreadsParser(stream)
            dump = parser.dump()

            for thread_idx in range(HotThreadsJStack.context_list_length(dump.threadDump)):
                thread_dump = dump.threadDump(thread_idx)
                thread_header = thread_dump.threadHeader()
                if self._above_threshold(thread_header):
                    # Store header only if beyond threshold cpu usage
                    thread_name = thread_header.NoQuote(1).getText()
                    if thread_name not in self._hot_thread_headers:
                        self._hot_thread_headers[thread_name] = []
                    self._hot_thread_headers[thread_name].append(thread_header)

    def _above_threshold(self, thread_header):
        percentage = thread_header.Percentage()


    def _parse_jstack_dump(self, file_name):
        input_stream = FileStream(file_name)
        lexer = JStackDumpLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = JStackDumpParser(stream)
        dump = parser.dump()

        thread_idx = 0
        while dump.threadDump(thread_idx) is not None:
            thread_dump = dump.threadDump(thread_idx)
            thread_name = thread_dump.threadHeader().NoQuote(0).getText()
            if thread_name in self._hot_thread_names:
                self._threads_stack[thread_name] = thread_dump
            thread_idx += 1

    def print_output(self):
        for thread_name in self._hot_thread_names:
            print(self._hot_thread_headers[thread_name].getText())
            print(self._threads_info[thread_name].getText())
            print("-------------------------------------------------")


def main(argv):
    argparser = argparse.ArgumentParser(description='Filter jstack dump by ES thread names found in /_nodes/hot_threads outputs')
    argparser.add_argument('jstack', help='jstack dump file')
    argparser.add_argument('--hot-threads', nargs='+', required=True, help='List of hot_threads output files')
    argparser.add_argument('--top-threads', type=int, default=3, help='Number of top stacks to print')
    argparser.add_argument('--min-cpu', type=float, default=0, help='Consider only the stacks with minimum cpu usage %')

    args = argparser.parse_args(argv)
    hot_threads_jstack = HotThreadsJStack(args.hot_threads_output_file, args.jstacks, args.top_stacks, args.min_cpu)
    hot_threads_jstack.print_output()


if __name__ == '__main__':
    main(sys.argv)
