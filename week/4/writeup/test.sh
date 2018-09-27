#!/bin/bash

echo -n "Enter IP address: "
read input
cmd="ping -w 5 -c 2 $input"
output=$(eval $cmd)
echo $output
echo "done"
