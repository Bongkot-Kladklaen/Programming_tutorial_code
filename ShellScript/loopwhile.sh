#!/bin/bash

num=1

while [ $num -le 10 ]
do
  echo "Loop $num"
  ((num = $num+1))
done

