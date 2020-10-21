import random

def skaiciavimas():       
    num1 = float(input('Irasykite pirmaji skaiciu: '))
    tikrinimas_1 = sarasas.count(num1)
    num2 = float(input('Irasykite antraji skaiciu: '))
    tikrinimas_2 = sarasas.count(num2)
    op = input('Pasirinkite veiksma veiksma kuri norite atlikti: (+, -, *, / ): ')

    if tikrinimas_1 == 1 and tikrinimas_2 == 1:     
        if op == '+':
            print(num1 + num2)
        elif op == '-':
            print(num1 - num2)
        elif op == '/':
            print(num1 / num2)
        elif op == '*':
            print(num1 * num2)
        else:
            print('Ivesto skaiciaus sarase nera')
            
            
x = input('Automatinis skaiciu generavimas(A), rankinis skaiciu irasymas(R): ')

if x.lower() == 'a':
    sarasas = [] 
  
    n = int(input("Iveskite kiek elementu bus sarase: ")) 
    print('Skaiciai generuojami atsitiktine tvarka')
    
    for i in range(0, n): 
        ele = float(random.randint(1,100))
        sarasas.append(ele)
    print(sarasas)
    skaiciavimas()
    
if x.lower() == 'r':
    sarasas = [] 
  
    n = int(input("Iveskite kiek elementu bus sarase: ")) 
    print('Iveskite norimus elementus:')
    
    for i in range(0, n): 
        ele = float(input())
        sarasas.append(ele) 
    print('Jusu skaiciu saras yra:')
    print(sarasas)
    skaiciavimas()

