grammar HotThreads;
dump: bplate threadDump*;

bplate: quoteLessLine*;

threadDump: threadHeader threadInfo;

threadHeader: Percentage NoQuote '\'' NoQuote '\'\n';
threadInfo: quoteLessLine*;


quoteLessLine: ('\n')* NoQuote ('\n')*;
NoQuote: (~['\n])+;
Quote: '\'';

Percentage: Digit+ (Dot Digit+)? '%';
Digit: [0-9];
Dot: '.';