rm frequency.txt

python3 frequency.py >> frequency.txt

rm code.txt

python3 frequency.py | python3 creature_dictionary.py  >> code.txt

rm text_by
rm text_by_code

python3 frequency.py | python3 creature_dictionary.py | python3 encryption.py  >> text_code.txt