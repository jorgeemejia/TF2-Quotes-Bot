import random

def get_engineer_quote():
    keys = list(engineer_dict.keys())
    return random.choice(keys)

def get_engineer_quote_url(quote):
    return engineer_dict[quote]

engineer_dict = {"You are a coward and a scoundrel!" : "https://www.youtube.com/watch?v=wO9Ch3AHwRs",
            "Not bad. Not bad at all.": "https://www.youtube.com/watch?v=wBtKmgHWt64",
            "Whoo, look at all that money." : "https://www.youtube.com/watch?v=4RkX_-0-eRs",
            "Job well done." : "https://www.youtube.com/watch?v=WTse28OS3qA",
            "Dispenser going up." : "https://www.youtube.com/watch?v=AuhqE20xdNI",
            "I'm a killer of men, doc. That is the God's-honest truth." : "https://www.youtube.com/watch?v=yYZwQxX5f9k",
            "Doctor! I am the better man!" : "https://www.youtube.com/watch?v=Ibs21vdwEcM",
            "You are a whole herd'a ugly." : "https://www.youtube.com/watch?v=tHZjqHDqOG8",
            "And another thing: you're ugly." : "https://www.youtube.com/watch?v=wKbWW0WTh0k"
            }