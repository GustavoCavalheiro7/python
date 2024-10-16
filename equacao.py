#equação

a=int(input("Digite o valor de a: "))
b=int(input("Digite o valor de b: "))
c=int(input("Digite o valor de c: "))
d=int(input("Digite o valor de d: "))
e=int(input("Digite o valor de e: "))
f=int(input("Digite o valor de f: "))

if a==0 or b==0 or c==0 or d==0:
    print("o sistema foi interrompido")
else:
    if (c*e - b*f)%(a*e - b*d)==0 and (a*f - c*d)%(a*e - b*d)==0:
        x=(c*e - b*f)/(a*e - b*d)
        y=(a*f - c*d)%(a*e - b*d)

        print(f" x é: {x:.0f}")
        print(f" y é: {y:.0f}")
    else:
        print("o sistema n tem solução")
