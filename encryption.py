import pickle
s = input()

exec(s)

r = ""

with open('text.txt') as f:
    for i in f.read():
        r += code[i]
    with open("text_by", "wb") as b:
        pickle.dump(f.read(), b)

with open("text_by_cod", "wb") as b:
	bins = int(r, 2).to_bytes(len(r)//8, "big")
    b.write (bins)



print(r)
