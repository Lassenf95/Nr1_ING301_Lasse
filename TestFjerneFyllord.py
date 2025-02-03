import sys

FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han', 'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']


def remove_filler_words(frequency_table):
    """
    Ofte inneholder tekst koblingsord som "og", "eller", "jeg", "da". Disse er ikke så spennende når man vil
    analysere innholdet til en tekst. Derfor vil vi gjerne fjerne dem fra vår frekvenstabell.
    Vi har gitt deg en liste med slike koblingsord i variablen FILL_WORDS ovenfor.
    Målet med denne funksjonen er at den skal få en frekvenstabll som input og så fjerne alle fyll-ord
    som finnes i FILL_WORDS.
    """
    ListeSplittet = frequency_table
    LinjerFilterert = ListeSplittet.strip(['og','eller','jeg','da']) #fjerner alle ''ord'' i listen som er av , . : ; ! `?`
    return LinjerFilterert  # TODO: Du må erstatte denne linjen


for element in FILL_WORDS: #PASS PÅ Å IKKE BRUKE LIST, fordi det er en funksjon, da endrer man på funksjonen. Husk PROG2 sin eksamens oppgave jeg misfrostod
    print(element) 
    

RensetListe = remove_filler_words(FILL_WORDS)

    
for element in RensetListe:
    print(element)