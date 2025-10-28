"""
calculadora simple.py
Autora: Nzinga Mbande
Descripcion: Calculadora básica de Python
Fecha: 28/10/2025 
"""

def sumar (a,b):
    return a+b
def restar (a,b):
    return a-b

def multi(a,b):
    return a*b
def div (a,b):
    if b == 0: 
        return "Error: division entre cero"
    else:
        return a/b

def main():
    print("Calculadora simple")
    x = float(input("Introduce el primer número: "))
    y = float(input("Introduce el segundo número: "))
    
    
    print(f"Suma: {sumar(x,y)}")
    print(f"Resta: {restar(x,y)}")
    print(f"Multiplicación: {multi(x,y)}")
    print(f"División: {div(x,y)}")
    
    
    if __name__ == "__main__":
        main()