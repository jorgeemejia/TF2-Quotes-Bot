import random
from typing import Text

def get_soldier_quote(*arg):
    keys = list(dict.keys())
    if arg:
        return(keys[arg[0]])
    else:
        return random.choice(keys)

def get_soldier_quote_url(quote):
    return dict[quote]

def print_soldier_list():
    keys = list(dict.keys())
    for (i, item) in enumerate(keys, start = 0):
        print(i, item)

def print_half_soldier_list():
    num = 0
    words = ""
    keys1 = list(dict.keys())
    actual_keys = keys1[:35]
    for actual_key in actual_keys:
        words += '['
        word_num = str(num)
        words += word_num
        words += ']'
        words += " "
        words += actual_key
        if num == 34:
            pass
        else:
            words += '\n'
        num += 1
    return words

def print_other_half_soldier_list():
    num = 35
    words = ""
    keys2 = list(dict.keys())
    actual_keys = keys2[35:70]
    for actual_key in actual_keys:
        words += '['
        word_num = str(num)
        words += word_num
        words += ']'
        words += " "
        words += actual_key
        if num == 69:
            pass
        else:
            words += '\n'
        num += 1
    return words

def print_last_half_soldier_list():
    num = 70
    words = ""
    keys2 = list(dict.keys())
    actual_keys = keys2[70:]
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


