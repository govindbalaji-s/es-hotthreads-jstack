import org.antlr.v4.runtime.ANTLRInputStream;
import org.antlr.v4.runtime.CommonTokenStream;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.HashMap;
import java.util.Map;

public class HotThreadsJStack {
    private ANTLRInputStream hotThreadsOutput;
    private ANTLRInputStream jStackDump;

    private static class ThreadInfo {
        HotThreadsParser.ThreadDumpContext hotThreadInfo;
        JStackDumpParser.ThreadDumpContext jStackInfo;
    }

    private Map<String, ThreadInfo> threadsInfo = new HashMap<>();

    public HotThreadsJStack(String hotThreadsFileName, String jStackDumpFileName) throws IOException {
        hotThreadsOutput = new ANTLRInputStream(new FileInputStream(hotThreadsFileName));
        jStackDump = new ANTLRInputStream(new FileInputStream(jStackDumpFileName));
        fetchThreadsInfo();
        printThreadsInfo();
    }

    private void fetchThreadsInfo() {
        fetchHotThreadsInfo();
        fetchJStackInfo();
    }

    private void fetchHotThreadsInfo() {
        HotThreadsLexer lexer = new HotThreadsLexer(hotThreadsOutput);
        HotThreadsParser parser = new HotThreadsParser(new CommonTokenStream(lexer));
        HotThreadsParser.DumpContext dump = parser.dump();
        for (HotThreadsParser.ThreadDumpContext threadDump : dump.threadDump()) {
            String threadName = threadDump.threadHeader().NoQuote(1).getText();
            threadsInfo.put(threadName, new ThreadInfo());
            threadsInfo.get(threadName).hotThreadInfo = threadDump;
        }
    }

    private void fetchJStackInfo() {
        JStackDumpLexer lexer = new JStackDumpLexer(jStackDump);
        JStackDumpParser parser = new JStackDumpParser(new CommonTokenStream(lexer));
        JStackDumpParser.DumpContext dump = parser.dump();
        for (JStackDumpParser.ThreadDumpContext threadDump : dump.threadDump()) {
            String threadName = threadDump.threadHeader().NoQuote(0).getText();
            if (threadsInfo.containsKey(threadName)) {
                threadsInfo.get(threadName).jStackInfo = threadDump;
            }
        }
    }

    private void printThreadsInfo() {
        for(Map.Entry<String, ThreadInfo> entry : threadsInfo.entrySet()) {
            ThreadInfo threadInfo = entry.getValue();
            System.out.println(threadInfo.hotThreadInfo.getText());
            System.out.println(threadInfo.jStackInfo.getText());
            System.out.println("----------------------------------------");
        }
    }

    public static void main(String[] args) throws Exception{
        if (args.length != 2) {
            throw new IllegalArgumentException("Usage: java -cp /usr/local/lib/antlr-4.5-complete.jar:build/classes/java/main: HotThreadsJStack <Jstack dump> <hotthreads output>");
        }

        new HotThreadsJStack(args[1], args[0]);
    }

    private static void printAllThreadsHotThreads(String fileName) throws Exception{
        ANTLRInputStream antlrInputStream = new ANTLRInputStream(new FileInputStream(fileName));
        HotThreadsLexer lexer = new HotThreadsLexer(antlrInputStream);
        HotThreadsParser parser = new HotThreadsParser(new CommonTokenStream(lexer));

        HotThreadsParser.DumpContext dump = parser.dump();
        for (HotThreadsParser.ThreadDumpContext threadDump : dump.threadDump()) {
            String threadName = threadDump.threadHeader().NoQuote(1).getText();
            System.out.println(threadName);
        }
    }

    static void printAllThreadsJStack(String fileName) throws Exception {
        ANTLRInputStream antlrInputStream = new ANTLRInputStream(new FileInputStream(fileName));
        JStackDumpLexer lexer = new JStackDumpLexer(antlrInputStream);
        JStackDumpParser parser = new JStackDumpParser(new CommonTokenStream(lexer));

        JStackDumpParser.DumpContext dump = parser.dump();
        for (JStackDumpParser.ThreadDumpContext threadDump : dump.threadDump()) {
            String threadName = threadDump.threadHeader().NoQuote(0).getText();
            System.out.println(threadName);
        }
    }
}
