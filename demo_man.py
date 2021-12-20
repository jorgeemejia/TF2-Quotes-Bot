import random

def get_demo_man_quote(*arg):
    keys = list(dict.keys())
    if arg:
        return(keys[arg[0]])
    else:
        return random.choice(keys)

def get_demo_man_quote_url(quote):
    return dict[quote]

# def print_demo_man_list():
#     keys = list(dict.keys())
#     for (i, item) in enumerate(keys, start = 0):
#         print(i, item)

def print_half_demo_man_list():
    num = 0
    words = ""
    keys1 = list(dict.keys())
    actual_keys = keys1[:35]
    for actual_key in actual_keys:
        word_num = str(num)
        words += '['
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

def print_other_half_demo_man_list():
    num = 35
    words = ""
    keys2 = list(dict.keys())
    actual_keys = keys2[35:]
    for actual_key in actual_keys:
        word_num = str(num)
        words += '['
        words += word_num
        words += ']'
        words += " "
        words += actual_key
        words += '\n'
        num += 1
    return words

dict = {"Yer a back-pokin' snake, and by God you'll die like one!" : "https://www.youtube.com/watch?v=jYkMJp8YUes",
        "You're weak. I'm strong. and I win, toymaker!" : "https://www.youtube.com/watch?v=gngfYEuEbFI",
        "I almost joined their bloody team!" : "https://www.youtube.com/watch?v=YfxJA-ObKsg",
        "Time to get bluttered!" : "https://www.youtube.com/watch?v=FAFnPJbebZU",
        "I hope I didn't scare you with my face-to-face man fightin!" : "https://www.youtube.com/watch?v=r9izjPinYRQ",
        "Little too much caber-tossin' pie down yer own throat, eh, chubby?" : "https://www.youtube.com/watch?v=THIDhZDbby0",
        "Wizard! Show yerself!" : "https://www.youtube.com/watch?v=02-HU11qnys",
        "He's got that book that stole me eye!" : "https://www.youtube.com/watch?v=f_N7vIl-EGo",
        "Not one of ya's going to survive this!" : "https://www.youtube.com/watch?v=E35gJNViNIY",
        "We're a sorry buncha' losers!" : "https://www.youtube.com/watch?v=dWHz3I1WcnI",
        "In your language; 'Eat lead, laddies!" : "https://www.youtube.com/watch?v=fGgnUGNYPmg",
        "You did good!" : "https://www.youtube.com/watch?v=JGluunMO-bA",
        "Hah! Barely broke a sweat!" : "https://www.youtube.com/watch?v=O9YLwyck19w",
        "FREEDOM!" : "https://www.youtube.com/watch?v=D2Ez1tAzSIw",
        "That wasn't supposed ta' happen!" : "https://www.youtube.com/watch?v=ixBfsjUNXtw",
        "Whoop de doo!" : "https://www.youtube.com/watch?v=vS2yNN1Lc_Y",
        "Aye, me bottle o' scrumpy!" : "https://www.youtube.com/watch?v=cPXQDR6o3Kg",
        "Yer a devil! A devil!" : "https://www.youtube.com/watch?v=REtGUu0YOiQ",
        "Oh, d'ye like that, yeah? Oh you like that, oh!":"https://www.youtube.com/watch?v=lQTQ6Pdlx-Q",
        "Don't fret, boyo. I'll be gentle!" :"https://www.youtube.com/watch?v=iHsb6ACn3B8",
        "Oh, that's nice.":"https://www.youtube.com/watch?v=-kcdjr3FqSM",
        "Wot magic is this?":"https://www.youtube.com/watch?v=YD6OoAAJ91Q",
        "Just bought two tickets to the gunshow, and I'm not givin' 'em...":"https://www.youtube.com/watch?v=2M_LPFGu1-A",
        "Ya' bleedin' idiots!":"https://www.youtube.com/watch?v=Hb6-FWGZg1Q",
        "Bloody hell, those ones were me favorites!":"https://www.youtube.com/watch?v=HZN-gM2mTKA",
        "Dominated! Ya wee unicorn-hatin' piece o' crap!":"https://www.youtube.com/watch?v=UAM63Ho-bqA",
        "Couldn't ya see the bloody bombs?":"https://www.youtube.com/watch?v=LQxPO0S-2BE",
        "Oh, that smarts.":"https://www.youtube.com/watch?v=Wsgn0yTZ77Q",
        "Let that be a bloody lesson to yeh!":"https://www.youtube.com/watch?v=m1fzN6GqJCg",
        "I didn't need yer help, you know.":"https://www.youtube.com/watch?v=ebNtd5Lekus",
        "Let's send that old man to Hell!!":"https://www.youtube.com/watch?v=Bv29wXfx25U",
        "That Spy's a bloody traitor!" :"https://www.youtube.com/watch?v=6Tg66Tp6Rm4",
        "What did I miss?":"https://www.youtube.com/watch?v=m73bQVa_-mY",
        "Oh, I need a drink!":"https://www.youtube.com/watch?v=d63osVaMmk4",
        "Let's finish this lads!":"https://www.youtube.com/watch?v=KTvLYTp7aS0",
        "Mediic!":"https://www.youtube.com/watch?v=XTyFJvDHBUY",
        "What's this now?":"https://www.youtube.com/watch?v=yHNb5A8_p8k",
        "Meeediiic!":"https://www.youtube.com/watch?v=0ftN_C6Go_s",
        "Medic!":"https://www.youtube.com/watch?v=8Oyrc4fachE",
        "All yah dandies prancin' aboot with ya heads full of eyeballs!":"https://www.youtube.com/watch?v=rIH0P9dqYQw",
        "Oh, they're gonna find ya all dead in the alley, with cats lickin' at ya!":"https://www.youtube.com/watch?v=HXoMNt_Fvco",
        "Ohhh... there's a new gravy-filled angel in heaven.":"https://www.youtube.com/watch?v=QbbaM-34efs",
        "Unicorn brothers! Tonight, we pony prance in HELL!":"https://www.youtube.com/watch?v=3HtrnpVsMck",
        "Oh what's your name ya pretty lit'le thing!":"https://www.youtube.com/watch?v=iP48WYM0ZW0",
        "You've brought shame on yer people, ya mumblin' devil.":"https://www.youtube.com/watch?v=v86HHXm3IlU",
        "Ohh, I'm gonna beat ya so hard, you'll have a twitch!":"https://www.youtube.com/watch?v=ZSPcLvOarzY",
        "Nah." :"https://www.youtube.com/watch?v=oBiI8ZW3Bio",
        "Go home, lassie; men are fightin' here!" :"https://www.youtube.com/watch?v=QDu63-YnEsM",
        "Next time you'll bloody ask before you stand on my point.":"https://www.youtube.com/watch?v=h86w6bpvXk4",
        "I'm goin' ta blast ya into thin gruel!":"https://www.youtube.com/watch?v=aa8tMyY7TvA",
        "You come wide at me again, boy, I'll stick that wrench right up yer arse!":"https://www.youtube.com/watch?v=DhcbiSdZDMs",
        "Keep it up, lads!":"https://www.youtube.com/watch?v=WEPzrMVN1rc",
        "You appear to have trodden on a mine!":"https://www.youtube.com/watch?v=2j05Nk2Ziuk",
        "And that's what yeh get for touching that!" :"https://www.youtube.com/watch?v=vhtaBG-ToUk",
        "How's that feel, ya blockhead?" :"https://www.youtube.com/watch?v=4jqOhvxWnpY",
        "I had me good eye on you the whole time!" :"https://www.youtube.com/watch?v=hhzhYi6CVfo",
        "It's on! It's on like [falls asleep, then wakes up] wha--?":"https://www.youtube.com/watch?v=wt27LhlDdFk",
        "Ahhh! Me head! It's wee. It's a wee head...":"https://www.youtube.com/watch?v=wEm289T86Oo",
        "Pbbbbt! Ergh!":"https://www.youtube.com/watch?v=oEPDEdPd6mA",
        "Lads! Get to the cart!":"https://www.youtube.com/watch?v=RNsutN9lPzE",
        "Wuhbluhbluhbluh!":"https://www.youtube.com/watch?v=JcTbfh_e5OA",
        "Now it's our flippin' point, hehah!":"https://www.youtube.com/watch?v=Cyq4xdLKfRg",
        'Time to pull ahead, boys!':"https://www.youtube.com/watch?v=tsU1w02AaPI",
        "They're goin' ta bury what's left of ye in a soup can!":"https://www.youtube.com/watch?v=FVpnhWE65QY",
        "Ooooh, I've reeallly hit rock bottom.":"https://www.youtube.com/watch?v=7w1r9BI7RZw",
        'This team needs all Demomen!':"https://www.youtube.com/watch?v=WPCwON1SV-w",
        "Oh, they're goin' ta have to glue you back together...IN HELL!":"https://www.youtube.com/watch?v=74YMEipVUmk",
        'Ya great lactating wet nurse!':"https://www.youtube.com/watch?v=rjKRiy4McOA",
        'Dominated you tutonic nurse maid *belch*' :"https://www.youtube.com/watch?v=svic3RvABAs",
        "Go to hell, and tell the devil I'm comin' for him next!":"https://www.youtube.com/watch?v=drfAs-QGxb4",
        'Oh, I need a drink!':"https://www.youtube.com/watch?v=ioVeDMUdXiM",
        "Yer so bloody TINY! Yer like a toy-sized version of a man!":"https://www.youtube.com/watch?v=5zmNNnRtzt4",
        'There can be only one!':"https://www.youtube.com/watch?v=JFTZqin0SqE",
        'See.':"https://www.youtube.com/watch?v=l-HRhYrucdU",
        'Ka-Boom!':"https://www.youtube.com/watch?v=WxjGZo8oN5Y"
        }


# list1 = print_half_demo_man_list()
# print(list1)

# list2 = print_other_half_demo_man_list()
# print(list2)

# print(get_demo_man_quote(1))

# quote = get_demo_man_quote()
# print(quote)