import forca
import matrix

print("*****************")
print("Escolha seu jogo!")
print("*****************")

print("(1) Forca (2) Matrix")

jogo = int(input("Qual jogo?"))

if(jogo == 1):
    print("Você iniciou a Forca")
    forca.jogar()
elif(jogo == 2):
    print("Você iniciou a Matrix")
    matrix.jogar()