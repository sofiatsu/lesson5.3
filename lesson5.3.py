import string

input_string = input("enter something")

capital = input_string.title()
cleaned_string = capital.replace(" ","")

for p in string.punctuation:
    cleaned_string = cleaned_string.replace(p, "")

hashtag = ("#" + cleaned_string)[:140]

print(hashtag)
