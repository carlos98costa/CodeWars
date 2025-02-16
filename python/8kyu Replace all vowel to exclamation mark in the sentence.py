def replace_exclamation(st):
    vogais = "aeiouAEIOU"
    nova_sentenca = ""
    for char in st:
        if char in vogais:
            nova_sentenca += "!"
        else:
            nova_sentenca += char
    return nova_sentenca