#! /bin/bash
source ./venv/bin/activate
files=$(ls -1 ./test_settings | wc -l)
counter=1
for i in $( ls ./test_settings ) ; do
    echo Processing settings: $counter/$files >> times.log
    out_file=$(echo $i | sed -e "s/\.py//g")
    echo $out_file >> times.log
    start_time=$(date +%s%N)
    rm ./database/greek_texts.db
    rm -r ./__pycache__
    mv ./test_settings/$i ./settings.py
    python setup.py
    python load_dir.py ./test_texts
    python compare_all.py
    python dump_comparisons.py ./test_results/$out_file.csv
    counter=$((counter+1))
    echo 'Ctrl+c now to exit script.'
    sleep 5s
    elapsed_time=$(($(date +%s%N)-start_time))
    seconds=$((elapsed_time/1000000000))
    hours=$(( seconds / 3600 ))
    minutes=$(( ( seconds / 60 ) % 60 ))
    secs=$(( seconds % 60 ))
    printf "   %02d:%02d:%02d\n" $hours $minutes $secs >> times.log
done


