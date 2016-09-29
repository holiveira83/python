def anti_vowel(text):
    phrase = ""
    for i in text:
        if i in "aeiouAEIOU":
            phrase = phrase + ""
        else:
            phrase = phrase + i
    print phrase
    return phrase

anti_vowel("hey you") 