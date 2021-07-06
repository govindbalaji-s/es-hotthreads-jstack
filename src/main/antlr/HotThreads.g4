grammar HotThreads;
dump: bplate threadDump*;

bplate: quoteLessLine*;

threadDump: threadHeader threadInfo;

threadHeader: NoQuote '\'' NoQuote '\'\n';
threadInfo: quoteLessLine*;


quoteLessLine: ('\n')* NoQuote ('\n')*;
NoQuote: (~['\n])+;
Quote: '\'';