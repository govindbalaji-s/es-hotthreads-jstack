Usage:

    java -cp ${CLASSPATH}:build/classes/java/main HotThreadsJStack src/test/example.jstack src/test/example.hotthreads

where `example.jstack` is the JStack dump,
and `example.hotthreads` is the output of `GET /_nodes/hot_threads` from ES.

(Default Run config from Intellij IDEA does the same as above
