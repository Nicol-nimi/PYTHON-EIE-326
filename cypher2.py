def caesar(word, cipher_shift_value):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    list_word = list(word.upper())
    caesar = list_word.copy()

    for i in range(len(list_word)):
        if list_word[i] in alphabet:
            index = alphabet.index(list_word[i])
            index = (index + cipher_shift_value) % len(alphabet)
            caesar[i] = alphabet[index]
        else:
            
           
            return ''.join(caesar)


print(caesar("ghhjr,!", 2))
