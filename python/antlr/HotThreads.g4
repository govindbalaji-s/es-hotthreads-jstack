grammar HotThreads;
dump: bplate threadDump*;

bplate: quoteLessLine+;

threadDump: threadHeader threadInfo;

threadHeader: WS Percentage unquoted Quote name=unquoted Quote NL;
threadInfo: (quoteLessLine)*;


quoteLessLine: (unquoted NL | NL)+;
unquoted: (NoQuote | WS)+;
Quote: '\'';
NL: '\n';
WS: (' ' | '\t')+;

Percentage: Digit+ (Dot Digit+)? '%';
fragment Digit: [0-9];
fragment Dot: '.';
NoQuote: .;