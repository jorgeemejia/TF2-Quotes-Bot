import random

def get_soldier_quote():
    keys = list(soldier_dict.keys())
    return random.choice(keys)

def get_soldier_quote_url(quote):
    return soldier_dict[quote]


soldier_dict = {'A big mug of my foot up your ass!': "https://www.youtube.com/watch?v=fwyQl_YUwnc",
            "Thanks, soldier." : "https://www.youtube.com/watch?v=6Hj5rC4snqw",
            "You were loud and ugly and now you're DEAD! Amen." : "https://www.youtube.com/watch?v=eKbcTbQIMqc",
            "You were good son, real good; maybe even the best." : "https://www.youtube.com/watch?v=jaQnQ17s4AQ",
            "Hooah!" : "https://www.youtube.com/watch?v=-U1mlDNSOSw",
            "This is my world. You are not welcome in my world." : "https://www.youtube.com/watch?v=2DT2uhpm7nU",
            "Screamin' Eagles!" : "https://www.youtube.com/watch?v=V7YBuu-KxgU",
            "Forward!" : "https://www.youtube.com/watch?v=Pqrm2eYX55w",
            "You will not be missed." : "https://www.youtube.com/watch?v=7gYIzcUxlSQ"
            }