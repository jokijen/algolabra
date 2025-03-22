# Määrittelydokumentti

## Mitä ohjelmointikieltä käytät? Kerro myös mitä muita kieliä hallitset siinä määrin, että pystyt tarvittaessa vertaisarvioimaan niillä tehtyjä projekteja.

Python. En hallitse muita kieliä riittävästi.


## Mitä algoritmeja ja tietorakenteita toteutat työssäsi?

Toteutan tieteellisen laskimen, joka validoi syötteen, muuntaa sen postfix-notaatioksi ja ratkaisee sen. Työssä käytetään pino ja jono tietorakenteita sekä Shuntig-Yard -algoritmia. 


## Minkä ongelman ratkaiset?

Käyttäjä voi antaa matemaattisen lausekkeen ja ohelma laskee sen arvon. 


## Mitä syötteitä ohjelma saa ja miten niitä käytetään?

Ohjelma saa syötteeksi matermaattisen lausekkeen, joka koostuu numeroista (0–9), operaattoreista (+, -, *, /, ^), sallituista merkeistä (".", "(", ")") ja funktioista (sqrt, sin, min, max). Ohjelma tulostaa vastauksen tai informatiivisen virheilmoituksen syötteen ollessa virheellinen. 


## Tavoitteena olevat aika- ja tilavaativuudet (esim. O-analyysit)

Tavoitteena on aikavaativuus O(n), joka on riippuvainen syötteen pituudesta. Eri osien aikavaativuudet ovat O(1)–O(n) riippuen osasta, esim. pino (stack) ja jono (queue) rakenteiden aikavaativuus on O(1). 
