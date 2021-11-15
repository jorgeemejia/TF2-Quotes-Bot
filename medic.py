import random

def get_medic_quote():
    keys = list(medic_dict.keys())
    return random.choice(keys)

def get_medic_quote_url(quote):
    return medic_dict[quote]

medic_dict = {"Ze healing is not as revarding as ze hurting." : "https://www.youtube.com/watch?v=EGmHVNLDxFw",
         "Zat vas doktor-assisted homicide!" : "https://www.youtube.com/watch?v=L-BctkSZLJ8",
         "Eins, zwei, drei... Ugh, I do not think ve brought enough body bags." : "https://www.youtube.com/watch?v=wYkIrbNuZ3A", 
         "I can't take any more of zis insanity!": "https://www.youtube.com/watch?v=0DJHFIRAqgI",
         "Zhe Überbot is destroyed." : "https://www.youtube.com/watch?v=oVMLKxpE5Aw",
         "Get zem. Raus, Raus!" : "https://www.youtube.com/watch?v=Hb9xzsYMC7o",
         "Haha! Vat a bloodbath!" : "https://www.youtube.com/watch?v=oYTbsWXbXMs",
         "Ooh, much better." : "https://www.youtube.com/watch?v=peM9uEcPM00",
         "Anuhza successful procedure!" : "https://www.youtube.com/watch?v=J96syviggBQ"
        }