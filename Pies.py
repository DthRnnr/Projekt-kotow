from ObiektDynamiczny import ObiektDynamiczny

class Pies(ObiektDynamiczny):

    def __init__(self, szybkosc, zasieglapek, wzrok, plodnosc, raniony, przestraszenie, jedzenie, przenoszenie, id, dead):
        super().__init__(szybkosc, zasieglapek, wzrok, id)