dict = {'A big mug of my foot up your ass!': "https://www.youtube.com/watch?v=fwyQl_YUwnc",
            "Thanks, soldier." : "https://www.youtube.com/watch?v=6Hj5rC4snqw",
            "You were loud and ugly and now you're DEAD! Amen." : "https://www.youtube.com/watch?v=eKbcTbQIMqc",
            "You were good son, real good; maybe even the best." : "https://www.youtube.com/watch?v=jaQnQ17s4AQ",
            "Hooah!" : "https://www.youtube.com/watch?v=-U1mlDNSOSw",
            "This is my world. You are not welcome in my world." : "https://www.youtube.com/watch?v=2DT2uhpm7nU",
            "Screamin' Eagles!" : "https://www.youtube.com/watch?v=V7YBuu-KxgU",
            "Forward!" : "https://www.youtube.com/watch?v=Pqrm2eYX55w",
            "You will not be missed." : "https://www.youtube.com/watch?v=7gYIzcUxlSQ",
            "Godspeed, you magnificent bastard.":"https://www.youtube.com/watch?v=nWDCIbrKnwg",
            "Time to inform your next of kin!":"https://www.youtube.com/watch?v=LMUup5x6jkk",
            "Blammo!":"https://www.youtube.com/watch?v=9FQmCXpST18",
            "Ka-boom!":"https://www.youtube.com/watch?v=SP8FLLbcaio",
            "You're dead, that's good, amen.":"https://www.youtube.com/watch?v=klFUZ2LQuh8",
            "Boom!":"https://www.youtube.com/watch?v=f8wuSYlViO8",
            "You are all weak. You are all bleeders.":"https://www.youtube.com/watch?v=-di9LocPINI",
            "Maggots!":"https://www.youtube.com/watch?v=sYqpNfHC1d8",
            "Oh yeah!":"https://www.youtube.com/watch?v=LQ9U6qlg-rw",
            "Take your lumps like a man, Private Twinkletoes.":"https://www.youtube.com/watch?v=8H4AYKpbudQ",
            "Pa-POW!":"https://www.youtube.com/watch?v=KnWoGh4LXHI",
            "This is not a camping trip, Sheila; this is war and I love it!":"https://www.youtube.com/watch?v=9MU8s5fcOxY",
            "I will send my condolences to your kangaroo wife.":"https://www.youtube.com/watch?v=0oV7S0Jot8Y",
            "Welcome to the United States of, you just got dominated!":"https://www.youtube.com/watch?v=xhDTjiIvuNk",
            "I'm gonna break this tie over my knee!":"https://www.youtube.com/watch?v=sizccpZYAcA",
            "Consider yourself dominated, you Scotch son of a b**ch!":"https://www.youtube.com/watch?v=h2O0acpMIjg",
            "Stop lagging and start tagging, men!":"https://www.youtube.com/watch?v=zPXgNMaGFVY",
            "I'm going to tell you ladies a secret. I hate losing!":"https://www.youtube.com/watch?v=4MgMYD-6i_k",
            "Gotcha, crouton.":"https://www.youtube.com/watch?v=e0zNBE5FsAI",
            "America wins again!":"https://www.youtube.com/watch?v=dV3YkOKI1Eo",
            "Booo...":"https://www.youtube.com/watch?v=n3xYX8W_iX4",
            "Checkmate, Stalingrad!":"https://www.youtube.com/watch?v=evHuK2LoUG4",
            "I never liked you.":"https://www.youtube.com/watch?v=SMcqiVWZ-EA",
            "Merasmus, I hate you!":"https://www.youtube.com/watch?v=4J8o8H8tUSA",
            "Your magic is weak, wizard!":"https://www.youtube.com/watch?v=H1O-Z68tXXs",
            "Your mouth wrote checks, my gun has cashed them.":"https://www.youtube.com/watch?v=OzTAp2Q0TkU",
            "Never bring a bat to a battlefield, war is not a game.":"https://www.youtube.com/watch?v=v7IELYu0fpk",
            "Got anything funny to say about that, funny man?":"https://www.youtube.com/watch?v=-jEOu3I8RkE",
            "I am painis cupcake i will eat you.":"https://www.youtube.com/watch?v=876jCFneUzw",
            "You are a spineless worm!...":"https://www.youtube.com/watch?v=C6KLWr0t7NI",
            "Attack!":"https://www.youtube.com/watch?v=8XOAXLfv1BY",
            "Charge!":"https://www.youtube.com/watch?v=94Q9u3DFRIE",
            "Oh look it's Houdini. What's that Hougenie?...":"https://www.youtube.com/watch?v=Z3n9UasNEOY",
            "If God had wanted you to live, he would not have created me!":"https://www.youtube.com/watch?v=1_xvLtGyr9E",
            "Merasmus! I am going to pull a rabbit out of your ass!":"https://www.youtube.com/watch?v=p4ieOF3Z8WU",
            "Box!":"https://www.youtube.com/watch?v=pavRFUdtaA0",
            "Painis.":"https://www.youtube.com/watch?v=VRVaYzeEouI",
            "Pain is weakness leaving the body!":"https://www.youtube.com/watch?v=XEtzB7PaVLI",
            "Painis cupcake":"https://www.youtube.com/watch?v=cZofQJpmLxk",
            "You have dishonored this entire unit!":"https://www.youtube.com/watch?v=O4obwEbdkHg",
            "This is what God would use to shoot somebody.":"https://www.youtube.com/watch?v=TEwMEmgAtiI",
            "Your country did not prepare you for the level of violence you will... ":"https://www.youtube.com/watch?v=cprc8EiBBxw",
            "I am not trapped in a facility full of robots. You are all trapped in...":"https://www.youtube.com/watch?v=R7SR_g5gwfI",
            "Today is a good day.":"https://www.youtube.com/watch?v=OMpFXAG4bqA",
            "Damn you, Merasmuuuuus! You are the worst roommaaaaaaaaate!":"https://www.youtube.com/watch?v=z-9WZ-RTz6U",
            "Stars and Stripes beats Hammer and Sickle. Look it up!":"https://www.youtube.com/watch?v=B_xcbu-C31A",
            "My blood! No!":"https://www.youtube.com/watch?v=iAXnaQm0TD0",
            "Merasmus! I need that blood!":"https://www.youtube.com/watch?v=oJW0RfqweNY",
            "Scotland is not a real country; you are an Englishman with a dress.":"https://www.youtube.com/watch?v=Xq4bDgX1rUc",
            "Mediic!":"https://www.youtube.com/watch?v=7a-FYUInrpU",
            "MEDIC!":"https://www.youtube.com/watch?v=txJTv3Jio6I",
            "Medic!":"https://www.youtube.com/watch?v=KIi_wnyyqAI",
            "Get a haircut, trashcans.":"https://www.youtube.com/watch?v=fpXboddNLHA",
            "I am scared, you maggots!":"https://www.youtube.com/watch?v=yvSRn6FzK5A",
            "Get a haircut, hippie.":"https://www.youtube.com/watch?v=nxGIlboamdU",
            "We give up, Merasmus! You're too scary for us! Now come on out so we can...":"https://www.youtube.com/watch?v=DCg08NtuMVs",
            "Holy Mary, mother of Joseph!":"https://www.youtube.com/watch?v=Fv46_4OWJuI",
            "Never forget, always remember. Pepper fie.":"https://www.youtube.com/watch?v=zskJBP3zT2s",
            "U! S! A!":"https://www.youtube.com/watch?v=WMQ-6b3AtAE",
            "I have uploaded a boot up your metal asses!":"https://www.youtube.com/watch?v=Li4x57NzLcE",
            "No guts, no glory, robots!":"https://www.youtube.com/watch?v=tFdgdIJTZ2o",
            "I will open up your chassis and use you all as a latrine!":"https://www.youtube.com/watch?v=YXVu09vLttA",
            "Human grit always beats robot magic.":"https://www.youtube.com/watch?v=kKkpydH-Yt8",
            "All men gave some. Some men gave more than some.":"https://www.youtube.com/watch?v=3gG52sJy_4g",
            "I joined this team just to kill maggots like you.":"https://www.youtube.com/watch?v=d2u-riNwT8g",
            "Hello again!":"https://www.youtube.com/watch?v=oYmqFFzk91U",
            "Back from Hell!":"https://www.youtube.com/watch?v=KVczuV1eSV8",
            "Big robot!":"https://www.youtube.com/watch?v=Fgg0RpzGZq8",
            "I am having a heart attack!":"https://www.youtube.com/watch?v=zC9XqM96a9k",
            "You are all maggots! Oop, sorry brain maggot I forgot you were there.":"https://www.youtube.com/watch?v=HJuggBqdOO8",
            "I am a robot! I am here to take American jobs!":"https://www.youtube.com/watch?v=lXMg9_LZfes",
            "Give 'em hell boys!":"https://www.youtube.com/watch?v=1p-clJO4o0U",
            "Sir, yes, Sir!":"https://www.youtube.com/watch?v=8DJGRgLZbw4",
            "My head smells delicious!":"https://www.youtube.com/watch?v=5kkVKOFjYfU",
            "That is not a hat, that is an excuse to kick your ass!":"https://www.youtube.com/watch?v=0NqQy7DyWSQ",
            "Well that went pear-shaped fast!":"https://www.youtube.com/watch?v=uWRIqQPLNio",
            "If I have to crack some skulls, I will.":"https://www.youtube.com/watch?v=e5ZHb49WwZU",
            "You are a coward, and you died like one.":"https://www.youtube.com/watch?v=qe5EaFP-sk4",
            "That was an amazing killing spree... by the other team!":"https://www.youtube.com/watch?v=9kMfyLPk8cQ",
            "Thanks for the Teleporter.":"https://www.youtube.com/watch?v=d-0H2t3DhAg",
            "Thanks, Engie.":"https://www.youtube.com/watch?v=fUHxB6JmLO4",
            "Grab that cash boys, we earned it.":"https://www.youtube.com/watch?v=RspgXnqxMR0",
            "Each and every one of you will be sent home to your momma' in a box!":"https://www.youtube.com/watch?v=8Tjy49WTOx4",
            "The last word out of your sorry mouth will be Sir, and it will be loud!":"https://www.youtube.com/watch?v=330wXH4ciIQ",
            "Everyone, please stand! [singing] God bless America, land of... ":"https://www.youtube.com/watch?v=jQhEHwvP14g",
            "C'mere, cupcake!":"https://www.youtube.com/watch?v=nrqrZKgl_hU",
            "Get with the program!":"https://www.youtube.com/watch?v=UlwuKEGh9So",
            "It's a book! He's going to read!":"https://www.youtube.com/watch?v=iB3EguUurXo",
            "Last one alive, lock the door!":"https://www.youtube.com/watch?v=Fvbaa610lgg",
            "Hit the showers, Frenchie.":"https://www.youtube.com/watch?v=rO8Bf2hbp18",
            "Here we go.":"https://www.youtube.com/watch?v=bfv9IkgHvxo",
            "God Bless America!":"https://www.youtube.com/watch?v=ISz1MmeqkQw",
            "You better hide, Merasmus!":"https://www.youtube.com/watch?v=R32YBooTiQM",
            "I did not have permission to die!":"https://www.youtube.com/watch?v=5MYlswxSfp8",
            "Dominated, grease monkey.":"https://www.youtube.com/watch?v=Ucrt9vhOEm8",
            "If you know what's good for ya, you will run!":"https://www.youtube.com/watch?v=c6-pK-GsTXE",
            "It's perfect!":"https://www.youtube.com/watch?v=hkHWSlksY9k",
            "You cannot burn me, I'm already on fire!":"https://www.youtube.com/watch?v=iXqGSLLC7-I",
            "I am going to claw my way down your throat and tear out your very soul!":"https://www.youtube.com/watch?v=vvplX5biR4I",
            }


# Text = print_half_soldier_list()

# text2 = print_other_half_soldier_list()

# text3 = print_last_half_soldier_list()

# print(Text)

# print(text2)

# print(text3)

# print_soldier_list()