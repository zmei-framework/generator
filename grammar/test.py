import sys
from time import perf_counter

from antlr4 import *
from antlr4.xpath.XPath import XPath

from cratis_generator.parser.ZmeiLanguage import ZmeiLanguage

from cratis_generator.parser.ZmeiLanguageLexerRules import ZmeiLanguageLexerRules

start = perf_counter()
# input = FileStream('test.col')
input = FileStream('comlex_model.col')

lexer = ZmeiLanguageLexerRules(input)

next = None
while 'EOF' not in str(next):
    next = lexer.nextToken()

    print(next)


# parser = ZmeiLanguage(stream)
# tree = parser.col_file()
#
# print(tree.comment())
#
# end = perf_counter() - start
#
# print(end)
