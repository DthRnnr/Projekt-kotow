from models.ObiektDynamiczny import ObiektDynamiczny

class Mysz(ObiektDynamiczny):

    def __init__(self, szybkosc, zasieglapek, wzrok, plodnosc, raniony, przestraszenie, jedzenie, przenoszenie, id, dead):
        super().__init__(szybkosc, wzrok, plodnosc, raniony, przestraszenie, id, dead)