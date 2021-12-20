import random
from typing import Text


def get_heavy_quote(*arg):
    keys = list(dict.keys())
    if arg:
        return(keys[arg[0]])
    else:
        return random.choice(keys)

def get_heavy_quote_url(quote):
    return dict[quote]

# def print_heavy_list():
#     keys = list(dict.keys())
#     for (i, item) in enumerate(keys, start = 0):
#         print(i, item)

def print_half_heavy_list():
    num = 0
    words = ""
    keys1 = list(dict.keys())
    actual_keys = keys1[:65]
    for actual_key in actual_keys:
        words += '['
        word_num = str(num)
        words += word_num
        words += ']'
        words += " "
        words += actual_key
        if num == 64:
            pass
        else:
            words += '\n'
        num += 1
    return words

def print_other_half_heavy_list():
    num = 65
    words = ""
    keys2 = list(dict.keys())
    actual_keys = keys2[65:]
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

dict = {"Get behind me doctor!" : "https://www.youtube.com/watch?v=7duMsdAtrO8",
         "Little little man." : "https://www.youtube.com/watch?v=MG3v3_ahd3Q",
         "Do you remember me now?!": "https://www.youtube.com/watch?v=B_eX15hz_Is",
         "I am angry!" : "https://www.youtube.com/watch?v=UNEubxOT-5E",
         "Ha ha ha ha! Heavy is back babies!" : "https://www.youtube.com/watch?v=8ILFT198-WY",
         "Who. Touched. My. Gun." : "https://www.youtube.com/watch?v=ATtE-deTW2s",
         "Get behind pretty pink pony mane, Doctor!" : "https://www.youtube.com/watch?v=b7qanrgwbd4",
         "Run, cowards! Tweet tweet tweeeet!" : "https://www.youtube.com/watch?v=530I7ZPc6CE",
         "Shh... Sasha is asleep." : "https://www.youtube.com/watch?v=jQV0e4AJtn4",
         "HEAVY IS PRETTY PRINCESS!" :"https://www.youtube.com/watch?v=LwPK_JGQiSM",
         "All of you are dancing babies!":"https://www.youtube.com/watch?v=HfgFSfJU8ys",
         "Now is coward killing time!":"https://www.youtube.com/watch?v=1e-HGyU8hVM",
         "Thank you for life, doktor":"https://www.youtube.com/watch?v=SVWg2u31PDs",
         "Not so mighty now, tiny giant.":"https://www.youtube.com/watch?v=Sa62vtw6fxE",
         "You are best of best!":"https://www.youtube.com/watch?v=Vg5AyJ1lUXY",
         "I see Spy!":"https://www.youtube.com/watch?v=axUS0lUCzsM",
         "Oh nooooo!":"https://www.youtube.com/watch?v=gcqthHu0ahs",
         "Time to hide, cowards!":"https://www.youtube.com/watch?v=p5AEfZ5fNvs",
         "Bomb is friend! Come, visit friend!":"https://www.youtube.com/watch?v=gmk6Y-4Kwa0",
         "Heavy is flying! Is greatest moment of Heavy's life!":"https://www.youtube.com/watch?v=hRT7_yYx9jw",
         "The burning you feel? It is shame.":"https://www.youtube.com/watch?v=I6p-082zK08",
         "It is good day to be Giant Man!":"https://www.youtube.com/watch?v=ilzaOOfsPLA",
         "It is good day to be Giant Man.":"https://www.youtube.com/watch?v=xosAX7SeLr4",
         "Yes." :"https://www.youtube.com/watch?v=BGJhpeqn_6I",
         "Huh, Heavy feel funny." :"https://www.youtube.com/watch?v=FvBXVxp6AsM",
         "Oh, this is bad!":"https://www.youtube.com/watch?v=8rYBN3MOfyc",
         "Did you think I would forget you?!":"https://www.youtube.com/watch?v=VaLbhjekRy8",
         "HEAVY IS MADE OF SUGAR PLUMS!":"https://www.youtube.com/watch?v=RQ96NDpy3t0",
         "Never give up!":"https://www.youtube.com/watch?v=ZHVE3d3ha8g",
         "Tell me, where did we go so wrong?":"https://www.youtube.com/watch?v=kxgJnfuqy8M",
         "Argh! Cart is not moving!":"https://www.youtube.com/watch?v=7nNUA77gpLA",
         "What's the matter with you?":"https://www.youtube.com/watch?v=p4W6PujHvX4",
         "Which one of you is crying?":"https://www.youtube.com/watch?v=Kwww6TUeqgQ",
         "So much blood!":"https://www.youtube.com/watch?v=JlZHEo3n3VQ",
         "Bomb!" :"https://www.youtube.com/watch?v=X7UqgR1KWFs",
         "Taaaank!" :"https://www.youtube.com/watch?v=CnrN7GcljDs",
         "Your doctor is dead!":"https://www.youtube.com/watch?v=fHO2crM-4wk",
         "You drew first! Hahahahaha!":"https://www.youtube.com/watch?v=zNi2bSpUoNI",
         "You are now without doctor!" :"https://www.youtube.com/watch?v=A-L4fZf1SCI",
         "We make good team!":"https://www.youtube.com/watch?v=5ZDaZrVXDMg",
         "My fists! They are made of STEEL!":"https://www.youtube.com/watch?v=oGdv-TIU88Y",
         "Engineer is credit to team!":"https://www.youtube.com/watch?v=Ajvku_KiwnM",
         "I am bulletproof!":"https://www.youtube.com/watch?v=QOnvSBbiTDs",
         "Hmmm, tiny robots are in big trouble now." :"https://www.youtube.com/watch?v=BAWOwYxXbCQ",
         "I feel bigger *Laughs* good.":"https://www.youtube.com/watch?v=xdJMszArj50",
         "Yes!" :"https://www.youtube.com/watch?v=IcT_5PewZpQ",
         "MEDIC!":"https://www.youtube.com/watch?v=IJQtU4Jr44Q",
         "Doctor!":"https://www.youtube.com/watch?v=IncHyS5G_iI",
         "Help now!":"https://www.youtube.com/watch?v=fbd24Xd_dGc",
         "I am most dangerous man, in history of WORLD!":"https://www.youtube.com/watch?v=IURROOKjYOE",
         "Let us begin.":"https://www.youtube.com/watch?v=dgAob345cFA",
         "Saww-ndvich, sandvich!":"https://www.youtube.com/watch?v=_97PxQpSlDI",
         "Put up fists." :"https://www.youtube.com/watch?v=osqwACzqBBw",
         "Hoh, something is different.":"https://www.youtube.com/watch?v=VlOawpbGeIY",
         "Let us fight; man versus tiny baby man." :"https://www.youtube.com/watch?v=XWsuYsvIbqo",
         "Hmm. Is nice.":"https://www.youtube.com/watch?v=667s9MIafq0",
         "We must collect money.":"https://www.youtube.com/watch?v=3-BPefhuBjo",
         "I think you should fight someone much, much smaller.":"https://www.youtube.com/watch?v=16ikMQ_Vljg",
         "Good-Bye!" :"https://www.youtube.com/watch?v=y8UcnG87Fhw",
         "Dance or I crush you!":"https://www.youtube.com/watch?v=4n90SDfkgGo",
         "Hit me. I dare you." :"https://www.youtube.com/watch?v=GMCLCTvB45M",
         "I am very happy!":"https://www.youtube.com/watch?v=GmZ3rVB_mzU",
         "Sandvich make me strong!":"https://www.youtube.com/watch?v=g92zOQ70sRU",
         "What was that?":"https://www.youtube.com/watch?v=PQEHTwFe5y8",
         "All will fear my giant new gun.":"https://www.youtube.com/watch?v=qUnHlT5lWEs",
         "All of you are babies!":"https://www.youtube.com/watch?v=kMAiEZ45KrQ",
         "New weapon is good!" :"https://www.youtube.com/watch?v=RmxlGimxU5I",
         "Yes. I like this new weapon.":"https://www.youtube.com/watch?v=304Dr6KhEaE",
         "New weapon!":"https://www.youtube.com/watch?v=mBdftJWowsc",
         "*Crying Heavy*":"https://www.youtube.com/watch?v=DvnfpDVLWOI",
         "A spy!":"https://www.youtube.com/watch?v=WBtVSUNGaqM",
         "Vzzzzzt! Rahrahrahrah! Vrrrrr! Wahahahaaaaaa!":"https://www.youtube.com/watch?v=nXPh08ruVOU",
         "I destroy coward toys!":"https://www.youtube.com/watch?v=_cRzeXNOiMQ",
         "Keep crying, baby!":"https://www.youtube.com/watch?v=NqkRD4DMAuE",
         "All of you are dead!" :"https://www.youtube.com/watch?v=Kzk_7dK_pNA",
         "New gun is unfair to tiny baby enemies.":"https://www.youtube.com/watch?v=---gzcVXOcU",
         "I hear someone building diaper changing station!":"https://www.youtube.com/watch?v=XMUt0k1Kqzc",
         "Who send all these babies to fight!?":"https://www.youtube.com/watch?v=i8Bh7PwS9rU",
         "I am Heavy Weapons Guy, and this is my new weapon.":"https://www.youtube.com/watch?v=uF8ETnJSVng",
         "I'm coming for you!":"https://www.youtube.com/watch?v=o3UjCh_cods",
         "I have new way to kill cowards.":"https://www.youtube.com/watch?v=S4NpIkDHPAg",
         "More rubble, less trouble!":"https://www.youtube.com/watch?v=7e9LIj-_pgc",
         "Go ahead! Build your tiny gun then run!":"https://www.youtube.com/watch?v=RI4iQP0L5iQ",
         "I have new weapon!":"https://www.youtube.com/watch?v=o4hODghKI7Y",
         "Caputus crepitus!":"https://www.youtube.com/watch?v=Xnfi9K-SyBg",
         "Seismela tremoro!":"https://www.youtube.com/watch?v=OmUQT65_Zyo",
         "You are so small! Is funny to me!":"https://www.youtube.com/watch?v=3S2J5DZ8FBs",
         "We are done.":"https://www.youtube.com/watch?v=UAxzMC4hgk8",
         "Get on point, stupid!":"https://www.youtube.com/watch?v=GPwD9BOWZiA",
         "Attack book!" :"https://www.youtube.com/watch?v=kqsDIDqQ7H4",
         "Keep dancing, babies!":"https://www.youtube.com/watch?v=unwJQ3TCNlc",
         "The medal- it is so tiny!":"https://www.youtube.com/watch?v=rgr1bfhqqAA",
         "Conga, conga, conga!":"https://www.youtube.com/watch?v=Ff9mczI2fPk",
         "I promise you pain without end!":"https://www.youtube.com/watch?v=MZ9Ztjm2Flo",
         'Very good, very, very good!':"https://www.youtube.com/watch?v=-WVEgjeVK7E",
         "My doctor's still alive!" :"https://www.youtube.com/watch?v=7DlwaXx10VU",
         "Don't run! It's just ham!":"https://www.youtube.com/watch?v=t3nIFalT_-8",
         'Killing you is full time job now.':"https://www.youtube.com/watch?v=fGI9eXZIK10",
         'I love this doctor!':"https://www.youtube.com/watch?v=q1h3kmtBg8c",
         "Ooohhh, run, run, I'm coming for you!":"https://www.youtube.com/watch?v=Xms9ECtiNug",
         'You cannot hide, coward.':"https://www.youtube.com/watch?v=H72EUvo8huw",
         'Run home to momma!':"https://www.youtube.com/watch?v=UZclg7_AkxI",
         'Hide coward! I will find you.':"https://www.youtube.com/watch?v=EACJYCS--Sc",
         'Cry some more!':"https://www.youtube.com/watch?v=21U6k9M2TU4",
         'Nooo !!!' :"https://www.youtube.com/watch?v=SOGxzuZtmMs",
         'No! Cart moves wrong way!' :"https://www.youtube.com/watch?v=drkM6PKQpDw",
         'I am full of Sandvich, and I am coming for you!' :"https://www.youtube.com/watch?v=4T7GyXCGvi4",
         'Let this be lesson for you!':"https://www.youtube.com/watch?v=kG1vple0AAQ",
         "Brush Heavy's hair! BRUSH IT!":"https://www.youtube.com/watch?v=sbBnt21_l-c",
         'We lose, but they do not win?':"https://www.youtube.com/watch?v=CS16yLaFXiM",
         'What sick man sends babies to fight me?':"https://www.youtube.com/watch?v=7VM6Ui7VM6g",
         'Is good!':"https://www.youtube.com/watch?v=9a0AMDyZDXc",
         'Kiss me':"https://www.youtube.com/watch?v=OQrjcFCgKhI",
         'You are dead, not big suprise!':"https://www.youtube.com/watch?v=3fqYMRCyq_g",
         "Ho, hohoho, oh that slaps me on the knee!" :"https://www.youtube.com/watch?v=xSFEfWc_g60",
         'Medic!':"https://www.youtube.com/watch?v=zOUFI9T4_TA",
         'Entire team is babies!':"https://www.youtube.com/watch?v=wFGQXjlAXEg",
         'Sandwich and me going to beat your ass.':"https://www.youtube.com/watch?v=KaAJ4tj2C0A",
         'Good!':"https://www.youtube.com/watch?v=OlEfJAeJ5yw",
          'Come, sing with me!':"https://www.youtube.com/watch?v=sq7JTNc4q54",
         'Pootis spencer here!':"https://www.youtube.com/watch?v=g857eh1wBCo",
         'Nom nom nom, om nom!':"https://www.youtube.com/watch?v=kO1Yq7n9zLU",
         'Ya-dadadadad...':"https://www.youtube.com/watch?v=2yOvI-zMi_I",
         'What was that Sandvich? Kill them all? Good idea!':"https://www.youtube.com/watch?v=KqUBAS-aSTY",
         'No!':"https://www.youtube.com/watch?v=kiA_wC01KKo",
         "Stupid stupid stupid!":"https://www.youtube.com/watch?v=dRi_OPgICCA"
        }

# print_heavy_list()

# Text1 = print_half_heavy_list()
# Text2 = print_other_half_heavy_list()

# print(Text1)
# print(Text2)