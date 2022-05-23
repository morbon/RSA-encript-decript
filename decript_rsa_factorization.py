print("Enter your e:")
e = int(input())
print("Enter your n:")
n = int(input())
print("Enter your p:")
p = int(input())
print("Enter your q:")
q = int(input())
print("Enter your cipher c:")
c = int(input())

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
print('iverse ', inv)

d = inv
# расшифровываем закрытым ключом
m = pow(c,d,n)
print("Рашифровано в байтах: ", m)
#перевод в текст
res = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()
print("Результат расшифровки с байтов в текст: ", res)
