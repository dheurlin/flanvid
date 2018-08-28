# Huvud-features:

* Kör youtubevideor, man kan föreslå videor och rösta på vilken man vill ska spela nästa
* Den videon som har flest röster spelas upp, sedan tas den bort från listan
* Skydda mot concurrency-problem vid röstning! Tror Django har nåt gött inbyggt
* Man kan bara rösta en gång på en video
* Listan av videos bör uppdateras asynkront så att man kan se vilken ordning de
    ligger i, och vilka nya som lagts till
* Behöver nån slags "admin"-användare för den datorn som videon spelas upp på.
    När videon spelats färdigt bör den hämta nästa video och ta bort den nyligen
    spelade från kön.
    -   Denna bör endast få besökas av en enhet i taget, annars typ race
        conditions om flera spelar videon samtidigt.

# Bonus-features (i mån av tid):

* inga videor över typ 10 min
* Admin-interface för att ta bort alla i kön/specifika videor (enkelt med Django
    admin)
* Begränsa till en vid per person, personen kan ta bort sin egen video
