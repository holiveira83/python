def reverse(text):
    t = ""
    for i in text:
        print i,
        t = i + t
    return t
print reverse("herson")