
Tool to summarise `jstack` dumps of threads shown as "hot threads" by ES `_nodes/hot_threads` API, along with the tasks hierarchy of the corresponding threads using the modified `_cat/tasks` API.

## Dependencies

    pip3 install antlr4
    pip3 install requests
## Usage
	python3 hotThreadsJStack.py [-h] [--location LOCATION] [--num-hot-threads NUM_HOT_THREADS] [--num-jstacks NUM_JSTACKS] [--num-cat-tasks NUM_CAT_TASKS]
				   [--top-threads TOP_THREADS] [--min-cpu MIN_CPU]
				   pid

	Filter jstack dump by ES thread names found in /_nodes/hot_threads outputs

	positional arguments:
	  pid                   PID of ElasticSearch

	optional arguments:
	  -h, --help            show this help message and exit
	  --location LOCATION   Location where ES is running. Default=localhost:9200
	  --num-hot-threads NUM_HOT_THREADS
				Number of times to take hot threads output. Default=1
	  --num-jstacks NUM_JSTACKS
				Number of times to take jstack dump. Default=1
	  --num-cat-tasks NUM_CAT_TASKS
				Number of times to take cat tasks output. Default=1
	  --top-threads TOP_THREADS
				Number of top threads to print, defaults to 3
	  --min-cpu MIN_CPU     Consider only the hot threads measure with minimum cpu usage %, defaults to 0

## Example

    python3 hotThreadsJStack.py 2386 --num-hot-threads 2 --num-jstacks 0 --num-cat-tasks 2 --location localhost:9200 --top-threads 3
### Output:

```
Thread Name:"elasticsearch[Govind-Balaji-S][search][T#24][[kibana_sample_data_ecommerce][0]][taskId=LBUSH3whSeSCfwGFs7DCog:2908]"
Task:
Type: direct
Start Time: 1625821906993
Running Time: 2.6s
IP: 127.0.0.1
Node: Govind-Balaji-S
Descriptions(including cascading parent tasks):
-shardId[[kibana_sample_data_ecommerce][0]]
-indices[kibana_sample_data_ecommerce], types[], search_type[QUERY_THEN_FETCH], source[{"aggregations":{"concat":{"scripted_metric":{"init_script":{"source":"my-expand-init","lang":"my-script"},"map_script":{"source":"my-expand-map","lang":"my-script"},"combine_script":{"source":"my-expand-combine","lang":"my-script"},"reduce_script":{"source":"my-expand-reduce","lang":"my-script"},"params":{"field":"self_id.keyword"}}}}}]
HotThreads CPU Usage:
- 101.3% usage at 2021-07-09T09:11:48.963Z,
- 80.4% usage at 2021-07-09T09:11:48.334Z,
JStack dumps:
==============================================================================================
Thread Name:"ticker-schedule-trigger-engine"
Task:
None
HotThreads CPU Usage:
- 20.8% usage at 2021-07-09T09:11:48.334Z,
JStack dumps:
==============================================================================================
```
