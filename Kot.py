from models.ObiektDynamiczny import ObiektDynamiczny

import random


class Kot(ObiektDynamiczny):

    def __init__(self, szybkosc, zasieglapek, wzrok, plodnosc, raniony, przestraszenie, jedzenie, przenoszenie, dead):
        super().__init__(id, szybkosc, zasieglapek, wzrok, plodnosc, przestraszenie, jedzenie, dead)
        self.szybkosc = random.randint(2,6)
