from p_klass import *

fil = "personer.txt"

######################## FILHANTERING ######################################

def las_fil(): # laser filen
    plista = []
    pfil = open(fil, "r")
    rader = pfil.read().splitlines() # returnerar en lista
    pfil.close

    for i in range(0, len(rader), 4): # skapar ojbekt 
        enamn = rader[i]
        fnamn = rader[i+1]
        telenr = rader[i+2]
        adress = rader[i+3]
        person = Person(enamn, fnamn, telenr, adress) # ankallar  klassen
        plista.append(person)
    return plista

def spara_fil(lista): # skriver och sparar aktuell information 
    pfil = open(fil, "w")
    for person in lista:
        rad = "{}\n{}\n{}\n{}\n".format(person.enamn, person.fnamn, person.telenr, person.adress)
        pfil.write(rad)
    pfil.close 

########################## MENYER ##########################################

def huvud_meny():
    print("\n========================= HUVUDMENYN =========================")
    print("{}\n{}\n{}\n{}\n{}\n{}\n{}".format("1. Sok med namn", "2. Sok med telefonnummer", "3. Skriv ut telefonregister", "4. Lagg till en person", "5. Ta bort en person", "6. Avsluta", "Behover du hjalp, mata '?'"))
    print("==============================================================")

def meny():
    print("{}\n{}\n{}".format("1. Andra telefonnummer", "2. Andra adress", "3. Tillbaka till HUVUDMENYN"))

######################## FELHANTERING ######################################

def input_enamn(): # 3
    while True:
        en = input("Mata in efternamnet:")
        if en.strip().isalpha():
            return en.strip().lower()
        else:
            print("Mata enbart in bokstaver!")

def input_fnamn():
    while True:
        fn = input("Mata in fornamnet:")
        if fn.strip().isalpha():
            return fn.strip().lower()
        else:
            print("Mata enbart in bokstaver!")

def input_telenr(): # 2
    while True:
        nr = input("Mata in telefonnumret:")
        if nr.strip().isdigit() and len(nr) == 6:
            return nr
        else:
            print("Mata in 6 siffror!")

def input_val(): # 2
    while True: 
        val = input("\nValj ett av valen ovan:")
        if val.strip().isdigit() and int(val) <= 6:
            return int(val)
        elif val == '?':
            print("\n========================== HJALP =============================")
            print("{}\n{}\n{}".format("Mata in siffran for det alternativ du vill valja.","Anvand endast siffror.","Inmatning avslutas med enter."))
            print("==============================================================")
            return False
        else:
            print("Mata enbart in en siffra som finns ovan!")

def input_adress(): # 1
    while True:
        nyadress = input("Mata in adressens gatunamn:")
        nynr = input("Mata in adressens gatunummer:")
        if nyadress.strip().isalpha() and nynr.isdigit():
            return nyadress.strip().title()+","+str(nynr)
        else:
            print("Nagot gick fel, kontrollera att gatunamnet enbart innehaller bokstaver och gatunumret enbart  siffror!")
            
######################### FORANDRAR ########################################

def sok_namn(lista):
    plista = [] # lista med personer med samma efternamn
    enamn = input_enamn() # felhantering
    fnamn = input_fnamn()
    for i in lista: # gar igenom hela listan for att hitta matchningar  
        if i.enamn.lower() == enamn and i.fnamn.lower() == fnamn:
            plista.append(i)
    if len(plista) > 1: # flera matchningar
        i = valj_person(plista)
        return i
    elif len(plista) == 1: # en matchning
        person_info(plista[0])
        return plista[0]
    else: # ingen matchning 
        print("Det finns ingen vid namnet '"+fnamn,enamn+"' i telefonregistret!")
        return None
            
def valj_person(plista): # om flera matchningar  
    print("Det finns flera personer med samma efternamn!\n")
    print_telreg(plista) 
    val = input_val() # felhantering
    person_info(plista[val-1])
    return plista[val-1]

