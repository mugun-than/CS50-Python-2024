def main():
    mass = int(input("What's the mass? "))
    print(joules(mass))

def joules(m):
    c = 300000000
    return m*c*c

main()
