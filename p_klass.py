class Person():

    # Konstruktorn for att skapa objekt
    def __init__(self, enamn, fnamn, telenr, adress):
        self.enamn = enamn
        self.fnamn = fnamn
        self.telenr = telenr
        self.adress = adress

    def byta_nr(self, nyttnr):
        self.telenr = nyttnr

    def byta_adress(self, nyadress):
        self.adress = nyadress
        
    # Strangmetod for att kunna skriva ut objekten 
    def __str__(self): 
        return self.enamn.ljust(13)+self.fnamn.ljust(15)+self.telenr.ljust(15)+self.adress.ljust(15)

    # Jamforelsemetod for att kunna sortera objekten 
    def __cmp__(self, other): 
    # sorterar efter efternamn 
        if self.enamn < other.enamn: # om other ar storre returneras -1
            print("hej")
            return -1 
        elif self.enamn > other.enamn: # om other ar mindre returneras 1
            return 1 
        else: 
            # om efternamn ar lika, sorteras efter fornamn 
            if self.fnamn < other.fnamn: 
                return -1 
            elif self.fnamn > other.fnamn: 
                return 1 
            else: 
            # om for- och efternamn ar lika, sorteras efter adress 
                if self.adress < other.adress: 
                    return -1 
                elif self.adress > other.adress: 
                    return 1 
                else: 
                    if self.adress < other.adress: 
                        return -1 
                    elif self.adress > other.adress: 
                        return 1 
                    else: 
                        return 0
