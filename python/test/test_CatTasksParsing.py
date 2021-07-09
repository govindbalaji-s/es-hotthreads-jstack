import unittest

from ThreadInfo import CatTask


class CatTasksParsingTest(unittest.TestCase):
    file_names = ['inputs/detailed.cattasks', 'inputs/non-detailed.cattasks']
    cat_task_dicts = [
        [
            {'_description': 'description', '_id': 'task_id', '_parent_id': 'parent_task_id', '_type': 'type', '_start_time': 'start_time', '_timestamp': 'timestamp', '_running_time': 'running_time', '_ip': 'ip', '_node': 'node'},
            {'_description': 'indices[kibana_sample_data_ecommerce], types[], search_type[QUERY_THEN_FETCH], source[{"aggregations":{"concat":{"scripted_metric":{"init_script":{"source":"my-expand-init","lang":"my-script"},"map_script":{"source":"my-expand-map","lang":"my-script"},"combine_script":{"source":"my-expand-combine","lang":"my-script"},"reduce_script":{"source":"my-expand-reduce","lang":"my-script"},"params":{"field":"self_id.keyword"}}}}}]', '_id': 'LBUSH3whSeSCfwGFs7DCog:367', '_parent_id': '-', '_type': 'transport', '_start_time': '1625731116789', '_timestamp': '07:58:36', '_running_time': '2.4s', '_ip': '127.0.0.1', '_node': 'Govind-Balaji-S'},
            {'_description': 'shardId[[kibana_sample_data_ecommerce][0]]', '_id': 'LBUSH3whSeSCfwGFs7DCog:368', '_parent_id': 'LBUSH3whSeSCfwGFs7DCog:367', '_type': 'direct', '_start_time': '1625731116789', '_timestamp': '07:58:36', '_running_time': '2.4s', '_ip': '127.0.0.1', '_node': 'Govind-Balaji-S'},
            {'_description': None, '_id': 'LBUSH3whSeSCfwGFs7DCog:371', '_parent_id': '-', '_type': 'transport', '_start_time': '1625731119277', '_timestamp': '07:58:39', '_running_time': '168.8micros', '_ip': '127.0.0.1', '_node': 'Govind-Balaji-S'},
            {'_description': None, '_id': 'LBUSH3whSeSCfwGFs7DCog:372', '_parent_id': 'LBUSH3whSeSCfwGFs7DCog:371', '_type': 'direct', '_start_time': '1625731119277', '_timestamp': '07:58:39', '_running_time': '50micros', '_ip': '127.0.0.1', '_node': 'Govind-Balaji-S'}
        ],
        [
            {'_description': None, '_id': 'task_id', '_parent_id': 'parent_task_id', '_type': 'type', '_start_time': 'start_time', '_timestamp': 'timestamp', '_running_time': 'running_time', '_ip': 'ip', '_node': 'node'},
            {'_description': None, '_id': 'LBUSH3whSeSCfwGFs7DCog:785', '_parent_id': '-', '_type': 'transport', '_start_time': '1625748867635', '_timestamp': '12:54:27', '_running_time': '2.5s', '_ip': '127.0.0.1', '_node': 'Govind-Balaji-S'},
            {'_description': None, '_id': 'LBUSH3whSeSCfwGFs7DCog:786', '_parent_id': 'LBUSH3whSeSCfwGFs7DCog:785', '_type': 'direct', '_start_time': '1625748867635', '_timestamp': '12:54:27', '_running_time': '2.5s', '_ip': '127.0.0.1', '_node': 'Govind-Balaji-S'},
            {'_description': None, '_id': 'LBUSH3whSeSCfwGFs7DCog:787', '_parent_id': '-', '_type': 'transport', '_start_time': '1625748870194', '_timestamp': '12:54:30', '_running_time': '123micros', '_ip': '127.0.0.1', '_node': 'Govind-Balaji-S'},
            {'_description': None, '_id': 'LBUSH3whSeSCfwGFs7DCog:788', '_parent_id': 'LBUSH3whSeSCfwGFs7DCog:787', '_type': 'direct', '_start_time': '1625748870194', '_timestamp': '12:54:30', '_running_time': '48.4micros', '_ip': '127.0.0.1', '_node': 'Govind-Balaji-S'}
        ]
    ]
    def test_example(self):
        for i in range(2):
            file = self.file_names[i]
            with self.subTest(file=file):
                cat_tasks = CatTask.parse_cat_tasks(file)
                for j in range(len(cat_tasks)):
                    with self.subTest(thread=j):
                        cat_task: CatTask = cat_tasks[j]
                        for attr in self.cat_task_dicts[i][j]:
                            self.assertEqual(cat_task.__dict__[attr], self.cat_task_dicts[i][j][attr])
                        for attr in cat_task.__dict__:
                            if attr not in ['_row_context', '_parent', '_cascading_description']:
                                self.assertEqual(cat_task.__dict__[attr], self.cat_task_dicts[i][j][attr])


if __name__ == '__main__':
    unittest.main()
