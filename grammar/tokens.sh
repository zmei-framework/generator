#!/bin/bash

#cd .antlr

clear
echo '--------'
#antlr4 -o `pwd` -Xexact-output-dir ../ZmeiLanguage.g4
javac grammar/ZmeiLangSimpleLexer.java
grun grammar.ZmeiLangSimpleLexer tokens -tokens ../grammar/test.col

echo
echo
