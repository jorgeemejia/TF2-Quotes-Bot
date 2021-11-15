import random


def get_heavy_quote():
    keys = list(heavy_dict.keys())
    return random.choice(keys)

def get_heavy_quote_url(quote):
    return heavy_dict[quote]

heavy_dict = {"Get behind me doctor!" : "https://www.youtube.com/watch?v=7duMsdAtrO8",
         "Little little man." : "https://www.youtube.com/watch?v=MG3v3_ahd3Q",
         "Do you remember me now?!": "https://www.youtube.com/watch?v=B_eX15hz_Is",
         "I am angry!" : "https://www.youtube.com/watch?v=UNEubxOT-5E",
         "Ha ha ha ha! Heavy is back babies!" : "https://www.youtube.com/watch?v=8ILFT198-WY",
         "Who. Touched. My. Gun." : "https://www.youtube.com/watch?v=ATtE-deTW2s",
         "Get behind pretty pink pony mane, Doctor!" : "https://www.youtube.com/watch?v=b7qanrgwbd4",
         "Run, cowards! Tweet tweet tweeeet!" : "https://www.youtube.com/watch?v=530I7ZPc6CE",
         "Shh... Sasha is asleep." : "https://www.youtube.com/watch?v=jQV0e4AJtn4"
        }

