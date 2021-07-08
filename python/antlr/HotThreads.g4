grammar HotThreads;
dump: dumpHeader threadDump*;

dumpHeader: quoteLessLine timeStampLine quoteLessLine*;

timeStampLine: WS noQuoteWord WS noQuoteWord WS noQuoteWord WS timestamp=noQuoteWord unquoted NL;

threadDump: threadHeader threadInfo;

threadHeader: WS percentage unNumberQuoted usage=Number timeUnits=others WS unNumberQuoted interval=Number unquoted Quote name=unquoted Quote NL;
threadInfo: (quoteLessLine)*;



quoteLessLine: (unquoted NL | NL);
unquoted: (noQuoteWord | WS)+;
unNumberQuoted: (noNumberQuoteWord | WS)+;
noQuoteWord: (Others | Number | Percent)+;
noNumberQuoteWord: (Others | Percent)+;
percentage: Number Percent;
others: Others+;
Quote: '\'';
NL: '\n';
WS: (' ' | '\t')+;
Number: Digit+ (Dot Digit+)?;
Percent: '%';
Others: .;

fragment Digit: [0-9];
fragment Dot: '.';