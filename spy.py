import random


def get_spy_quote(*arg):
    keys = list(dict.keys())
    if arg:
        return(keys[arg[0]])
    else:
        return random.choice(keys)

def get_spy_quote_url(quote):
    return dict[quote]

# def print_spy_list():
#     keys = list(dict.keys())
#     for (i, item) in enumerate(keys, start = 0):
#         print(i, item)

def print_half_spy_list():
    num = 0
    words = ""
    keys1 = list(dict.keys())
    actual_keys = keys1[:30]
    for actual_key in actual_keys:
        words += '['
        word_num = str(num)
        words += word_num
        words += ']'
        words += " "
        words += actual_key
        if num == 29:
            pass
        else:
            words += '\n'
        num += 1
    return words

def print_other_half_spy_list():
    num = 30
    words = ""
    keys2 = list(dict.keys())
    actual_keys = keys2[30:]
    for actual_key in actual_keys:
        words += '['
        word_num = str(num)
        words += word_num
        words += ']'
        words += " "
        words += actual_key
        words += '\n'
        num += 1
    return words

dict = {"You imbecile! You've doomed us all!" : "https://www.youtube.com/watch?v=4ZPDpTwoQKQ",
       "My appreciation, amigo." : "https://www.youtube.com/watch?v=M-ioiw5t1dE",
       "I appreciate your help." : "https://www.youtube.com/watch?v=6AAyTYKz4BY",
       "Coward!" : "https://www.youtube.com/watch?v=9xWNyTwodXE",
       'You suck!' : "https://www.youtube.com/watch?v=XC4C-DwzaZI",
       "The cart is supposed to move forward!" : "https://www.youtube.com/watch?v=WO1zEznefDg",
       "We did it! I mean, of course we did it." : "https://www.youtube.com/watch?v=jvaFUSiXamM",
       "I dominate you, you sluggish simpleton." : "https://www.youtube.com/watch?v=Sb5QWMh_vzA",
       "Not our finest moment." : "https://www.youtube.com/watch?v=jOhxHBAz9bE",
       "It's perfect!":"https://www.youtube.com/watch?v=2-j194j4SZk",
       "Your precious sandvich won't save you now, fatty!":"https://www.youtube.com/watch?v=iO28sXl-cZI",
       "Don't feel bad. You did a fine job tossing your little balls around!":"https://www.youtube.com/watch?v=0LzGPFFoQQQ",
       "Too easy.":"https://www.youtube.com/watch?v=SXqHamsA3iU",
       "This next game is ours!":"https://www.youtube.com/watch?v=URRP9A9Q9Kw",
       "Well, off to visit your mother!":"https://www.youtube.com/watch?v=ronPG90mvr8",
       "You disgust me!":"https://www.youtube.com/watch?v=OdGW1HVoE30",
       "Perhaps they can bury you in that van you call home.":"https://www.youtube.com/watch?v=heuiibBNXGk",
       "Nooooo!":"https://www.youtube.com/watch?v=SjSRIx9lESw",
       "May I borrow your earpiece? This is Scout! Rainbows make me cry! Over!":"https://www.youtube.com/watch?v=7963X500S_Y",
       "Jarate? Nooo...!":"https://www.youtube.com/watch?v=LL68rJmHomU",
       "Slap my hand.":"https://www.youtube.com/watch?v=IAsXjZU4bEs",
       "Hello again, dumb-bell!":"https://www.youtube.com/watch?v=iUGiqI38fiw",
       "Oh, Soldier, who will they ever find to replace you? Anyone! (laughs)":"https://www.youtube.com/watch?v=CyYsq-m45x8",
       "I'll see you in hell... you handsome rogue!":"https://www.youtube.com/watch?v=lr1eTusEYm8",
       "What the hell?":"https://www.youtube.com/watch?v=TYaxAPPsLvY",
       "Oh dear, I've made quite a mess.":"https://www.youtube.com/watch?v=6a1XlScEEi4",
       "The world will thank me for this, you monster!":"https://www.youtube.com/watch?v=nA-h4RxB8I8",
       "Well, that was idiotic!":"https://www.youtube.com/watch?v=U-tS0spz2VI",
       "Here lies Scout--he ran fast and died a virgin.":"https://www.youtube.com/watch?v=m4B8S3SBW4o",
       "Doctor!":"https://www.youtube.com/watch?v=HwaLviIcbng",
       "Doctor!!":"https://www.youtube.com/watch?v=q77462d2u98",
       "Medic!":"https://www.youtube.com/watch?v=zsfWRmr6HCU",
       "Gentlemen. I'm back!":"https://www.youtube.com/watch?v=Y-84J3115AY",
       "No coffin can contain me!":"https://www.youtube.com/watch?v=KY-Yh_rJ8cM",
       "I murdered your toys as well.":"https://www.youtube.com/watch?v=xdK2ZRm4D40",
       "All in a day's work.":"https://www.youtube.com/watch?v=tlqSVNvZOHc",
       "What the hell is that?!":"https://www.youtube.com/watch?v=oZhfxbW3sOk",
       "Push, damn you!":"https://www.youtube.com/watch?v=kTDU-NHI4UU",
       "Thank you, laborer!":"https://www.youtube.com/watch?v=LmSjlxwXAUE",
       "Voilà!":"https://www.youtube.com/watch?v=qQTuDPhU3e8",
       "But of course!":"https://www.youtube.com/watch?v=NDhKgybDolw",
       "Hmm. Not bad.":"https://www.youtube.com/watch?v=jZNAv1rY8LM",
       "Jarate? *cries*":"https://www.youtube.com/watch?v=kS-Ei7wsLcs",
       "Did you forget about me?!":"https://www.youtube.com/watch?v=r4fuic789L0",
       "Listen up gentlemen, time to get serious!":"https://www.youtube.com/watch?v=UGwNXUG9SeA",
       "Surprise!":"https://www.youtube.com/watch?v=OAWYn-L7mC4",
       "Is this... Mon Dieu!":"https://www.youtube.com/watch?v=7tzG97u13zc",
       "What a disaster!":"https://www.youtube.com/watch?v=Nwm4Z1_DZ2I",
       "You live in a van!":"https://www.youtube.com/watch?v=-ANpoD1V1AY",
       "I never really was on your side.":"https://www.youtube.com/watch?v=NohaeGg8LNY",
       "Promise not to bleed on my suit, and I'll kill you quickly.":"https://www.youtube.com/watch?v=KDg-iiMxuOI",
       "Well, the moment has passed, back to work!":"https://www.youtube.com/watch?v=VNqxH1xoIR8",
       "They can bury you in the 'Tomb of the Unskilled Soldier!":"https://www.youtube.com/watch?v=KFceqntTp_c",
       "Let's see. Yes, good! I still look magnificent.":"https://www.youtube.com/watch?v=Ukx9yIrZcck",
       "Well, the moment has passed, back to work!":"https://www.youtube.com/watch?v=6yEIKHZHcao",
       "It's the only one of its kind! And it's mine!":"https://www.youtube.com/watch?v=zHi0bxL2Oss",
       "I require assistance!":"https://www.youtube.com/watch?v=FkqqnT_i0Xo",
       "Spy among us!":"https://www.youtube.com/watch?v=3--5ssZ2-1g",
       "Very nice, very nice!":"https://www.youtube.com/watch?v=5UPWDLSvyjQ",
       "Abort! Abort!":"https://www.youtube.com/watch?v=Z9nxPJ1HC1Y",
       "Yes! My friend, we have done it!":"https://www.youtube.com/watch?v=7giOf9rpFWA",
       "Excellent.":"https://www.youtube.com/watch?v=a6-bHcoBlm4",
       "Damn it! We are losing ground!":"https://www.youtube.com/watch?v=HD_0SUgdT1c",
       "This will be the last time you see me.":"https://www.youtube.com/watch?v=xuYsw2xJeOs",
       "I feel très bon!":"https://www.youtube.com/watch?v=Y0JoeWwOiK4",
       "That is a diet I call 'death.":"https://www.youtube.com/watch?v=s1wnE3DsDo4",
       "I do believe I'm on fire.":"https://www.youtube.com/watch?v=2BrqdcHF_T4",
       "I'm looking at your x-ray, and I'm afraid you s**k!":"https://www.youtube.com/watch?v=JIw_eH3qD5Q",
       "You are such a bad doctor!":"https://www.youtube.com/watch?v=SWQc_wJqB3A",
       "Tell no one of this.":"https://www.youtube.com/watch?v=yuuNzPmv31c"
        }