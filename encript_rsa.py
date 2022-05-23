print("Введите текст, который нужно зашифровать: ")
text = input(" ")
m = int.from_bytes(text.encode(),"big")
print("В байтах: ", m)
print("Введите e: ")
e = int(input())

p = 238324208831434331628131715304428889871
q = 296805874594538235115008173244022912163
n = p*q #mod
print("mod: ", n)
phi = (p-1)*(q-1)   
print("phi: ", phi)
def egcd(a,b):
    if a == 0:
        return(b,0,1)
    else:
        g,x,y = egcd(b%a,a)
        return(g,y-(b//a)*x,x)
# x = mulinv(b) mod n, (x * b) % n == 1
def mulinv(b, n):
    g, x, _ = egcd(b, n)
    print(g,x,_)
    if g == 1:
        return x % n
print(egcd(e, phi))

inv = mulinv(e, phi)
print('iverse',inv)
# Шифруем открытым ключом
d = inv
c = pow(m,e,n)
print("Шифр: ", c)
# расшифровываем закрытым ключом
m = pow(c,d,n)
print("Рашифровано в байтах: ", m)
#перевод в текст
res = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()
print("Результат расшифровки с байтов в текст: ", res)

