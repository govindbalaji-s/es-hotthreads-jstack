import unittest

from ThreadInfo import HotThread
from antlrgen.HotThreadsLexer import HotThreadsLexer
from antlrgen.HotThreadsParser import HotThreadsParser
from antlr4 import *

from hotThreadsJStack import context_list_length


class HotThreadsTestCase(unittest.TestCase):
    file_names = ['inputs/example.hotthreads', 'inputs/example4.hotthreads']
    thread_names = [
        ['elasticsearch[Govind-Balaji-S][clusterApplierService#updateTask][T#1]',
         'elasticsearch[Govind-Balaji-S][masterService#updateTask][T#1]'],
        ['elasticsearch[Govind-Balaji-S][search][T#7][[kibana_sample_data_ecommerce][0]][taskId=LBUSH3whSeSCfwGFs7DCog:2146]']
    ]
    usage_times = [
        [276.4, 12.7],
        [1.4]
    ]
    intervals = [
        [500, 500],
        [2]
    ]
    time_units = ['ms', 's']

    def test_example(self):
        for i in range(2):
            file = self.file_names[i]
            with self.subTest(file=file):
                    hot_threads = HotThread.parse_hot_threads(file)
                    for j in range(len(hot_threads)):
                        with self.subTest(thread=j):
                            hot_thread: HotThread = hot_threads[j]
                            self.assertEqual(hot_thread._name, self.thread_names[i][j])
                            self.assertEqual(hot_thread._usage_time, self.usage_times[i][j])
                            self.assertEqual(hot_thread._interval, self.intervals[i][j])
                            self.assertEqual(hot_thread._time_units, self.time_units[i])


if __name__ == '__main__':
    unittest.main()
