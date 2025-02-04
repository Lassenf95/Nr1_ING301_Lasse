from pathlib import Path
import sys
#import filter
import collections
#

def read_file(file_name):
    """
    Denne funksjonen får et filnavn som argument og skal gi
    tilbake en liste av tekststrenger som representerer linjene i filen.
    """
    # Tips: kanksje "open"-funksjonen kunne være nyttig her: https://docs.python.org/3/library/functions.html#open
    filenSomLeses = open(file_name, encoding="utf-8")     
    innholdIFilen = filenSomLeses.read()
    innholdSomLinjer = innholdIFilen.split("\n")
    innholdBareLinjerMedOrd = list(filter(None, innholdSomLinjer)) #fjenrer alle tomme linjer
    filenSomLeses.close()
    return innholdBareLinjerMedOrd




def lines_to_words(lines):
#      """
#     Denne funksjonen får en liste med strenger som input (dvs. linjene av tekstfilen som har nettopp blitt lest inn)
#     og deler linjene opp i enkelte ord. Enhver linje blir delt opp der det er blanktegn (= whitespaces).
#     Desto videre er vi bare interessert i faktiske ord, dvs. alle punktum (.), kolon (:), semikolon (;),
#     kommaer (,), spørsmåls- (?) og utråbstegn (!) skal fjernes underveis.
#     Til sist skal alle ord i den resulterende listen være skrevet i små bokstav slik at "Odin" og "odin"
#     blir behandlet likt.
#     OBS! Pass også på at du ikke legger til tomme ord (dvs. "" eller '' skal ikke være med) i resultatlisten!

#     F. eks: Inn: ["Det er", "bare", "noen få ord"], Ut: ["Det", "er", "bare", "noen", "få", "ord"]
#     """
#     # 
    
    EnStorString= '' #VIKTIG AT DENNE ER TOM; BYGGES BARE VIDERE PÅ
    #bygger opp hele stringen før splitting og rensing , merk mellomrom legges slik at blir en lang setning
    for alleLinjer in lines:  
        EnStorString += alleLinjer +' ' 
    
    TEGN_JEG_VIL_FJERNE = ['-','-',',',';','!','?',':','.'] #RENSETIS
   
    #erstatter alle tegn og erstatter de med ingenting
    for hvertElement in TEGN_JEG_VIL_FJERNE: 
        EnStorString = EnStorString.replace(hvertElement,'')  
    
    #får alt i lower case
    EnStorString = EnStorString.lower() #Overskriver stringen med en ny string der alt ewr lite
   
    #gjør om til liste igjen. splitter alt med mellomrom mellom seg
    Resultatet = EnStorString.split()
    return Resultatet

    

def compute_frequency(words):
    
    """
    Denne funksjonen tar inn en liste med ord og så lager den en frekvenstabell ut av den. En frekvenstabell
    teller hvor ofte hvert ord dykket opp i den opprinnelige input listen. Frekvenstabllen
    blir realisert gjennom Python dictionaires: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

    F. eks. Inn ["hun", "hen", "han", "hen"], Ut: {"hen": 2, "hun": 1, "han": 1}
    """
    #lager en tom dict. Mater alle ordene inn. Lagger til et tilfellet hver gang ordet oppstår på nytt
    Ordbok = {} #MANGE MÅTER
    for word in words[:]:
        Ordbok[word] = Ordbok.get(word, 0) +1
     
    return Ordbok

FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han', 'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']


def remove_filler_words(frequency_table):
    """
    Ofte inneholder tekst koblingsord som "og", "eller", "jeg", "da". Disse er ikke så spennende når man vil
    analysere innholdet til en tekst. Derfor vil vi gjerne fjerne dem fra vår frekvenstabell.
    Vi har gitt deg en liste med slike koblingsord i variablen FILL_WORDS ovenfor.
    Målet med denne funksjonen er at den skal få en frekvenstabll som input og så fjerne alle fyll-ord
    som finnes i FILL_WORDS.
    """
    
    #sjekker hvert ord i dicten. Sletter hvert ord i tabellene som er av et ord som inngår i FILL_WORDS
    for key in FILL_WORDS:
        frequency_table.pop(key, None)
    
    return frequency_table  # TODO: Du må erstatte denne linjen

