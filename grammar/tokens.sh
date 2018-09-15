#!/bin/bash

cd .antlr

clear
echo '--------'
#antlr4 -o `pwd` -Xexact-output-dir ../ZmeiLanguage.g4
javac *.java
grun ZmeiLanguage tokens -tokens ../test.col

echo
echo
