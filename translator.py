def translation(phrase):
    translate = ""


    for letter in phrase:
        if letter in "AEIOUaeiou":

            translate = translate + "p"
        else:
            translate = translate + letter
    return translate



print(translation(input("\nEnter a phrase to translate- ")))


