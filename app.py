#Python Program to Demonstrate a dictionary
import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def dictionary(word):
    word=word.casefold()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        ch=input("Did you mean %s instead ? Press Y if yes and Press N if no :" % get_close_matches(word,data.keys())[0])
        if ch=="Y" or ch=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif ch=="N" or ch=="n":
            w=input("Enter the word you want to search :")
            return dictionary(w)  #Recursion
        else:
            return "We dont understand your query !"
    else:
        return "The word doesn't belongs to the dictionary !"

word=input("Enter any word :")
out=dictionary(word)

if type(out)==list:
   for item in out:
      print(item)
else:
    print(out)
