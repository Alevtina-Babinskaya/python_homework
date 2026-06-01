def make_hangman(secret_word):
    guesses=set()
    def hangman_closure(letter):
        guesses.add(letter)
        new_word=''
        for char in secret_word:
            if char in guesses:
                new_word += char
            else:
                new_word += '_'
        print (new_word)
        if set(secret_word).issubset(guesses):
            return True
        else:
            return False
    return hangman_closure

word = input('Enter your word')
game1 = make_hangman(word)
while True:
    guess = input('Type your letter')
    finished = game1(guess)
    if finished:
        print("You've got it")
        break
    
 