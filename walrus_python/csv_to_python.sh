#!/bin/bash
file=$(mktemp)
../walrus_cpp/slor $1 >$file

cat $file | grep "@source" | sed -e 's/.*source=\([0-9]*\).*tion=\([0-9]*\).*/\1 \2/g' >python_graph.dat

cat $file | grep "; @value=T;" | sed -e 's/.*id=\([0-9]*\).*/\1/g' >python_spanning_tree.dat

