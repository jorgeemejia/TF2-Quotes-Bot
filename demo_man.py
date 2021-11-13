import random

def get_demo_man_quote():
    keys = list(demo_man_dict.keys())
    return random.choice(keys)

def get_demo_man_quote_url(quote):
    return demo_man_dict[quote]

demo_man_dict = {"Yer a back-pokin' snake, and by God you'll die like one!" : "https://www.youtube.com/watch?v=jYkMJp8YUes",
        "You're weak. I'm strong. and I win, toymaker!" : "https://www.youtube.com/watch?v=gngfYEuEbFI",
        "I almost joined their bloody team!" : "https://www.youtube.com/watch?v=YfxJA-ObKsg",
        "Time to get bluttered!" : "https://www.youtube.com/watch?v=FAFnPJbebZU",
        "I hope I didn't scare you with my face-to-face man fightin!" : "https://www.youtube.com/watch?v=r9izjPinYRQ",
        "Little too much caber-tossin' pie down yer own throat, eh, chubby?" : "https://www.youtube.com/watch?v=THIDhZDbby0",
        "Wizard! Show yerself!" : "https://www.youtube.com/watch?v=02-HU11qnys",
        "He's got that book that stole me eye!" : "https://www.youtube.com/watch?v=f_N7vIl-EGo",
        "Not one of ya's going to survive this!" : "https://www.youtube.com/watch?v=E35gJNViNIY"
        }


