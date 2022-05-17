from models.ObiektDynamiczny import ObiektDynamiczny

class Hycel(ObiektDynamiczny):
    
    def __init__(self, id, plodnosc, raniony, przestraszenie, jedzenie, dead, przenoszenie, szybkosc=3, zasieglapek=2, wzrok=10, ):
        super().__init__(id, szybkosc, zasieglapek, wzrok, przenoszenie)