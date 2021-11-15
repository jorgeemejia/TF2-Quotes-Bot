import random 

def get_sniper_quote():
    keys = list(sniper_dict.keys())
    return random.choice(keys)

def get_sniper_quote_url(quote):
    return sniper_dict[quote]

sniper_dict = {"You're making this so easy, I'm actually getting worse." : "https://www.youtube.com/watch?v=4SH45dwczZA",
          "Now this is a knife!" : "https://www.youtube.com/watch?v=f_M9va9Ozng",
          "I see ya." : "https://www.youtube.com/watch?v=6C5dRpBnf3Q",
          "Fine shot, mate!" : "https://www.youtube.com/watch?v=C_UMjobugxM",
          "You want to hear something funny? You're dead." : "https://www.youtube.com/watch?v=Bjjli9ovP5s",
          "Thanks for that, Truckie" : "https://www.youtube.com/watch?v=vWYEwNON7Jo",
          "Not so smart with yer brains outside yer head, are ya?" : "https://www.youtube.com/watch?v=tjJeQ88m_U8",
          "Piss off, you bloody pikers!" : "https://www.youtube.com/watch?v=OFLrOMEyYL8",
          "Piss off, you bloody pikers." : "https://www.youtube.com/watch?v=2LplrSqIfhQ"
        }   