import random

def get_scout_quote():
    keys = list(scout_dict.keys())
    return random.choice(keys)

def get_scout_quote_url(quote):
    return scout_dict[quote]



scout_dict = {"Screw you, Death" : "https://www.youtube.com/watch?v=1i3svP-Kp94",
         "Yeah, I dare ya, rage quit. C'mon make us both happy." : "https://www.youtube.com/watch?v=EgjpSnXmPD4",
         "We did it, Scary Hat! We did it because we're best friends." : "https://www.youtube.com/watch?v=jeiqUlL5ZIo",
         "You're like a car crash in slow motion. It's like I'm watchin' ya fly through a windshield" : "https://www.youtube.com/watch?v=Vc6yQ9GO5e0",
         "S'no problem. I do dis all the time. I could do dis for money, I don't, but I could." : "https://www.youtube.com/watch?v=1fZX5FxthWM",
         "It's happening! Oh God! It's happening!":"https://www.youtube.com/watch?v=X89NTUwWiE0" ,
         "I love my ball!" : "https://www.youtube.com/watch?v=CmWE9w_pAX0" ,
         "Ya head's a freakin' bat magnet!" : "https://www.youtube.com/watch?v=m2dka39Pios" ,
         "I love this game!" : "https://www.youtube.com/watch?v=iRrkg2OCis4",
         "Oh, dat's a skull fracture for sure!" : "https://www.youtube.com/watch?v=t6lYCUMGktc",
         "Did we win another one of these? Oh man, we are so good!" : "https://www.youtube.com/watch?v=Nj34YBXP_iA",
         "Wait, wait. Something beats rock?" : "https://www.youtube.com/watch?v=mkvDEZF9JLQ",
         "Gotta dance, I gotta dance!" : "https://www.youtube.com/watch?v=Q83sinuMyDg",
         "I'm dying here!" : "https://www.youtube.com/watch?v=sYGfzCBD7mo",
         "Are you freakin' kidding me?" : "https://www.youtube.com/watch?v=bJw_wcYh8lE",
         "Ya like that, chucklenuts?" : "https://www.youtube.com/watch?v=0RQdmoRhT6k",
         "Diagnosis: you suck!" : "https://www.youtube.com/watch?v=3_urjWZ3KcA",
         "I love winnin'! Love it!" : "https://www.youtube.com/watch?v=Kl3uEZUhxSw"

        }



# for key in scout_dict.keys():
#     print(scout_dict[key])

# keys = list(scout.keys())

# print(keys)

# for key in keys:
#     print(scout[key])