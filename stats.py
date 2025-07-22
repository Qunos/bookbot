from email.mime import text


def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def count_characters(text):
    convert_text = text.lower()
    registru_caractere = {}
    for char in convert_text:
        if char.isalpha():
            if char not in registru_caractere:
                registru_caractere[char] = 1
            else:
                registru_caractere[char] += 1
        else:
            pass
    return registru_caractere

def sort_on(items):
    return items["frecventa"]

def sortare(dictionar):
    preluare_dictionar = count_characters(dictionar)
    lista_dictionar = []
    for i in preluare_dictionar:
        lista_dictionar.append({"litera":i, "frecventa": preluare_dictionar[i]})
    lista_dictionar.sort(key=sort_on, reverse=True)
    for o in lista_dictionar:
        print(f"{o['litera']}: {o['frecventa']}")

    return lista_dictionar
    