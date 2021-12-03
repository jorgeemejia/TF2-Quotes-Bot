import random

def get_scout_quote(*arg):
    keys = list(dict.keys())
    if arg:
        return(keys[arg[0]])
    else:
        return random.choice(keys)

def get_scout_quote_url(quote):
    return dict[quote]

def print_scout_list():
    keys = list(dict.keys())
    for (i, item) in enumerate(keys, start = 0):
        print(i, item)


dict = {"Screw you, Death" : "https://www.youtube.com/watch?v=1i3svP-Kp94",
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
         "Diagnosis: you suck!" : "https://www.youtube.com/watch?v=3_urjWZ3KcA", #ERROR
         "I love winnin'! Love it!" : "https://www.youtube.com/watch?v=Kl3uEZUhxSw",
         "I don't know how to lose. I tried it once. It didn't work." : "https://www.youtube.com/watch?v=sl9krkGcOLc",
         "Yeah, there it is!" : "https://www.youtube.com/watch?v=WritlVcI3jE",
         "Hey, look at me, Ma!" : "https://www.youtube.com/watch?v=xeYYHj4IPQ0",
         "Hi, Ma!" : "https://www.youtube.com/watch?v=dgNGqMT1AWQ",
         "Doc! Come on, man!" : "https://www.youtube.com/watch?v=ymMFBpurOmg",
         "Medic!" : "https://www.youtube.com/watch?v=L5LLOq0VPZM",
         "MEDIC!" : "https://www.youtube.com/watch?v=OohIlelP8II",
         "Y'all know what, you're not scary, you're just weird." : "https://www.youtube.com/watch?v=GUDfh2GBR-I",
         "I'm runnin' circles around ya!" : "https://www.youtube.com/watch?v=H8c3PBL_vFA",
         "If you order now, I'll throw in a second beatin', absolutely free." : "https://www.youtube.com/watch?v=FjBhFgDBhpU",
         "What is your major malfunction, brother?" : "https://www.youtube.com/watch?v=GCJvPGNbp3k",
         "'Ey, is somebody keepin' track of my heads batted in?" : "https://www.youtube.com/watch?v=yPF3gvFbih8",
         "Hey, who's on fire now?" : "https://www.youtube.com/watch?v=QjA0n3o1HXk",
         "Hehey, I'm flyin'!" : "https://www.youtube.com/watch?v=dt9ERqz5Ay4",
         "Hey, I love brains.": "https://www.youtube.com/watch?v=X_DfFD-4xgM",
         "No seriously, you all suck!" : "https://www.youtube.com/watch?v=epkwn3nIZQU",
         "Wananananana..." : "https://www.youtube.com/watch?v=ZEfhljPE1pA",
         "Yeah, that's right!"  : "https://www.youtube.com/watch?v=_7bQ_HMo_UY",
         "Sweet" : "https://www.youtube.com/watch?v=JkbawKYFaEI",
         "How's that feel, wimp?" : "https://www.youtube.com/watch?v=i62an3f-XTE",
         "Yo, batter up!" : "https://www.youtube.com/watch?v=Plu66j928Y0",
         "Dat didn't hurt." : "https://www.youtube.com/watch?v=9jpHeEwf8Ho",
         "I'm gonna headbutt cha', I'm gonna headbutt cha', I'm gonna headbutt cha'!" : "https://www.youtube.com/watch?v=Rbjtl-e_iYA",
         "Man, your skull's so soft you're makin' this easy!" : "https://www.youtube.com/watch?v=W1YvUPMBnyM",
         "You're all losers!" : "https://www.youtube.com/watch?v=_ltEZCQi690",
         "You're a disgrace to the uniform, pal!"  : "https://www.youtube.com/watch?v=fZwGvwaU5hc",
         "Is-is anybody even payin' attention to me?" : "https://www.youtube.com/watch?v=bTy9sZfPKWY",
         "Eat it, fatty!" : "https://www.youtube.com/watch?v=RB5pJEdnd1I",
         "I will never... stop... killing you." : "https://www.youtube.com/watch?v=NKhVGwW2-Us",
         "Hit the bricks, pal. You're done."  : "https://www.youtube.com/watch?v=PQgXsWZibgk",
         "Hehey, look, you shapeshifted into a dead guy!"  : "https://www.youtube.com/watch?v=Fr8Df8rvrzk",
         "I wasted you": "https://www.youtube.com/watch?v=8Z0coIwjTXI",
         "Oh what, you gonna cry? You gonna cry now?" : "https://www.youtube.com/watch?v=LVst2xEaAq0",
         "Oh hey! You suck." : "https://www.youtube.com/watch?v=N0J6tqdBChA",
         "You... are... terrible!" : "https://www.youtube.com/watch?v=CXa3EnJmyEk",
         "Bonk/Boink" : "https://www.youtube.com/watch?v=ahs82jWWy-Y",
         "Drop dead and gimme 20!" : "https://www.youtube.com/watch?v=sL28sMkHACY",
         "You knuckleheads ain't even worth the effort."  : "https://www.youtube.com/watch?v=8j60kmy-T5A",
         "Not so tough now are ya? Are ya?!" : "https://www.youtube.com/watch?v=SCk3xQR5qIA",
         "That's what I'm talking about!" : "https://www.youtube.com/watch?v=0zKFXM2ly24",
         "What, ya guys give up?" : "https://www.youtube.com/watch?v=FkpCV5QKTuw",
         "Gravity? Who gives a crap about gravity?" : "https://www.youtube.com/watch?v=W9wu9D1_vRM",
         "I did it!" : "https://www.youtube.com/watch?v=dzKiMcp0p7I",
         "What is your major malfunction, brother?" : "https://www.youtube.com/watch?v=MbUTRWhoGOM",
         "Boom! I am a dance machine!" : "https://www.youtube.com/watch?v=s_dfQHbBRqs",
         "Boom! I'm back, dummy!" : "https://www.youtube.com/watch?v=Gzz-RVo-sXs",
         "I think I'll take Sasha out for a steak dinner tonight...": "https://www.youtube.com/watch?v=JT2UJZmp440",
         'Kay, this does not look good here, um...' : "https://www.youtube.com/watch?v=MA21GJuowvc",
         "Woow!" : "https://www.youtube.com/watch?v=ZkdzpGV9yfA",
         "I regret everything! I regret everything I've ever done!": "https://www.youtube.com/watch?v=illmRq0PATk",
         'Look at me!' : "https://www.youtube.com/watch?v=MyzAjE23f9o",
         'Play ball !': "https://www.youtube.com/watch?v=cCIZOc87Y7I",
         'Fire, fire, fire !': "https://www.youtube.com/watch?v=X1Uw32GslU0",
         'All right, I feel good.' : "https://www.youtube.com/watch?v=NEBZHiF2ooQ",
         'Ah, jeez !' : "https://www.youtube.com/watch?v=jZtFAmFUBDc",
         "I am the Scout here!" : "https://www.youtube.com/watch?v=d09rWYY05Xc",
         "It's startin' to bore me how much you suck." : "https://www.youtube.com/watch?v=bdAtBEXyjbY",
         'Yea.': "https://www.youtube.com/watch?v=5WUUDvuaaAE",
         "Repeat after me: mhmm-mhmm-mhmm I'm dead!": "https://www.youtube.com/watch?v=Kehh71pZ-TQ",
         "Mumnumnum.": "https://www.youtube.com/watch?v=GZbiz4hDUvI"

        }



# for key in scout_dict.keys():
#     print(scout_dict[key])

# keys = list(scout.keys())

# print(keys)

# for key in keys:
#     print(scout[key])