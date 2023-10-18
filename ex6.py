def est_palindrome(chaine):
    return chaine == chaine[::-1]

chaine = input("Entrez une chaîne de caractères : ")
if est_palindrome(chaine):
    print("La chaîne est un palindrome.")
else:
    print("La chaîne n'est pas un palindrome.")
