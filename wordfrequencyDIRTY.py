from pathlib import Path
import sys
#import filter
import collections
#

def read_file(file_name):
    # """
    # Denne funksjonen får et filnavn som argument og gir
    # tilbake en liste av tekststrenger som representerer linjene i filen.
    # """
    # #får feilmelding på at python ikke kan lese det. formatet på filen er cp1252, konverter til utf-8.
    # filenSomLeses = open(file_name)
    filenSomLeses = open(file_name, encoding="utf-8")     
    innholdIFilen = filenSomLeses.read()
    #innholdIFilen = innholdIFilen.split('')
    innholdSomLinjer = innholdIFilen.split("\n")
    # itere=0
    # for linjer in innholdSomLinjer[:]:
    #     print(innholdSomLinjer[itere])
    #     itere = itere + 1
    #ser at teksten inneholder tomme linjer også. Disse må slettes.
    innholdBareVerdier = list(filter(None, innholdSomLinjer))
    
    # itere=0
    # for linjer in innholdBareVerdier[:]:
    #     print(innholdBareVerdier[itere])
    #     itere = itere + 1     
        
        
    #ALTERNATIV ENDA KORTET 
    #with open(file_name, encoding="utf-8") as filenSomLeses:
     #  innholdSomLinjer =  file_name.read().splitlines()
    
    #with open(file_name, encoding='utf-8') as fil:
     #   innholdSomLinjer = [linje for linje in fil.read().splitlines() if linje]  
    
    # resultat = []
    # for linje in innholdSomLinjer[1:]:
    #     # result.append(Point(linje))
    #     resultat += linje #like funksjoner
    filenSomLeses.close()
    return innholdBareVerdier




def lines_to_words(lines): 
    EnStorString=''
    for alleLinjer in lines:   #bygger opp hele stringen før splitting og rensing , merk mellomrom legges slik at blir en lang setning
        EnStorString += alleLinjer +' ' 
    #print(EnStorString)
    #print(EnStorString)
    TEGN_JEG_VIL_FJERNE = ['-','-',',',';','!','?',':','.'] #RENSETIS
   
    for hvertElement in TEGN_JEG_VIL_FJERNE: 
        EnStorString = EnStorString.replace(hvertElement,'')  #erstatter alle tegn og erstatter de med ingenting
    #print(EnStorString)
    
    #får alt i lower case
    EnStorString = EnStorString.lower() #Overskriver stringen med en ny string der alt ewr lite
    #print(EnStorString)
    #gjør om til liste igjen. splitter alt med mellomrom mellom seg
    #print(EnStorString)
    Resultatet = EnStorString.split()
    return Resultatet

    

def compute_frequency(words):
    
    """
    Denne funksjonen tar inn en liste med ord og så lager den en frekvenstabell ut av den. En frekvenstabell
    teller hvor ofte hvert ord dykket opp i den opprinnelige input listen. Frekvenstabllen
    blir realisert gjennom Python dictionaires: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

    F. eks. Inn ["hun", "hen", "han", "hen"], Ut: {"hen": 2, "hun": 1, "han": 1}
    """
    ##LASSE LINJER START
    
    #Ordbok = {}
    #bruker collections sin tellefunksjon som teller antall forekomseter av ord i en lsitet sortet-
    #OrdForekomst = collections.Counter(words)
    Ordbok = {} #MANGE MÅTER
    for word in words[:]:
        Ordbok[word] = Ordbok.get(word, 0) +1
    #sorter
    #SortertOrdbok = dict(sorted(Ordbok.items(), key=lambda item: item[1]))
    #print(type(Ordbok))
    #SortertOrdbok =/=
    #SortertOrdbok=sorted(Ordbok.keys()) #[:]
    #print(Ordbok)
    #sorted(frequency_table.keys())
   # print(SortertOrdbok)
     
    return Ordbok #senter ut resultatet 
   # OrdForekomst = compute_frequency(words.split())
    #print(OrdForekomst)
    #print(type(OrdForekomst))
    #return OrdForekomst
    
    # for Ord in words:
    #     if Ord in Ordbok:
    #         Ordbok[Ord] += 1 #tell opp en hvis ordet finnes
    #     else:
    #         Ordbok[ord]= 1 #legger til ordet med verdi en når nye ord finnes

    # print(Ordbok)
    
    # #compute_frequency('hun', 'hen', 'han', 'hen')
    # #print(compute_frequency(["hun", "hen", "han", "hen"]))
    # return Ordbok
    ##LASSE LINJER SLUTT
    

FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han', 'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']


