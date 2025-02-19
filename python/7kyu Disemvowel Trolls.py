def disemvowel(semVogais):
    vowels = "aeiouAEIOU"
    new = ""
    for i in semVogais:
        new = new + i.strip(vowels)
    return new