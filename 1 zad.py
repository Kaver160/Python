zad1 = range(1,2019)
for n in zad1:
    m=str(n)
    if m[0:] == m[::-1]:
        print (m[::-1])
