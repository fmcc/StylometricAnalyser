#! /bin/bash
source ./venv/bin/activate
for i in $( ls ./test_settings ) ; do
    rm ./database/greek_texts.db
    rm -r ./__pycache__
    mv ./test_settings/$i ./settings.py
    python setup.py
    python load_dir.py ./test_texts
    python compare_all.py
    out_file=$(echo $i | sed -e "s/\.py//g")
    echo $out_file
    python dump_comparisons.py ./test_results/$out_file.csv
    echo 'Ctrl+c now to exit script.'
    sleep 10s
done
