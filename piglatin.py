try:
    import paperclip
except ImportError:
    pass 


vowels = ('a', 'e', 'i', 'o', 'u', 'y')

def main():
    print("Pig Latin:")
    pigLatin = englishToPigLatin(input('> '))
    print(pigLatin)
    try:
        paperclip.copy(pigLatin)
        print("Copied pig latin to clipbaord")
    except NameError:
        pass 
    
def englishToPigLatin(message):
    pigLatin = ''  # A string of the pig latin translation.
    for word in message.split():
        # Separate the non-letters at the start of this word:
        prefixNonLetters = ''
        while len(word) > 0 and not word[0].isalpha():
            prefixNonLetters += word[0]
            word = word[1:]
        if len(word) == 0:
            pigLatin = pigLatin + prefixNonLetters + ' '
            continue   
        # Separate the non-letters at the end of this word:
        suffixNonLetters = ''
        while not word[-1].isalpha():
            suffixNonLetters = word[-1] + suffixNonLetters
            word = word[:-1]   
        # Remember if the word was in uppercase or titlecase.
        wasUpper = word.isupper()
        wasTitle = word.istitle()  
        word = word.lower()  # Make the word lowercase for translati    
        # Separate the consonants at the start of this word:
        prefixConsonants = ''
        while len(word) > 0 and not word[0] in vowels:
            prefixConsonants += word[0]
            word = word[1:]    
        # Add the pig latin ending to the word:
        if prefixConsonants != '':
            word += prefixConsonants + 'ay'
        else:
            word += 'y'  
        # Set the word back to uppercase or titlecase:
        if wasUpper:
            word = word.upper()
        if wasTitle:
            word = word.titl    
        # Add the non-letters back to the start or end of the word.
        pigLatin += prefixNonLetters + word + suffixNonLetters + ' '
    return pigLatin

if __name__ == '__main__':
    main()