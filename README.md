
	usage: hotThreadsJStack.py [-h] [--location LOCATION] [--num-hot-threads NUM_HOT_THREADS] [--num-jstacks NUM_JSTACKS] [--num-cat-tasks NUM_CAT_TASKS]
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
