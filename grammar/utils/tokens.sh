#!/bin/bash

#cd .antlr

clear
echo '--------'
antlr4 -o `pwd` -Xexact-output-dir ../ZmeiLangSimpleLexer.g4
javac ZmeiLangSimpleLexer.java
grun ZmeiLangSimpleLexer tokens -tokens test.col

echo
echo
