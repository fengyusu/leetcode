
def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

def lcm(a, b):
    return int( a * b / gcd(a, b) )

print("gcd", gcd(24,36))
print("lcm", lcm(4,6))