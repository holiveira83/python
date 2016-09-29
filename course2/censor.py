def censor(text,word):
    t = []
    for i in text.split():
        if word==i:
            t.append("*"*len(i))
        else:
            t.append(i)
    return " ".join(t) 
        
print censor("hj eh dia de foder", "foder")