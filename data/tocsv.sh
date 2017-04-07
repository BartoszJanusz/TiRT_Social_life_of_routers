#! /bin/bash

sed 's/\t/,/g' $1 > $2.csv
