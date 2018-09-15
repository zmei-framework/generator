# Generated from /Users/aleksandrrudakov/dev/generator/grammar/ZmeiLanguage.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3>")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\16\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class ZmeiLanguage ( Parser ):

    grammarFileName = "ZmeiLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'['", "'#'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'='", "'$'", 
                     "'&'", "'!'", "'*'", "'~'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "':'", "<INVALID>", "']'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "ANNOT_BLOCK", "COMMENT_LINE", "COMMENT_BLOCK", 
                      "PAGE_IMPORTS", "DOCUMENT_START", "PAGE_HDR_START", 
                      "COL_HDR_START", "GENERAL_COMMENT_LINE", "GENERAL_COMMENT_BLOCK", 
                      "MODEL_IMPORTS", "NEWLINE", "WHITESPACE", "ERRCHAR", 
                      "COL_NAME", "COL_HDR_SEPARATOR", "COL_HDR_ERRCHAR", 
                      "COL_COMMENT_LINE", "COL_COMMENT_BLOCK", "COL_STR_EXPR", 
                      "COL_MODIFIER__STR", "COL_MODIFIER__LOC", "COL_MODIFIER__UNQ", 
                      "COL_MODIFIER__IDX", "COL_MODIFIER__REQ", "COL_MODIFIER__NNL", 
                      "COL_FIELD", "COL_ANNOT", "COL_FIELD_HELP", "COL_FIELD_VNAME", 
                      "COL_FIELD_SEPARATOR", "COL_ERRCHAR", "FIELD_DECL_COMMENT_LINE", 
                      "FIELD_DECL_COMMENT_BLOCK", "COL_FIELD_CALCULATED", 
                      "COL_FIELD_TYPE", "COL_FIELD_ARGS", "FIELD_DECL_ERRCHAR", 
                      "PAGE_BASE", "PAGE_NAME", "PAGE_HDR_WHITESPACE", "PAGE_HDR_ERRCHAR", 
                      "PAGE_HDR_SEPARATOR", "PAGE_HDR_PART", "PAGE_HDR_END", 
                      "PAGE_HDR_PARTS_WHITESPACE", "PAGE_HDR_PARTS_ERRCHAR", 
                      "PAGE_COMMENT_LINE", "PAGE_COMMENT_BLOCK", "PAGE_FIELD", 
                      "PAGE_FIELD_SEPARATOR", "PAGE_CODE", "PAGE_ANNOT", 
                      "PAGE_ERRCHAR", "PYTHON_LINE_END", "PYTHON_LINE_CODE", 
                      "PYTHON_LINE_ERRCHAR", "ANNOT_COMMENT_LINE", "ANNOT_COMMENT_BLOCK", 
                      "ANNOT_DESCR", "ANNOT_ERRCHAR" ]

    RULE_col_file = 0

    ruleNames =  [ "col_file" ]

    EOF = Token.EOF
    ANNOT_BLOCK=1
    COMMENT_LINE=2
    COMMENT_BLOCK=3
    PAGE_IMPORTS=4
    DOCUMENT_START=5
    PAGE_HDR_START=6
    COL_HDR_START=7
    GENERAL_COMMENT_LINE=8
    GENERAL_COMMENT_BLOCK=9
    MODEL_IMPORTS=10
    NEWLINE=11
    WHITESPACE=12
    ERRCHAR=13
    COL_NAME=14
    COL_HDR_SEPARATOR=15
    COL_HDR_ERRCHAR=16
    COL_COMMENT_LINE=17
    COL_COMMENT_BLOCK=18
    COL_STR_EXPR=19
    COL_MODIFIER__STR=20
    COL_MODIFIER__LOC=21
    COL_MODIFIER__UNQ=22
    COL_MODIFIER__IDX=23
    COL_MODIFIER__REQ=24
    COL_MODIFIER__NNL=25
    COL_FIELD=26
    COL_ANNOT=27
    COL_FIELD_HELP=28
    COL_FIELD_VNAME=29
    COL_FIELD_SEPARATOR=30
    COL_ERRCHAR=31
    FIELD_DECL_COMMENT_LINE=32
    FIELD_DECL_COMMENT_BLOCK=33
    COL_FIELD_CALCULATED=34
    COL_FIELD_TYPE=35
    COL_FIELD_ARGS=36
    FIELD_DECL_ERRCHAR=37
    PAGE_BASE=38
    PAGE_NAME=39
    PAGE_HDR_WHITESPACE=40
    PAGE_HDR_ERRCHAR=41
    PAGE_HDR_SEPARATOR=42
    PAGE_HDR_PART=43
    PAGE_HDR_END=44
    PAGE_HDR_PARTS_WHITESPACE=45
    PAGE_HDR_PARTS_ERRCHAR=46
    PAGE_COMMENT_LINE=47
    PAGE_COMMENT_BLOCK=48
    PAGE_FIELD=49
    PAGE_FIELD_SEPARATOR=50
    PAGE_CODE=51
    PAGE_ANNOT=52
    PAGE_ERRCHAR=53
    PYTHON_LINE_END=54
    PYTHON_LINE_CODE=55
    PYTHON_LINE_ERRCHAR=56
    ANNOT_COMMENT_LINE=57
    ANNOT_COMMENT_BLOCK=58
    ANNOT_DESCR=59
    ANNOT_ERRCHAR=60

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Col_fileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHITESPACE(self):
            return self.getToken(ZmeiLanguage.WHITESPACE, 0)

        def getRuleIndex(self):
            return ZmeiLanguage.RULE_col_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_file" ):
                listener.enterCol_file(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_file" ):
                listener.exitCol_file(self)




    def col_file(self):

        localctx = ZmeiLanguage.Col_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_col_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(ZmeiLanguage.WHITESPACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





