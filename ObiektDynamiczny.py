from models.obiekt import obiekt

class ObiektDynamiczny:

    ObiektDynamicznylist = []

    def __init__(self, szybkosc, zasieglapek, wzrok, raniony, przestraszenie):
        
        self.id = len(self.ObiektDynamicznylist)
        self.szybkosc = szybkosc
        self.zasieglapek = zasieglapek
        self.wzrok = wzrok
        self.raniony = raniony
        self.przestaszenie = przestraszenie