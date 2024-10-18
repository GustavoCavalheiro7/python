#fatorial
n=int(input("Digite o valor fatorial: "))
c=n
va=n
f=1
if n==0 :
    print("O valor do fatorial é: 1")
elif n<0 :
    print("Não e possível fazer o cálculo")
else:
    while f != c:
        n=n-1
        va=va*n
        f=f+1
print(f"O valor do fatorial é: {va}")
