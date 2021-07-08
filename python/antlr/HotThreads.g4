grammar HotThreads;
dump: dumpHeader threadDump*;

dumpHeader: quoteLessLine timeStampLine quoteLessLine*;

timeStampLine: WS NoQuoteWord WS NoQuoteWord WS NoQuoteWord WS timestamp=NoQuoteWord unquoted NL;

threadDump: threadHeader threadInfo;

threadHeader: WS Percentage unquoted Quote name=unquoted Quote NL;
threadInfo: (quoteLessLine)*;

quoteLessLine: (unquoted NL | NL);
unquoted: (NoQuoteWord | WS)+;
Quote: '\'';
NL: '\n';
WS: (' ' | '\t')+;

Percentage: Digit+ (Dot Digit+)? '%';
fragment Digit: [0-9];
fragment Dot: '.';
NoQuoteWord: (~[ \t\n'])+;