import unittest

from ThreadInfo import HotThread


class HotThreadsTestCase(unittest.TestCase):
    file_names = ['inputs/example.hotthreads', 'inputs/example4.hotthreads']
    thread_names = [
        ['elasticsearch[Govind-Balaji-S][search][T#11][[kibana_sample_data_ecommerce][0]][taskId=LBUSH3whSeSCfwGFs7DCog:52]',
         'elasticsearch[Govind-Balaji-S][search][T#12][[kibana_sample_data_ecommerce][0]][taskId=LBUSH3whSeSCfwGFs7DCog:54]'],
        ['elasticsearch[Govind-Balaji-S][search][T#7][[kibana_sample_data_ecommerce][0]][taskId=LBUSH3whSeSCfwGFs7DCog:2146]']
    ]
    usage_times = [
        [503.3, 502.7],
        [1.4]
    ]
    intervals = [
        [500, 500],
        [2]
    ]
    time_units = ['ms', 's']
    task_ids = [
        ['LBUSH3whSeSCfwGFs7DCog:52', 'LBUSH3whSeSCfwGFs7DCog:54'],
        ['LBUSH3whSeSCfwGFs7DCog:2146']
    ]
    indices = [
        ['kibana_sample_data_ecommerce', 'kibana_sample_data_ecommerce'],
        ['kibana_sample_data_ecommerce', 'kibana_sample_data_ecommerce']
    ]
    shards = [
        ['0', '0'],
        ['0', '0']
    ]

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
                            self.assertEqual(hot_thread._task_id, self.task_ids[i][j])
                            self.assertEqual(hot_thread._shard, self.shards[i][j])
                            self.assertEqual(hot_thread._index, self.indices[i][j])


if __name__ == '__main__':
    unittest.main()
