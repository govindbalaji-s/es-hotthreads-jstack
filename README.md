Usage:

    java -cp /usr/local/lib/antlr-4.5-complete.jar:build/classes/java/main: HotThreadsJStack src/test/example.jstack src/test/example.hotthreads

where `example.jstack` is the JStack dump,
and `example.hotthreads` is the output of `GET /_nodes/hot_threads` from ES.
