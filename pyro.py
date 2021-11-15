import random

def get_pyro_quote():
    keys = list(pyro_dict.keys())
    return random.choice(keys)

def get_pyro_quote_url(quote):
    return pyro_dict[quote]

pyro_dict = {"Thanks for the teleporter." : "https://www.youtube.com/watch?v=nbsxrRkTh44",
        "This point is ours!" : "https://www.youtube.com/watch?v=feKQTpvkcN8",
        "I didn't really think I would kill you like that." : "https://www.youtube.com/watch?v=f-phY4g4QNw",
        "Thanks for the help." : "https://www.youtube.com/watch?v=pDhld1BzdZg",
        "I don't think so" : "https://www.youtube.com/watch?v=dFx39LVzd_o",
        "pyro!" : "https://www.youtube.com/watch?v=do5KrAS91vM",
        "Awwwww!" : "https://www.youtube.com/watch?v=3QVNHqj34Ng",
        "Activate the charge!" : "https://www.youtube.com/watch?v=TcFo3PGo__4"
}