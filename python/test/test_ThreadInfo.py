import unittest

from ThreadInfo import ThreadInfo


class ThreadInfoTest(unittest.TestCase):

    def test_inner_join(self):
        hot_threads_files = ['inputs/join.hotthreads']
        jstacks_files = ['inputs/join.jstack']
        cat_tasks_files = ['inputs/join.cattasks']

        threads_info = ThreadInfo.inner_join_files(hot_threads_files, jstacks_files, cat_tasks_files)
        with open('outputs/join.out', 'r') as file:
            exp = file.read()
        val = ''
        for thread_info in threads_info:
            val += (thread_info.__str__()) + '\n'
        self.assertEqual(val, exp)


if __name__ == '__main__':
    unittest.main()
