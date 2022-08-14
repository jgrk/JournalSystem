from textredigerare import *
class User:
    def __init__(self, namn, persnr, mail, losen, journal):
        self.namn = namn #förnamn str
        self.persnr = persnr #personnummer str
        self.mail = mail #email str
        self.losen = losen #lösen str
        self.journal = journal #txt str

    def open_journal(self):
        redigerare()
    
    def inlogg(self):
        persnr = input("Personnummer: ")
        losen = input("Lösenord: ")
        return self.persnr == persnr and self.losen == losen

    def ändra_uppgifter():
        pass






        
        



        