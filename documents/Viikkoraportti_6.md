# Viikkoraportti 6

Käytetty tuntimäärä: 12


## Mitä olen tehnyt tällä viikolla? 

Muutin laskimen toimintaa ohjaajan kanssa käytyjen keskustelujen pohjalta. Käyttäjä voi nyt joko määrittää muuttujan tai vain saada lausekkeelle arvon vastaukseksi riippuen siitä, miten hän kirjoittaa lausekkeen: Jos lauseke alkaa isolla aakkosella ja yhtäsuuruusmerkillä, määritetään muuttuja (esim. "A="). Jos muuttuja on jo käytössä, saa käyttäjä valita muuttujan päivityksen, uuden muuttujan, tai ohituksen väliltä. 

Päivitin yksikkötestejä ja lisäsin uusia. Tein pientä koodin siistimistä ja korjasin yhden bugin, joka johtui floating point -numeroista. 


## Miten ohjelma on edistynyt? 

Ohjelma on hyvällä mallilla. Yksi [bugi](./IMPLEMENTATION.md#bugs) on yhä korjaamatta, mutta olen jo suunnitellut tähän ratkaisun.

Periaatteessa toiminnallisuus on valmis, minkä lisäksi testaus sekä dokumentaatio ovat hyvällä mallilla.


## Mitä opin tällä viikolla / tänään?

Olen yrittänyt löytää sopivan tavan tehdä yksikkötestejä laajempaa testausta. Olen perehtynyt hieman Pytestin monkeypatchiin ja lähden varmaan testailemaan sitä. 

Ohjelman toimintaa muuttaessani kävi hyvin selväksi miten arvokasta modulaarisuus ja selkeys on. Muokkaus oli yllättävän helppoa, eikä ohjelma hajonnut muutoksen yhteydessä. 


## Mikä jäi epäselväksi tai tuottanut vaikeuksia?

Käyttäjälle tarjotaan nyt kaksi vaihtoehtoa: 
- "1: Get a solution for an expression or set a variable"
- "2: List all defined variables"

Käyttäjä voi siis syöttää lausekkeen tyyliin "7+7" joka määrittää muuttujan "A=14", tai "7+7", jolloin palautetaan vastaus "14". Tämä lienee nyt ok?

Olen suunnitellut hieman yksikkötestejä laajempaa testausta ja törmännyt Pytestin monkeypatchiin, jonka avulla uskoisin saavani tehtyä end-to-end testejä. Tämä (eli end-to-end ja yksikkötestit) riittänee testien osalta?


## Mitä teen seuraavaksi?

Korjaan [bugin](./IMPLEMENTATION.md#bugs). Suunnitelmissa on myös parantaa käyttöliittymän koodia ja tehdä siitä hieman modulaarisempaa. Käyttäjälle näytettäviä ohjeita pitäisi myös selkeyttää. Aion myös tehdä lisää testejä ja viimeistellä dokumentaatiota. 
