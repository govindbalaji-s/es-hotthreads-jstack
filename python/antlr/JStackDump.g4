grammar JStackDump;
dump: bplate threadDump*;

bplate: quoteLessLine*;

threadDump: threadHeader threadInfo;

threadHeader: '"' name=NoQuote '"' NoQuote '\n'+;
threadInfo: quoteLessLine*;


quoteLessLine: ('\n')* NoQuote ('\n')*;
NoQuote: (~["\n])+;
Quote: '"';
