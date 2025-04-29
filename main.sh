rm frequency.txt

python3 frequency.py >> frequency.txt

rm code.txt

python3 frequency.py | python3 creature_dictionary.py  >> code.txt

rm text_by.bnr
rm text_by_cod.bnr
rm text_code.txt

python3 frequency.py | python3 creature_dictionary.py | python3 encryption.py  >> text_code.txt