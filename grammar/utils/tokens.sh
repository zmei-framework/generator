#!/bin/bash

#cd .antlr

clear
echo '--------'
#antlr4 -o `pwd` -Xexact-output-dir ../ZmeiLanguage.g4
javac ZmeiLangSimpleLexer.java
grun ZmeiLangSimpleLexer tokens -tokens ../grammar/test.col

echo
echo
