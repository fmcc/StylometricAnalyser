#! /bin/bash

for setting in $( ls ./test_settings) ; do

sett=$(echo $setting | sed -e "s/\.py//g")
s=$(echo $sett | sed -e "s/^[0-9]\+_//g")
for result in $( ls ./test_results) ; do
res=$(echo $result | sed -e "s/\.csv//g")
r=$(echo $res | sed -e "s/^[0-9]\+_//g")
if [ "$r" == "$s" ]; then
    rm ./test_settings/$setting
fi

done
done
