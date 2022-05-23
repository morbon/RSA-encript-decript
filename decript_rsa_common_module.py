print("Enter your e1: ")
e1 = int(input())
print("Enter your e2: ")
e2 = int(input())
print("Enter N: ")
n = int(input())
print("Enter C1: ")
c1 = int(input())
print("Enter C2: ")
c2 = int(input())

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
print(egcd(e1, e2))

inv = mulinv(e1, e2)
rs = egcd(e1, e2)
r = rs[1]
s = rs[2]
print("r =", r, "s =", s)

def gcd(n,m):
        a, a_ = 0, 1
        b, b_ = 1, 0
    
        c, d = n, m
    
        q = c // d
        r = c % d
        while r:
            c, d = d, r
            a_, a = a, a_ - q * a
            b_, b = b, b_ - q * b
        
            q = c // d
            r = c % d
        return (d, a, b)

def modinv(r, m):
    g, x, y = gcd(r, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

g = e2*s+e1*r
r = (-1)*r
c1_inv = modinv(c1, n)
print('c1_inv = ' + str(c1_inv))
c1r = pow(c1_inv,r,n)
print('c1**r = ' + str(c1r))
c2s = pow(c2,s,n)
print('c2**s = ' + str(c2s))
m = 0
d=c1r * c2s
print('d = ' + str(d))
m = d % n
print('m = ' + str(m))
text=m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()
print(text)


