def WordReplace():
    str="hi this is albert and hello broskies i hi hi hi hi"
    word_to_replace=input("Enter the word to replace : ") # the existing word that you want to replace
    replacement_word=input("Enter the replacement word : ") # The new word that need to nee placed in the existing string
    print(str.replace(word_to_replace,replacement_word))

WordReplace()
