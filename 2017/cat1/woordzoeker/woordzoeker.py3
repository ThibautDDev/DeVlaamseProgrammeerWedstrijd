import numpy as np

for testgeval in range(1, 1 + int(input(''))):
    invoerLijn = input("")
    invoerLijn = invoerLijn.split(" ")
    aantal_woorden = int(invoerLijn[0])
    aantal_rijen = int(invoerLijn[1])
    aantal_kolommen = int(invoerLijn[2])
    print(aantal_woorden, aantal_rijen, aantal_kolommen)

    woordenlijst = [input() for i in range(aantal_woorden)]


    

    ver = []
    for i in range(aantal_rijen):
        lijn = ""
        for j in range(aantal_kolommen):
            lijn += hor[j][i]
        ver += [lijn]
    
    #ver, woordenlijst = checkList(ver, woordenlijst)
    print(ver)
    print()

    #####
    #Diagonalen implementeren!
    ####

"""
1
16 12 12
clojure
cpp
csharp
haskell
java
nodejs
pascal
perl
php
prolog
python
ruby
scala
scheme
visualbasic
lisp
kanjlleksahe
tpclojureeam
dhnodejsezev
rpaaglacsapy
nohtypvavndb
visualbasicu
epvlapjamser
prroargppcra
mameloemehcs
ehrwalperled
sstrcoijpsil
dcopsglossen
    """
    


      

    

