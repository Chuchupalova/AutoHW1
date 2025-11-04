while True:
    word = input("Enter a word that contains the letter 'h'")

    if 'h' in word.lower():
        print("You have the word 'h'")
        break
    else:
        print("Sorry, the word 'h' is not in the alphabet")