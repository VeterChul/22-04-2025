
s = {}

with open('text.txt') as f:
    for i in f.read():
        if not(i in s):
            s[i] = 1
        else:
            s[i] += 1
    
print("frequency =", s)

