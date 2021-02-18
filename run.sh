
python app-nothing.py
python app-numpy.py
python app-scipy.py

for file in /tmp/*.json
do
    echo $file
    cat $file
    echo
done