def largest_pair(par_1, par_2):
    #  """
    # Denne funksjonen får som input to tupler/par (https://docs.python.org/3/library/stdtypes.html#tuple) der den
    # første komponenten er en string (et ord) og den andre komponenten er en integer (heltall).
    # Denne funksjonen skal sammenligne heltalls-komponenten i begge par og så gi tilbake det paret der
    # tallet er størst.
    # """
    # # OBS: Tenk også på situasjonen når to tall er lik! Vurder hvordan du vil handtere denne situasjonen
    # kanskje du vil skrive noen flere test metoder ?!
    
    #definer en ny tuple med ukjent innhpød
    BiggestTuple = ()
    
    
    if par_1[1] > par_2[1]:  
        # print('Par1 er størt med verdien ' + str(par_1[1]))
        BiggestTuple = par_1
    elif par_1[1] < par_2[1]: 
        # print('Par2 er størt med verdien ' + str(par_2[1]))
        BiggestTuple = par_2
    else: 
        # print('Like store')
        return None #verdiene er like stor. Gir beskjed om at de ikke kan sammenlignes.
    
    '''#SE UNDER TEST-PROGRAM
        #Tester at først at testen finner største paret... Dersom world,5 finnes i listen av par1 og par2, 
        # så retunerer testen bare None fordi de er like. Da er det OK. Testen returerer riktig TUPLER.
        resultT1 = self.assertEqual(("World", 5), wf.largest_pair(('Hallo', 3), ("World", 5)))
        print('Test for ulike verdier', 'Bestått' if resultT1 is None else "Feilet")
        #Nå skal jeg se at resten returnerer None dersom jeg tester 2 ord med like mange forekomster
        resultT2 = self.assertEqual(None, wf.largest_pair(('Hallo', 5), ("World", 5)))
        print('Test for like verdier', 'Bestått' if resultT2 is None else "Feilet")
    '''  
    #Hvis en av testene gir at par 1 eller par 2 er størst så returneres par, ellers NONE
    return BiggestTuple  # TODO: Du må erstatte denne linjen HV


def find_most_frequent(frequency_table):
    """
    Nå er det på tide å sette sammen alle bitene du har laget.
    Den funksjonen får frekvenstabllen som innputt og finner det ordet som dykket opp flest.
    """
    #FORSØK TO... Tar inn alle verdiene. Sjekker så alle forekomster av hvert ord. Når et nyttOrd har forekomt flest
    #ganger hittil, så lagres indeksen for dette ordet. Til slutt så hentes ordet som forkommer mest ut med indeksen som er funnet.

    AntallGangerAvORDET = -1 #setter en verdi av ordet. Vet at -1 0 osv ikke er brukt siden alle vil jo ha min 1 forkomest
    ORDETSomErMestAv= 'ordet'
    IndexPlasseringTilORDET=-1
    for index, (ordet, antall) in enumerate(frequency_table.items()):
        #sjekker om ordet jeg finner har større forekomster
        if antall > AntallGangerAvORDET:
            AntallGangerAvORDET = antall
            ORDETSomErMestAv = ordet
            IndexPlasseringTilORDET=index
            
    # print('ordet med flest forekomster er  '+ ORDETSomErMestAv + 'med ' + str(AntallGangerAvORDET) +' forkomster')
    # print('Ble funnet på index' + str(IndexPlasseringTilORDET) + 'i tabellen ')        

    return ORDETSomErMestAv
    
    #
    # Tips: se på "dict.items()" funksjonen (https://docs.python.org/3/library/stdtypes.html#dict.items)
    # og kanskje du kan gjenbruke den "largest_pair" metoden som du nettopp har laget
    #return NotImplemented  # TODO: Du må erstatte denne linjen


############################################################
#                                                          #
# Her slutter dendelen av filen som er relevant for deg ;-)#
#                                                          #
############################################################


def main():
    if len(sys.argv) > 1 and Path(sys.argv[1]).exists():
        file = sys.argv[1]
    else:
        file = str(Path(__file__).parent.absolute()) + "/voluspaa.txt"
    lines = read_file(file)
    words = lines_to_words(lines)
    table = compute_frequency(words)
    table = remove_filler_words(table) 
    most_frequent = find_most_frequent(table)
    print(f"The most frequent word in {file} is '{most_frequent}'")

    
if __name__ == '__main__':
    main()
