from pathlib import Path
import sys
#import filter
import collections
#

def read_file(file_name):
    """
    Denne funksjonen får et filnavn som argument og gir
    tilbake en liste av tekststrenger som representerer linjene i filen.
    """
    #får feilmelding på at python ikke kan lese det. formatet på filen er cp1252, konverter til utf-8.
    
    filenSomLeses = open(file_name, encoding="utf-8")     
    innholdIFilen = filenSomLeses.read()
    innholdSomLinjer = innholdIFilen.split("\n")
    
    #ALTERNATIV ENDA KORTET 
    #with open(file_name, encoding="utf-8") as filenSomLeses:
    #   innholdSomLinjer = filenSomLeses.read().splitlines()
    filenSomLeses.close()
    
    
   
   # with open(file_name, encoding="utf-8") as filenSomLeses:
    #    innholdSomLinjer = filenSomLeses.read().splitlines()
    return innholdSomLinjer




def lines_to_words(lines): #mater inn en liste format [a,b,c d... osv] til her. split funksjonene funker bare på string, så må lage en lang string av hele lista før 
    #print(lines)
    #print(type(lines))
    
    EnStorString = ''
    for alleLinjer in lines:   #bygger opp hele stringen før splitting og rensing  
         EnStorString += alleLinjer +' ' 
    #print(EnStorString)
    
    TEGN_JEG_VIL_FJERNE = ['.','-',',',';','!','?',';',':'] #RENSETIS
    for hvertElement in TEGN_JEG_VIL_FJERNE:    
        EnStorString = EnStorString.replace(hvertElement, '')  #erstatter alle tegn og erstatter de med ingenting
    #print(EnStorString)
    
    #får alt i lower case
    EnStorString = EnStorString.lower() #Overskriver stringen med en ny string der alt ewr lite
    
    #gjør om til liste igjen. splitter alt med mellomrom
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
    SortertOrdbok = dict(sorted(Ordbok.items(), key=lambda item: item[1]))
    #print(type(Ordbok))
    #SortertOrdbok =/=
    #SortertOrdbok=sorted(Ordbok.keys()) #[:]
    #print(Ordbok)
    #sorted(frequency_table.keys())
   # print(SortertOrdbok)
     
    return SortertOrdbok #senter ut resultatet 
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
    interasjon = 0
    for hverOrd in FILL_WORDS[:]:
        del frequency_table[FILL_WORDS[interasjon]]
        interasjon = interasjon +1 
         
#        interasjon += interasjon
    print(frequency_table)
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
    
    print('verdi av 0th index i tuple 1 : ', par_1[:])
    print('fg', par_2[:])
    
    #tuple(1)
    #print(par1[0])
    #print(type(par_2))
    # OBS: Tenk også på situasjonen når to tall er lik! Vurder hvordan du vil handtere denne situasjonen
    # kanskje du vil skrive noen flere test metoder ?!
    #return NotImplemented  # TODO: Du må erstatte denne linjen


def find_most_frequent(frequency_table):
    """
    Nå er det på tide å sette sammen alle bitene du har laget.
    Den funksjonen får frekvenstabllen som innputt og finner det ordet som dykket opp flest.
    """
    #Vet at listen allerede er sortert fra tidligere.... henter bare ut siste verdi
    print(len(frequency_table))
    siste = list(frequency_table)[-1]
    print(siste)
    return siste
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
