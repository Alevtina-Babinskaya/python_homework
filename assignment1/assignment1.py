def hello ():
    return "Hello!"
hello()

def greet (name):
    return "Hello, " + name + "!"
greet("James")

def calc (a, b, action="multiply"):
    if type(a) == str or type(b) == str:
        return "You can't multiply those values!"
    elif action=="multiply":
        return a * b
    elif action=="add":
        return a + b
    elif action=="divide":
        if b == 0:
            return "You can't divide by 0!"
        else:
            return a / b
    elif action=="subtract":
        return a - b
    elif action=="modulo":
        return a % b
    elif action=="power":
        return a ** b
    elif action=="int_divide":
        if b == 0:
            return "You can't divide by 0!"
        else:
            return a // b
    else:
        return "Invalid action provided."
calc(5,6)
  

def data_type_conversion (value, target_type):
    try:
        if target_type == "int":
            return int(value)
        elif target_type == "float":
            return float(value)
        elif target_type == "str":
            return str(value)
        else:
            return "Invalid target type provided."
    except ValueError:
        return f"You can't convert {value} into a {target_type}."
data_type_conversion("110", "int")

def grade (*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."
grade(75,85,95)

def repeat (string, times):
    result_string = string
    for i in range(times-1):
        result_string += string
    return result_string
repeat("up,", 4)

def student_scores (action, **kwargs):
    max_score = 0
    key_with_max_score = None
    sum_score = 0
    length = 0
    for key, value in kwargs.items():
        if value > int(max_score):
            max_score = value
            key_with_max_score = key
        sum_score += value
        length += 1                 # This loop finds the student with maximum score, calculates the mean score, though there is an easier way to do this using the max, sum, and len function
    average = sum_score / length   
    if action == "mean":
        return average
    elif action == "best":
        return key_with_max_score
    else:
        return "Invalid action provided."
student_scores ("mean", Tom=75, Dick=89, Angela=91)

def titleize (string):
    words = string.split()
    little_words = ["and", "or", "the", "a", "an", "in", "on", "with"]
    for i, word in enumerate(words):
        if word not in little_words:
            words[i] = word.capitalize()
        elif i == 0 or i == len(words) - 1:
            words[i] = word.capitalize()
        else:
            words[i] = word
    return " ".join(words)
titleize("the lord of the rings")
    
def hangman (secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result
hangman("district", "ic")

def pig_latin (string):
    words = string.split()
    vowels = "aeiou"
    pig_latin_words = []
    for word in words:
        if word[0] in vowels or word[0:1] == "qu":
            pig_latin_words.append(word)
        else:
            k=0
            for index in range(len(word)):
                if word[index] not in vowels and word[index:index+2] != "qu":
                    k = k + 1
                else:
                     break
            pig_latin_words.append(word[k:] + word[:k])
   
    for pl_word in pig_latin_words:
        qu_index = pl_word.find("qu")
        if qu_index != -1:
            pig_latin_words[pig_latin_words.index(pl_word)] = pl_word[:qu_index] + pl_word[qu_index+2:] + "quay"
        else:            
            pig_latin_words[pig_latin_words.index(pl_word)] = pl_word + "ay"
    return " ".join(pig_latin_words)
print(pig_latin("square"))