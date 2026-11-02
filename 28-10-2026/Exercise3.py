word = input("Inserte una palabra: ").strip()

inverted_word = word[::-1]

if word == inverted_word:
    print(f"La palabra {word}, es un palindromo")
else:
    print(f"La palabra {word}, no es un palindromo")