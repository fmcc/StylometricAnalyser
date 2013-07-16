#! /bin/bash

source ./venv/bin/activate

for i in $( ls ./test_settings ) ; do
    rm ./database/greek_texts.db
    mv ./test_settings/$i ./settings.py
    python setup.py
    python load_dir.py ./test_texts
    python compare_all.py
    python plot.py first_test.png
    mv ./first_test.png ./test_results/$i.png
done
