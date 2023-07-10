#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    flag = False
    for i in range(len(text)):
        if text[i] in [".", "?", ":"]:
            print(text[i])
            flag = True
        elif flag and text[i] == " ":
            flag = False
            print("")
            continue
        else:
            print(text[i], end="")
