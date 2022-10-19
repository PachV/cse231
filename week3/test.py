VOWELS = "aeiou"
word = input("Enter a word ('quit' to quit): \n")

while word.lower() != "quit":
    lowcase = word.lower()
    if lowcase[0] in VOWELS:
        print(lowcase + "way")
    elif (lowcase[0] not in VOWELS) and (len(lowcase) == 1):
        print(lowcase + "ay")
    else:
        for ind,val in enumerate(lowcase):
            if val in VOWELS:
                print(lowcase[ind:] + lowcase[0:ind] + "ay")
                break
    word = input("Enter a word ('quit' to quit): \n")
