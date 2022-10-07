def get_count(sentence):
    vog = 0
    vogais = ["a", "e", "i", "o", "u"]
    for i in sentence:
        if i in vogais:
            vog = vog + 1
    return vog
