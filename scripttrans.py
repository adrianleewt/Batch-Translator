print("""
Simple Google Translate - Run from Command Prompt

To use, simply run in command prompt. The program will ask for input. Input each
of your desired strings, pressing enter after each string. Input blank once you
have completed data entry. Input your desired language destination in the two
letter code.

This program needs googletrans (run 'pip install googletrans' in CP) and python
""")

from googletrans import Translator
import os

os.system("chcp 950")
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
    end = input("Destination Language (Two Letter Code): ")
    translations = translator.translate(text, dest = end)
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
        trans(translations)

        print("\n")
        ask = input("Continue? (Y/N) ")
        if ask == "Y":
            run()
        else:
            active = False

run()