def remove_filler_words(frequency_table):
    """
    Ofte inneholder tekst koblingsord som "og", "eller", "jeg", "da". Disse er ikke så spennende når man vil
    analysere innholdet til en tekst. Derfor vil vi gjerne fjerne dem fra vår frekvenstabell.
    Vi har gitt deg en liste med slike koblingsord i variablen FILL_WORDS ovenfor.
    Målet med denne funksjonen er at den skal få en frekvenstabll som input og så fjerne alle fyll-ord
    som finnes i FILL_WORDS.
    """
    #del frequency_tabl[]
    #print(type(frequency_table))
    #interasjon = -1
    #for index, hvertOrd in enumerate(FILL_WORDS):
    for key in FILL_WORDS:
        frequency_table.pop(key, None)
    
    #del frequency_table[''dei'']
        #interasjon = interasjon +1 
         
    #for hvertElement in TEGN_JEG_VIL_FJERNE: 
    #    EnStorString = EnStorString.replace(hvertElement,'') 
         
         
#        interasjon += interasjon
    #print(frequency_table)
    #no_rivers_dict= frequency_table.pop('og')
   # del frequency_table('og')
    #tall = frequency_table.popitem('dei')
    
    #print(tall)
    #print(no_rivers_dict)
    
    #for hvertElement in FILL_WORDS[:]:
    #OrdBokFjernetMas = {key.replace}
    #    resultatWords = frequency_table.strip([tall])
    #    tall += tall
    
    
   # print(resultatWords)
    return frequency_table  # TODO: Du må erstatte denne linjen

def largest_pair(par_1, par_2):
     # """
     # Denne funksjonen får som input to tupler/par (https://docs.python.org/3/library/stdtypes.html#tuple) der den
     # første komponenten er en string (et ord) og den andre komponenten er en integer (heltall).
     # Denne funksjonen skal sammenligne heltalls-komponenten i begge par og så gi tilbake det paret der
     # tallet er størst.
    #EKS par1 =()'navn1':32)
    # par2 = ('navn2' :4)
    
    # test1= ('navn1',32)
    # test2= ('nav2', 55)
    # print(test1[0])
    
    
    # test1= ('navn1',1)
    # test2= ('nav2', .1)
    # print(test1[0])
    # print(test1[1])
    # print(test2[0])
    # print(test2[1])
    BiggestTuple = ()
    
    if par_1[1] > par_2[1]:  
        print('Par1 er størt med verdien' + str(par_1[1]))
        BiggestTuple = par_1
    elif par_1[1] < par_2[1]: 
        print('Par er størt med verdien' + str(par_2[1]))
        BiggestTuple = par_2
    else: 
        print('Like store')
        BiggestTuple = par_1
    # print('verdi av 0th index i tuple 1 : ', par_1[:])
    # print('fg', par_2[:])
    # pri
    # tuple(1)
    # print(par1[0])
    # print(type(par_2))
     # OBS: Tenk også på situasjonen når to tall er lik! Vurder hvordan du vil handtere denne situasjonen
    #kanskje du vil skrive noen flere test metoder ?! 
    return BiggestTuple  # TODO: Du må erstatte denne linjen


def find_most_frequent(frequency_table):
    """
    Nå er det på tide å sette sammen alle bitene du har laget.
    Den funksjonen får frekvenstabllen som innputt og finner det ordet som dykket opp flest.
    """
    #FORSØK TO... Tar inn alle verdiene. Sjekker så alle forekomster av hvert ord. Når et nyttOrd har forekomt flest
    #ganger hittil, så lagres indeksen for dette ordet. Til slutt så hentes ordet som forkommer mest ut med indeksen som er funnet.
    
    # #vet at formatet i frekvens tabellene er slik
    # " eks= "
    # MestBruktOrd=''
    # MestBruktOrdAntall = 0
    # MestBruktOrdIndex = 0    
    # for hvertElement in frequency_table:
    #     if(hvert)

    # for key, value in table.items():
    #     if 
    #     print(f"{key}: {value}")
    AntallGangerAvORDET = -1 #setter en verdi av ordet. Vet at -1 0 osv ikke er brukt siden alle vil jo ha min 1 forkomest
    ORDETSomErMestAv= 'ordet'
    IndexPlasseringTilORDET=-1
    for index, (ordet, antall) in enumerate(frequency_table.items()):
        #sjekker om ordet jeg finner har større forekomster
        if antall > AntallGangerAvORDET:
            AntallGangerAvORDET = antall
            ORDETSomErMestAv = ordet
            IndexPlasseringTilORDET=index
            
    print('ordet med flest forekomster er  '+ ORDETSomErMestAv + 'med ' + str(AntallGangerAvORDET) +' forkomster')
    print('Ble funnet på index' + str(IndexPlasseringTilORDET) + 'i tabellen')        

    return ORDETSomErMestAv
    
    # #DUM LØSNINT START
    # #Vet at listen allerede er sortert fra tidligere.... henter bare ut siste verdi
    # SortertOrdbok = dict(sorted(frequency_table.items(), key=lambda item: item[1]))
    # print(len(SortertOrdbok))
    # siste = list(SortertOrdbok)[-1]
    # print(siste)
    # #DUM LØSNING SLUTT
    # return siste

    #print(last key = list(frequency_table[-1])
    #print(frequency_table['odin'])
    
    #tall=  frequency_table.popitem('odin')
    #print(tall)
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
