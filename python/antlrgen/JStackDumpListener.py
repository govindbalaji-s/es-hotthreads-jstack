# Generated from JStackDump.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JStackDumpParser import JStackDumpParser
else:
    from JStackDumpParser import JStackDumpParser

# This class defines a complete listener for a parse tree produced by JStackDumpParser.
class JStackDumpListener(ParseTreeListener):

    # Enter a parse tree produced by JStackDumpParser#dump.
    def enterDump(self, ctx:JStackDumpParser.DumpContext):
        pass

    # Exit a parse tree produced by JStackDumpParser#dump.
    def exitDump(self, ctx:JStackDumpParser.DumpContext):
        pass


    # Enter a parse tree produced by JStackDumpParser#bplate.
    def enterBplate(self, ctx:JStackDumpParser.BplateContext):
        pass

    # Exit a parse tree produced by JStackDumpParser#bplate.
    def exitBplate(self, ctx:JStackDumpParser.BplateContext):
        pass


    # Enter a parse tree produced by JStackDumpParser#threadDump.
    def enterThreadDump(self, ctx:JStackDumpParser.ThreadDumpContext):
        pass

    # Exit a parse tree produced by JStackDumpParser#threadDump.
    def exitThreadDump(self, ctx:JStackDumpParser.ThreadDumpContext):
        pass


    # Enter a parse tree produced by JStackDumpParser#threadHeader.
    def enterThreadHeader(self, ctx:JStackDumpParser.ThreadHeaderContext):
        pass

    # Exit a parse tree produced by JStackDumpParser#threadHeader.
    def exitThreadHeader(self, ctx:JStackDumpParser.ThreadHeaderContext):
        pass


    # Enter a parse tree produced by JStackDumpParser#threadInfo.
    def enterThreadInfo(self, ctx:JStackDumpParser.ThreadInfoContext):
        pass

    # Exit a parse tree produced by JStackDumpParser#threadInfo.
    def exitThreadInfo(self, ctx:JStackDumpParser.ThreadInfoContext):
        pass


    # Enter a parse tree produced by JStackDumpParser#quoteLessLine.
    def enterQuoteLessLine(self, ctx:JStackDumpParser.QuoteLessLineContext):
        pass

    # Exit a parse tree produced by JStackDumpParser#quoteLessLine.
    def exitQuoteLessLine(self, ctx:JStackDumpParser.QuoteLessLineContext):
        pass



del JStackDumpParser