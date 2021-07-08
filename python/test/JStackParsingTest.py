import unittest

from ThreadInfo import HotThread, JStack


class JStackParsingTestCase(unittest.TestCase):
    file_names = ['inputs/example.jstack', 'inputs/example2.jstack']
    thread_names = [
        ['elasticsearch[Govind-Balaji-S][search][T#1]',
         'elasticsearch[Govind-Balaji-S][search][T#2]'],
        ['elasticsearch[Govind-Balaji-S][search][T#3]']
    ]
    timestamps = ['2021-07-06 14:38:51', '2021-07-07 12:50:23']
    # contents = []

    def test_example(self):
        for i in range(2):
            file = self.file_names[i]
            with self.subTest(file=file):
                jstacks = JStack.parse_jstacks(file, self.thread_names[i])
                for j in range(len(jstacks)):
                    with self.subTest(thread=j):
                        jstack: JStack = jstacks[j]
                        self.assertEqual(jstack._name, self.thread_names[i][j])
                        self.assertEqual(jstack._timestamp, self.timestamps[i])


if __name__ == '__main__':
    unittest.main()
