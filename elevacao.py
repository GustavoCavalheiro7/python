#elevacao
a=int(input("Digite o valor a ser elevado: "))
b=int(input("Digite o valor que elevara o primeiro: "))
va=a
CONT=1
if b==1 :
    print(f"O valor da elevacao e: {a}")
elif b<0 :
    print("Nao e possivel fazer o calculo")
else:
    while CONT != b:
        va=va*a
        CONT=CONT + 1
print(f"O valor da elevacao e: {va}")
