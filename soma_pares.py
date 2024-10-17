#impares e pares
qtd=int(input("quantos numeros deseja digitar: "))
cont=0
i=0
p=0
while cont != qtd:
    n=int(input("digite um numero: "))
    if(n%2==0):
        p=p+n
    else:
        i=i+1
    cont=cont+1
print(f"a soma dos numeros pares são {p}")
print(f"a quantidade de numeros impares é {i}")
