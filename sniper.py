import random 

def get_sniper_quote(*arg):
    keys = list(dict.keys())
    if arg:
        return(keys[arg[0]])
    else:
        return random.choice(keys)

def get_sniper_quote_url(quote):
    return dict[quote]

# def print_sniper_list():
#     keys = list(dict.keys())
#     for (i, item) in enumerate(keys, start = 0):
#         print(i, item)

def print_half_sniper_list():
    num = 0
    words = ""
    keys1 = list(dict.keys())
    actual_keys = keys1[:25]
    for actual_key in actual_keys:
        words += '['
        word_num = str(num)
        words += word_num
        words += ']'
        words += " "
        words += actual_key
        if num == 24:
            pass
        else:
            words += '\n'
        num += 1
    return words

def print_other_half_sniper_list():
    num = 25
    words = ""
    keys2 = list(dict.keys())
    actual_keys = keys2[25:]
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


dict = {"You're making this so easy, I'm actually getting worse." : "https://www.youtube.com/watch?v=4SH45dwczZA",
          "Now this is a knife!" : "https://www.youtube.com/watch?v=f_M9va9Ozng",
          "I see ya." : "https://www.youtube.com/watch?v=6C5dRpBnf3Q",
          "Fine shot, mate!" : "https://www.youtube.com/watch?v=C_UMjobugxM",
          "You want to hear something funny? You're dead." : "https://www.youtube.com/watch?v=Bjjli9ovP5s",
          "Thanks for that, Truckie" : "https://www.youtube.com/watch?v=vWYEwNON7Jo",
          "Not so smart with yer brains outside yer head, are ya?" : "https://www.youtube.com/watch?v=tjJeQ88m_U8",
          "Piss off, you bloody pikers!" : "https://www.youtube.com/watch?v=OFLrOMEyYL8",
          "Piss off, you bloody pikers." : "https://www.youtube.com/watch?v=2LplrSqIfhQ",
          "God Save the Queen!" :'https://www.youtube.com/watch?v=ckQv9aV1Boc',
          "Ah... Piss!" :'https://www.youtube.com/watch?v=N0UI4y7-4cY',
          "Well, Happy Australia Day to me.":'https://www.youtube.com/watch?v=i61pCLzMgQg',
          "The bullets come outta the slim end, mate!":'https://www.youtube.com/watch?v=pPSXL_OenDU',
          "Come to Sniper, my little beauty.":'https://www.youtube.com/watch?v=egaCrZVKGm0',
          "Ah! What the bloody hell just happened?":'https://www.youtube.com/watch?v=zIYfmlxbcS0',
          "Here's a touchin' story. Once upon a time you died, and I lived happily ever..":'https://www.youtube.com/watch?v=mLU5uyR9rmE',
          "I just bagged the world's fattest man!"  :'https://www.youtube.com/watch?v=-OCpcn9cuec',
          "Huhbluhbluhbluhbluhbluh! Bloody hell!":'https://www.youtube.com/watch?v=gC6-wWLr6CM',
          "Yeah, that seems about right!":'https://www.youtube.com/watch?v=hbvEX4b2WOQ',
          "Wave goodbye to your head, wanker." :'https://www.youtube.com/watch?v=3HG3iEPQp54',
          #"Piss off, big-head!" :'https://www.youtube.com/watch?v=-mFwP41VCaU',
          "It's a miracle. It's an Australian Christmas bloody miracle!":'https://www.youtube.com/watch?v=6rpCNKUNGXc',
          "Help me pin this down!":'https://www.youtube.com/watch?v=d0FXxaDJuEE',
          "You got a forehead on ya like a coffee table.":'https://www.youtube.com/watch?v=Z7aD_aPRGSE',
          "I'm gonna carve you a new cake hole!":'https://www.youtube.com/watch?v=OQKec-dwfuc',
          "Oi! Yer bleedin' gravy, fatso!" :'https://www.youtube.com/watch?v=dA7heD_YAvM',
          "One Sniper to another, mate: Give! Up!":'https://www.youtube.com/watch?v=ishoGIz0j1M',
          "You're better than the best, mate. You're a Sniper.":'https://www.youtube.com/watch?v=gu4Eb9UT_vU',
          "Gotcha, ya pot-bellied lardass!":'https://www.youtube.com/watch?v=YHx6LA-asHk',
          "Aw, beaut! We did it!":'https://www.youtube.com/watch?v=4TsVFm3ck5g',
          "No worries.":'https://www.youtube.com/watch?v=SvQD6_l_zV4',
          "You. Are. A. Bloody. Disgrace.":'https://www.youtube.com/watch?v=KrbXol9Km4M',
          "All in a days work.":'https://www.youtube.com/watch?v=6l6a8UtMzQc',
          "Medic!":'https://www.youtube.com/watch?v=v0WptQh1KIw',
          "Gotcha, ya bomb-lobbin' wanker!":'https://www.youtube.com/watch?v=wCMD07JaENY',
          "Now this is a nice weapon.":'https://www.youtube.com/watch?v=YCJyaONKcMw',
          "I'm a dinkum Aussie, not some bloody cartoon!":'https://www.youtube.com/watch?v=0e5JQaBjbYs',
          "Everything above your neck is going to be a fine red mist.":'https://www.youtube.com/watch?v=TUKFZ9DrMRA',
          "Now I gotta make a necklace outta your teeth, bushman's rules.":'https://www.youtube.com/watch?v=SGWDfaLw6JM',
          "Thanks for the target practice, ya plump bloody freakshow!":'https://www.youtube.com/watch?v=GMh-l55aAl8',
          "Skill always beats luck, ya weasel.":'https://www.youtube.com/watch?v=vuPMtP1Z0Z4',
          "I'm gonna blow the inside of ya head all over four counties!":'https://www.youtube.com/watch?v=63UA_UN3oog',
          "That's some shonky business right there!":'https://www.youtube.com/watch?v=z68hGfL9QMM',
          "Ahh, that's apples mate.":'https://www.youtube.com/watch?v=yTk3YyH50do',
          "Let's dance!":"https://www.youtube.com/watch?v=fWbyiyA2Ub8",
          "All your heads look bloody twelve feet tall.":"https://www.youtube.com/watch?v=jCXxXaz5K0s",
          "You're all a bunch of no-hopers!" :"https://www.youtube.com/watch?v=_uVjNNnLSeg",
          "Mongrel!":"https://www.youtube.com/watch?v=bdu7ScO0Sx4",
          "A little of the ol' 'chop-chop'!":"https://www.youtube.com/watch?v=Z-hzpqTRlzA",
          "Who wants some bloody horn?!":"https://www.youtube.com/watch?v=Y9X2kAThzgY",
          "Owl Jarate!" :"https://www.youtube.com/watch?v=7JaSKRggGqE",
          "No worries!":"https://www.youtube.com/watch?v=3gaQhgLipQI",
          "I have an owl head *long scream*":"https://www.youtube.com/watch?v=sCgmx6VDAqA",
          "Get to it!" :"https://www.youtube.com/watch?v=QIQe3K7-iHQ",
          "Quit blubberin' and take yer medicine like a man!":"https://www.youtube.com/watch?v=OdMtajN66Tc",
          "You know what you and Jane Austen have in common..." :"https://www.youtube.com/watch?v=tiVsT2iSgBw",
          "That helmet's going to make a nice bowl for ya brains!":"https://www.youtube.com/watch?v=nQeBvl6mHFY",
          "You bloody pikers!":"https://www.youtube.com/watch?v=nXO3aBqSjQo",
          "Okay, mate!":"https://www.youtube.com/watch?v=Io-8Xd6ryWo",
          "You are a creepy, mute little bugger, ain't ya?":"https://www.youtube.com/watch?v=gAmUylmYESc",
          "This is gonna be a real piece of piss...":"https://www.youtube.com/watch?v=ieYFa3h3-r4",
          "Someone's about to have a very bad day.":"https://www.youtube.com/watch?v=cQPwLtpQr04",
          "I'm gonna carve you a new cake hole!":"https://www.youtube.com/watch?v=XsZaSQIvp-M",
          "I am the king of Australia!":"https://www.youtube.com/watch?v=j6o0zREYFDs",
          "Let's make some bloody magic!":"https://www.youtube.com/watch?v=GqUy-DSugWM"
             }   

# print_sniper_list()