# Création d'une boucle de 1 à 101
for i in range(1,101):
    # Verifie si le nombre est divisible par 3 
    divisible_3 = (i % 3 == 0)
    # Verifie si le nombre est divisible par 5
    divisible_5 = (i % 5 ==0) 

    # Si le nombre est divisible par 3 ou 5, afficher "Fizzbuzz"
    if divisible_3 and divisible_5:
        print("FizzBuzz")
    # S'il n'est divisible que par 3, afficher "Fizz"
    elif divisible_3:
        print("Fizz")
    # S'il n'est divisible que par 5, afficher "Buzz"
    elif divisible_5:
        print("Buzz")
    # Autrement, afficher le nombre
    else:
        print(i)