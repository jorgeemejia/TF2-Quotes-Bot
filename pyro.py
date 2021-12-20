import random

def get_pyro_quote(*arg):
    keys = list(dict.keys())
    if arg:
        return(keys[arg[0]])
    else:
        return random.choice(keys)

def get_pyro_quote_url(quote):
    return dict[quote]

# def print_pyro_list():
#     keys = list(dict.keys())
#     for (i, item) in enumerate(keys, start = 0):
#         print(i, item)

def print_pyro_list():
    num = 0
    words = ""
    keys = list(dict.keys())
    for key in keys:
        word_num = str(num)
        words += '['
        words += word_num
        words += ']'
        words += " "
        words += key
        words += '\n'
        num += 1
    return words

dict = {"Thanks for the teleporter." : "https://www.youtube.com/watch?v=nbsxrRkTh44",
        "This point is ours!" : "https://www.youtube.com/watch?v=feKQTpvkcN8",
        "I didn't really think I would kill you like that." : "https://www.youtube.com/watch?v=f-phY4g4QNw",
        "Thanks for the help." : "https://www.youtube.com/watch?v=pDhld1BzdZg",
        "I don't think so" : "https://www.youtube.com/watch?v=dFx39LVzd_o",
        "pyro!" : "https://www.youtube.com/watch?v=do5KrAS91vM",
        "Awwwww!" : "https://www.youtube.com/watch?v=3QVNHqj34Ng",
        "Activate the charge!" : "https://www.youtube.com/watch?v=TcFo3PGo__4"
}