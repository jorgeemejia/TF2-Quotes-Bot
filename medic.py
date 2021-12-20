import random

def get_medic_quote(*arg):
    keys = list(dict.keys())
    if arg:
        return(keys[arg[0]])
    else:
        return random.choice(keys)

def get_medic_quote_url(quote):
    return dict[quote]

# def print_medic_list():
#     keys = list(dict.keys())
#     for (i, item) in enumerate(keys, start = 0):
#         print(i, item)

def print_medic_list():
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

dict = {"Ze healing is not as revarding as ze hurting." : "https://www.youtube.com/watch?v=EGmHVNLDxFw",
         "Zat vas doktor-assisted homicide!" : "https://www.youtube.com/watch?v=L-BctkSZLJ8",
         "Eins, zwei, drei... Ugh, I do not think ve brought enough body bags." : "https://www.youtube.com/watch?v=wYkIrbNuZ3A", 
         "I can't take any more of zis insanity!": "https://www.youtube.com/watch?v=0DJHFIRAqgI",
         "Zhe Überbot is destroyed." : "https://www.youtube.com/watch?v=oVMLKxpE5Aw",
         "Get zem. Raus, Raus!" : "https://www.youtube.com/watch?v=Hb9xzsYMC7o",
         "Haha! Vat a bloodbath!" : "https://www.youtube.com/watch?v=oYTbsWXbXMs",
         "Ooh, much better." : "https://www.youtube.com/watch?v=peM9uEcPM00",
         "Anuhza successful procedure!" : "https://www.youtube.com/watch?v=J96syviggBQ",
         "Ve did it, Kamerad!":"https://www.youtube.com/watch?v=7e9esIc_wCE",
         "Hoo, hoo! Astounding!":"https://www.youtube.com/watch?v=wCo2SXSpisA",
         "Oops! Zat vas not Medizin!":"https://www.youtube.com/watch?v=d1SHf2K02zA",
         "Free money ! Free money!":"https://www.youtube.com/watch?v=f00_zJhfg9s",
         "You vill go no furzher!" :"https://www.youtube.com/watch?v=mJ-IJCZILYQ",
         "Achtung! Spy!":"https://www.youtube.com/watch?v=plHsg5R0EVY",
         "Zis... is unacceptable!":"https://www.youtube.com/watch?v=E2orBWdptss",
         "Ze Engineer is a Spy!":"https://www.youtube.com/watch?v=RJJdz9cO2LY",
         "Velcome to the 've lose vonce again'-fest.":"https://www.youtube.com/watch?v=KFA1oGjLdcY",
         "Medic!":"https://www.youtube.com/watch?v=8mJk77EMBtU",
         "Ooh. I must learn how to do zhat.":"https://www.youtube.com/watch?v=0lzO1sswbWk",
         "Doktor!":"https://www.youtube.com/watch?v=l9nxG21NrYE",
         "MEEEDIIIC!" :"https://www.youtube.com/watch?v=bv3Vpi6MoA8",
         "Can you feel ze Schadenfreude?":"https://www.youtube.com/watch?v=oKrC8EH6l_Q",
         "You are... schtupid!" :"https://www.youtube.com/watch?v=l5V4G6uPMiU",
         "Sturm und Drang!" :"https://www.youtube.com/watch?v=3F8Y5pKcu50",
         "Would you like a second opinion? You are also ugly!":"https://www.youtube.com/watch?v=DCNTCFSyGcA",
         "Puuuush!":"https://www.youtube.com/watch?v=AqKqLO1JTAM",
         "All I can tell you about zis next procedure is zat it vill be... excruciating!":"https://www.youtube.com/watch?v=3NWntF9VRkw",
         "Ooh. Interesting.":"https://www.youtube.com/watch?v=fMpbat_50fc",
         "Wuh ho ho! Vhat a curious sensation!":"https://www.youtube.com/watch?v=pHJcW3U8_4s",
         "I can't take it any more!":"https://www.youtube.com/watch?v=EQWbEsS4tgQ",
         "I am melting!" :"https://www.youtube.com/watch?v=ywRyQNocjp4",
         "Raus, Raus!":"https://www.youtube.com/watch?v=F_oUr-SsHJU",
         "You are trying my patience!":"https://www.youtube.com/watch?v=flVn1yX38bI",
         "Papers, please.":"https://www.youtube.com/watch?v=c_cGRLB24Uw",
         "Everyvun! Freee money!":"https://www.youtube.com/watch?v=ThOTb2UmMVo",
         "I am zhe angry bird god of zhe Badlands! Fear me!":"https://www.youtube.com/watch?v=B9yKoFwsFC4",
         "Everyone, we must stop zhat bomb!":"https://www.youtube.com/watch?v=oBrYwkqEMUc",
         "Ooh, money!" :"https://www.youtube.com/watch?v=JgUDzgwIspU",
         "So many bombs!" :"https://www.youtube.com/watch?v=ruwHlcqlziE",
         "I'm going to saw through your bones!":"https://www.youtube.com/watch?v=EYTuSTjttGg",
         "Good shooting!":"https://www.youtube.com/watch?v=NRkYjSDVX-A",
         "Come out, Merasmus! Nothing vill happen to you. I svear...":"https://www.youtube.com/watch?v=6hmQCgl7i7k",
         "I toiled in God's domain!" :"https://www.youtube.com/watch?v=VgGv2cfW4uk"
        }