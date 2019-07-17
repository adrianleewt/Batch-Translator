print("""
Batch Translate - Adrian Lee

To use, simply run in command prompt. The program will ask for input. Input each
of your desired strings, pressing enter after each string. Input blank once you
have completed data entry. Input your desired language destination in the two
letter code.

""")

from googletrans import Translator
import os

os.system("chcp 950")
#This line is used so the command prompt can dispaly chinese characters.
translator = Translator()

def ask_input():
    inputting = True
    text = []
    while inputting == True:
        temp = input("Input a string: ")
        if temp == "":
            inputting == False
            break
        text.append(temp)
    return text

def ask_config(text):
    print("\n")
    inputting = True
    while inputting == True:
        try:
            end = input("Destination Language (Two Letter Code): ")
            translations = translator.translate(text, dest = end)
        except:
            print("Invalid destination language, try again.")
            continue
        else:
            return translations

def trans(translations):
    print("\n")
    for translation in translations:
        print(translation.origin, ' -> ', translation.text)

def run():
    active = True
    while active == True:

        text = ask_input()
        translations = ask_config(text)
        print("Working...")
        trans(translations)

        print("\n")
        ask = input("Continue? (Y for yes, any other key for no.) ")
        if ask == "Y":
            print("\n")
            run()
        else:
            active = False

run()
