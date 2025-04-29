import pickle
import struct
s = input()

exec(s)

r = ""

with open("text_by_cod.bnr", "wb") as c:    

    with open('text.txt') as f:
        text = f.read()
        for i in text:
            r += code[i]
            for j in code[i]:
                c.write(int(r, 2))
        with open("text_by.bnr", "wb") as b:
            pickle.dump(text, b)

    



