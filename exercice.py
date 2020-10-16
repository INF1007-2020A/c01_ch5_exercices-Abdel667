#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
    Nb = float(input('entrez un nombre'))
    if Nb <= 0 :
        Nb *= (-1)
    
    return Nb


def use_prefixes() -> List[str]:
    Chaine = ''
    prefixes, suffixes = 'JKLMNOP', 'ack'
    for letter in prefixes :
        Chaine += letter + suffixes + ' '
    
    return Chaine




def prime_integer_summation() -> int:
    somme = 0
    terme=1
    nombre = 2
    while terme < 101:
        
        prime = True
        for i in range (2, int(nombre**0.5)+1):
            if nombre% i == 0 :
                prime = False
        if prime :
            
            somme += nombre
            terme+= 1
        nombre += 1
            

    return somme 


def factorial(number: int) -> int:
    factor = 1
    for i in range (1, number):
        factor *= i
    factorial = number * factor
    return factorial


def use_continue() -> None:
    for i in range (1, 11):
        if i == 5 :
            continue
        print(i)
    return i
    
    


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()

