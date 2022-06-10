"""Programa que calcule el IMC de una persona dado su peso y estatura. Luego, indicar su nível de peso asi:


IMC                             CLASIFICACIÓN
 ------------------------------------------------------------
Menor que 18.5     -   Bajo peso
18.5 - 24.9  -         Normal
25.0 - 29.9  -         Sobrepeso
30.0 - 34.9  -         Obesidad I
35.0 - 39.9  -         Obesidad II
40.0 - 49.9  -         Obesidad III
Mayor que 50.0     -   Obesidad IV

La fórmula para el

IMC = peso / (estatura * estatura)"
"""

def calcularIMC(p, a):
     return p / (a * a)

def nivelDePeso(IMC):
     if IMC < 18.5:
         return "Bajo peso"
     elif 18.5 <= IMC <= 24.9:
         return "Normal"
     elif 25 <= IMC <= 29.9:
         return "Sobrepeso"
     elif 30 <= IMC <= 34.9:
         return "Obesidad I"
     elif 35 <= IMC <= 39.9:
         return "Obesidad II"
     elif 40 <= IMC <= 49.9:
         return "Obesidad III"
     elif IMC >= 50:
        return "Obesidad IV"

peso = float(input("Dime su peso (kg): "))
altura = float(input("Dime su estatura (m): "))
print("\nSu nivel de peso es:", nivelDePeso(calcularIMC(peso, altura)))