def sok_telenr(lista):
    telenr = input_telenr() # felhantering
    ejhittad = True # manniskor kan ej ha samma nr
    for i in lista:
        if i.telenr == telenr:
            person_info(i)
            return i
            ejhittad = False
    if ejhittad == True:
        print("Det finns ingen med numret '"+str(telenr)+"' i telefonregistret!")
        return None

def person_info(i):
    print("\n{}\n{}\n{}\n{}\n".format("EFTERNAMN: "+i.enamn, "FORNAMN: "+i.fnamn, "TELEFONNUMMER: "+i.telenr, "ADRESS: "+i.adress))

def andra_telenr(lista, i):
    nyttnr = kolla_nr(lista)
    i.byta_nr(nyttnr)
    print("Uppgifterna har nu uppdaterats till:")
    person_info(i)
            
def kolla_nr(lista):
    while True: # loopas till anvandaren matat in ett nr som inte redan existerar 
        nyttnr = input_telenr()
        ejsamma = True
        for p in lista:
            if p.telenr == nyttnr:
                print("Telefonnumret existerar redan, valj ett annat!")
                ejsamma = False
        if ejsamma == True:
            return nyttnr
        
def andra_adress(i):
    nyadress = input_adress()
    i.byta_adress(str(nyadress))
    print("Uppgifterna har nu uppdaterats till:")
    person_info(i)

def print_telreg(lista): # skriver ut registret
    print("EFTERNAMN".ljust(15)+"FORNAMN".ljust(15)+"TELEFONNUMMER".ljust(15)+"ADRESS".ljust(15))
    print("===============================================================")
    c = 1
    for i in lista:
        print(str(c)+".",end="")
        print(i)
        c += 1 # problem med formatering nar det blir storre tal

def lagg_till(lista):
    en = input_enamn()
    fn = input_fnamn()
    nr = kolla_nr(lista) # kollar sa att ett nr inte redan existerar 
    ad = input_adress()
    nyperson = Person(en.title(), fn.title(), nr, ad)
    print("\nDen nya personen...")
    person_info(nyperson)
    print("... har nu lagts till i telefonregistret!")
    lista.append(nyperson)

def ta_bort(lista):
    i = sok_namn(lista)
    if i != None:
        while True:
            svar = input("Ar du saker pa att du vill ta bort denna person? j/n:")
            if svar.isalpha():
                if svar.lower() == 'j':
                    print("Vald person har nu tagits bort fran telefonregistret!")
                    return lista.remove(i)
                elif svar.lower() == 'n':
                    return False
                else:
                    print("Mata 'j' for 'ja', 'n' for 'nej'")
            else:
                print("Mata enbart in bokstaver!")

########################### MAIN ################################################

def main():
    print("************** VALKOMMEN TILL TELEFONREGISTRET ***************")
    lista = las_fil()
    while True:
        huvud_meny()
        val = input_val()
        
        if val >= 1 and val <= 2:
            if val == 1:
                sokt_person = sok_namn(lista)
            elif val ==2:
                sokt_person = sok_telenr(lista)
            if sokt_person == None:
                pass
            else:
                ejhm = True
                while ejhm == True:
                    meny()
                    val2 = input_val()
                    if val2 == 1:
                        andra_telenr(lista, sokt_person)
                    elif val2 == 2:
                        andra_adress(sokt_person)
                    elif val2 == 3:
                        ejhm = False
                    else:
                        print("Mata enbart en siffra som finns ovan!\n")
                    
        elif val >= 3 and val <= 6:
            if val == 3:
                print_telreg(lista)
            elif val == 4:
                lagg_till(lista)
            elif val == 5:
                ta_bort(lista)
            elif val == 6:
                print("\n***************** TELEFONREGISTRET AVSLUTAS ******************")
                return False
            
        spara_fil(lista) 
    
main() # anropar huvudfunktionen som startar programmet
