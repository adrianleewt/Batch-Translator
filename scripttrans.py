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
active = True

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

def ask_config():
    end = input("Destination Language (Two Letter Code): ")
    translations = translator.translate(text, dest = end)
    return translations

def trans(config):
    print("\n")
    for config in translations:
        print(config.origin, ' -> ', config.text)

def run():
    while active == True:

        data = ask_input()
        config = ask_config()
        trans(config)

        ask = input("Continue? (Y/N) ")
        if ask == "Y":
            run()
        else:
            break

run()
