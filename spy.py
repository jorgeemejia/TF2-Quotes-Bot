import random


def get_spy_quote():
    keys = list(spy_dict.keys())
    return random.choice(keys)

def get_spy_quote_url(quote):
    return spy_dict[quote]


spy_dict = {"You imbecile! You've doomed us all!" : "https://www.youtube.com/watch?v=4ZPDpTwoQKQ",
       "My appreciation, amigo." : "https://www.youtube.com/watch?v=M-ioiw5t1dE",
       "I appreciate your help." : "https://www.youtube.com/watch?v=6AAyTYKz4BY",
       "Coward!" : "https://www.youtube.com/watch?v=9xWNyTwodXE",
       'You suck!' : "https://www.youtube.com/watch?v=XC4C-DwzaZI",
       "The cart is supposed to move forward!" : "https://www.youtube.com/watch?v=WO1zEznefDg",
       "We did it! I mean, of course we did it." : "https://www.youtube.com/watch?v=jvaFUSiXamM",
       "I dominate you, you sluggish simpleton." : "https://www.youtube.com/watch?v=Sb5QWMh_vzA",
       "Not our finest moment." : "https://www.youtube.com/watch?v=jOhxHBAz9bE"
        }