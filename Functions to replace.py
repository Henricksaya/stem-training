#functions to replaace characters in string
def replace_in(phrase):
    word=""
    for letter in phrase :
        if letter.lower() in "a e i o u" :
            word =word +"g"
        elif letter.upper() in "A E I O U" :
            word=word + "G"

        else: word= word +letter
    return word
print(replace_in(input("enter a phrase :")))

#asign if 'A' replace with 'G' if 'a' replace with 'g'

