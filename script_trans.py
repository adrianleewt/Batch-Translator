print("""
Batch Translate - Adrian Lee

To use, simply run in command prompt. The program will ask for input. Input each
of your desired strings, pressing enter after each string. Input blank once you
have completed data entry. Input your desired language destination in the
code form (eg. zh-CN, en, fr).

""")

from googletrans import Translator
import pinyin

import pandas as pd
from pandas import ExcelWriter
from openpyxl import load_workbook
import os


os.system("chcp 950")
#This line is used so the command prompt can dispaly chinese characters.
translator = Translator()


def ask_input():
    inputting = True
    lst = []
    while inputting == True:
        temp = input("Input a string: ")
        if temp == "":
            inputting == False
            break
        lst.append(temp)
    return lst


def ask_session():
    inputting = True
    while inputting == True:
        session_name = input("Input session name: ")
        if len(session_name) > 30:
            print("ERROR: Name is too long. Try again.")
        else:
            inputting = False
            return session_name


def get_config(text, end):

    try:
        translations = translator.translate(text, dest = end)
        detect = str(translator.detect(text[0]))

        start = int(detect.find("lang=")) + 5
        end = int(detect.find(","))

        lang = detect[start:end]

        return translations,lang

    except:
        print("ERROR: Translation failed. Please check your internet connection and ensure input consistency.")


def get_trans(translations):
    print("\n" + "=============================================")
    output = []

    for translation in translations:
        output.append(translation.text)
        try:
            print(translation.origin + "\n" + translation.text + "\n" + pinyin.get(translation.origin) + "\n")
        except:
            print(translation.origin + "\n" + translation.text + "\n")

    print("=============================================")
    return output


def get_pinyin(text):
    pinyins = [str(pinyin.get(item)) for item in text]
    return pinyins


def save_session(df, session_name):
    try:
        book = load_workbook('trans_record.xlsx')
        writer = ExcelWriter('trans_record.xlsx', engine='openpyxl')
        writer.book = book
        df.to_excel(writer, sheet_name = session_name, index = False)
        writer.save()
        writer.close()
    except:
        print("ERROR: Cannot load/save to workbook. Ensure validity of files and that the sheet is not open.")


session_name = ask_session()
end = input("Destination Language (Two Letter Code): ")

fin_text = []
fin_pin = []
fin_output = []

running = True

while running == True:

    tp_text = ask_input()
    tp_translations, lang = get_config(tp_text,end)
    print("Working...")
    tp_pin = get_pinyin(tp_text)
    tp_output = get_trans(tp_translations)

    fin_text += tp_text
    fin_pin += tp_pin
    fin_output += tp_output

    print("\n")
    ask = input("Continue? (Y for yes, any other key for no.) ")
    if ask == "Y":
        print("\n")
    else:
        print("\nBye! Saving...")
        running = False


df_session = pd.DataFrame(
    {'Input': fin_text,
     'Pinyin': fin_pin,
     'Output': fin_output,
    }, columns = ['Input', 'Pinyin', 'Output'])
save_session(df_session, session_name)

print("\nDone!")
