import random

def get_engineer_quote(*arg):
    keys = list(dict.keys())
    if arg:
        return(keys[arg[0]])
    else:
        return random.choice(keys)

def get_engineer_quote_url(quote):
    return dict[quote]

# def print_engineer_list():
#     keys = list(dict.keys())
#     for (i, item) in enumerate(keys, start = 0):
#         print(i, item)

def print_engineer_list():
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


dict = {"You are a coward and a scoundrel!" : "https://www.youtube.com/watch?v=wO9Ch3AHwRs",
            "Not bad. Not bad at all.": "https://www.youtube.com/watch?v=wBtKmgHWt64",
            "Whoo, look at all that money." : "https://www.youtube.com/watch?v=4RkX_-0-eRs",
            "Job well done." : "https://www.youtube.com/watch?v=WTse28OS3qA",
            "Dispenser going up." : "https://www.youtube.com/watch?v=AuhqE20xdNI",
            "I'm a killer of men, doc. That is the God's-honest truth." : "https://www.youtube.com/watch?v=yYZwQxX5f9k",
            "Doctor! I am the better man!" : "https://www.youtube.com/watch?v=Ibs21vdwEcM",
            "You are a whole herd'a ugly." : "https://www.youtube.com/watch?v=tHZjqHDqOG8",
            "And another thing: you're ugly." : "https://www.youtube.com/watch?v=wKbWW0WTh0k",
            "Y'all just got branded.":"https://www.youtube.com/watch?v=EH971ie6MZw",
            'You shoulda oughta brought more gun, son.':"https://www.youtube.com/watch?v=ey82Y1vJGbY",
            "Why don't you all get along before one of you gets hurt.":"https://www.youtube.com/watch?v=aS4ZDB6-FvI",
            "You're all about to have a real bad day!":"https://www.youtube.com/watch?v=gQvQ3AKdKuk",
            "Start prayin', boy!":"https://www.youtube.com/watch?v=q75VE8Vm_ic",
            "Don't worry, boys! The Engineer, is Engi-here!":"https://www.youtube.com/watch?v=aDuOk8COKPQ",
            "I'm wolverine-mean, you son of a Bitch.":"https://www.youtube.com/watch?v=ab-jPul8az8",
            "Drunk on the battlefield ain't no way to be, son.":"https://www.youtube.com/watch?v=grXNneUkY7E",
            'Oh my God.':"https://www.youtube.com/watch?v=1Vv0Nph2UPA",
            "I'm gonna lay you out!":"https://www.youtube.com/watch?v=VMXT4Zcqm3I",
            'Sniper!':"https://www.youtube.com/watch?v=d2rc_HPfUwU",
            'I need some doggone help!':"https://www.youtube.com/watch?v=gLjXuKLP5oc",
            'I will send every damn one of you back to robot hell!':"https://www.youtube.com/watch?v=fjHjARkDFjw",
            'Meeeh-dic!':"https://www.youtube.com/watch?v=U4SXWfeU1oA",
            'Medic!':"https://www.youtube.com/watch?v=8Bs28mNmeLQ",
            'Doc!':"https://www.youtube.com/watch?v=S1SC07x-yBg",
            "What in Sam Hill were you thinkin', string-bean?":"https://www.youtube.com/watch?v=9XKvQymsk10",
            'Damnit, fellas!':"https://www.youtube.com/watch?v=VZcwowk3q0U",
            'Slither on back to hell, coward!':"https://www.youtube.com/watch?v=gGTLcZjAs8A",
            'What dumb son of a bitch cast that?':"https://www.youtube.com/watch?v=rrOV3e4iiqo",
            "Hey boys, it's a Spy!":"https://www.youtube.com/watch?v=umrbbPT9l20",
            "Erectin' a statue of a moron.":"https://www.youtube.com/watch?v=kXHLPFiBhGY",
            "Let's do-si-do!":"https://www.youtube.com/watch?v=cPCQ2ifkry0",
            "This thing ain't on auto-pilot, son!":"https://www.youtube.com/watch?v=qySdzW5dYN4",
            "That's what it was made for.":"https://www.youtube.com/watch?v=Nolbb3TFYqA",
            'Whoooowee, would ya look at that!':"https://www.youtube.com/watch?v=2VGhovAioQ8",
            'Another satisfied customer!':"https://www.youtube.com/watch?v=iGyRu64JHdg",
            'Sometimes, you just need a little less gun.':"https://www.youtube.com/watch?v=NSWqA2xZhyQ",
            'Gotcha!':"https://www.youtube.com/watch?v=lx1EcO6ln08",
            "That's from yours truly, son.":"https://www.youtube.com/watch?v=8O26lle7hFo",
            "Whoooowee! Makin' bacon!":"https://www.youtube.com/watch?v=cJnf1ViI2tc",
            "I told ya don't touch that darn thing.":"https://www.youtube.com/watch?v=U5c33fl4Nh8",
            "How'd that plan turn out for ya, dummy?":"https://www.youtube.com/watch?v=gQbiSOCHPRU",
            'Take it like a man, shorty.':"https://www.youtube.com/watch?v=M_UWYSentzQ",
            'Thanks, mister!':"https://www.youtube.com/watch?v=JxEigiYqjNI",
            "Nice goin', pardner":"https://www.youtube.com/watch?v=OxT1uhc_sOs",
            'Tagged ya.':"https://www.youtube.com/watch?v=SKiOObZQ4dA",
            'I built that.':"https://www.youtube.com/watch?v=SL-Hwqd5C2U",
            "Spy's sappin' my Sentry!":"https://www.youtube.com/watch?v=3Evk5t_B6ag",
            "Buildin' a Sentry.":"https://www.youtube.com/watch?v=_Q6CVJA9HHE",
            "I'm gonna beat you like a rented mule, boy.":"https://www.youtube.com/watch?v=mPhwWakl1wY",
            'Dominated, corn cakes.':"https://www.youtube.com/watch?v=vznP1D7iuDo",
            'Come on, fellas!':"https://www.youtube.com/watch?v=MPiBwEislEc",
            "Y'all just got dominated, city boy.":"https://www.youtube.com/watch?v=qjYY4KOPPAk",
            #"I've seen better sides of beef, been run over by a combine.":"https://www.youtube.com/watch?v=yCAoaATAZLE",
            'Okay body, time to Teleport you to a world of physical fitness!':"https://www.youtube.com/watch?v=YQeJyJ_UtVc",
            '*drinking*. Aaaah, life of Reilly! Mmm.':"https://www.youtube.com/watch?v=U21xfZdP9wk",
            'Stupid face.':"https://www.youtube.com/watch?v=4NqHV1BpQHQ",
            'Cream gravy!':"https://www.youtube.com/watch?v=zYc201wEDDQ",
            'Nope!':"https://www.youtube.com/watch?v=O8uGgyT6KCQ",
            'Now just stop trying to mess with my contraptions!':"https://www.youtube.com/watch?v=dnKr4cPCd9o"
            }

# txt = print_engineer_list()
# print(txt)