# Palindrome
def palindrome(): #Function to call always
    word = str(input('Write a word: ')) #Ask for a word
    word = word.lower() #Do the word lower
    for space in word:
        if space == " ": #If the word had spaces
            word = word.replace(' ','')
    if word == word[::-1]: #Check if the word is palindrome
        print("The word IS Palindrome")
    else:
        print("The word IS NOT Palindrome")
        palindrome()
palindrome() #Call the function

execution = 0 
while execution == 0: #Execution of the function
    palindrome()
    
#Juan Pablo Picón Martínez