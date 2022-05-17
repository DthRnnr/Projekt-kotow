class ObiektDynamiczny:

    ObiektDynamicznylist = []

    def __init__(self, szybkosc, zasieglapek, wzrok, plodnosc, raniony, przestraszenie, jedzenie, przenoszenie, id, dead):
        self.id = len(self.ObiektDynamicznylist)
        self.szybkosc = szybkosc
        self.zasieglapek = zasieglapek
        self.wzrok = wzrok
        self.plodnosc = plodnosc
        self.raniony = raniony
        self.przestaszenie = przestraszenie
        self.jedzenie = jedzenie
        self.przenoszenie = przenoszenie
        self.dead