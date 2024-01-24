#Faça um programa que leia um número inteiro e mostre na tela o
# seu sucessor e o seu antecessor
n1 = int(input('Digite um número inteiro: '))

#s = n1 + 1
#a = n1 - 1

print('O número \033[1;31m{}\033[m tem como seu antecessor \033[1;31m{}\033[m e o seu sucessor \033[1;31m{}\033[m.' .format(n1, (n1-1), (n1+1)))
