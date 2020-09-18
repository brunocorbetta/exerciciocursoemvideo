num = list()
for c in range(0, 5):
    n = int(input('Digite um numero: '))
    if c == 0 or n> num[-1]:
        num.append(n)
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                break
            pos += 1
print(num)