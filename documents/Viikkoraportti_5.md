# Viikkoraportti 5

Käytetty tuntimäärä: 28


## Mitä olen tehnyt tällä viikolla? 

Keskityin Shunting-Yard -algoritmin sekä RPN/postfix-lausekkeen evaluoinnin toteuttamiseen. Lisäksi olen parannellut syötteen validointia, jossa on yhä pieniä puutteita, jotka vaikuttavat lopputuloksen oikeellisuuteen tietyissä tapauksissa. Nämä tapaukset löytyivät manuaalisella testauksella ja on raportoitu dokumentaatiossa.

Olen lisäksi panostanut tällä viikolla kommentointiin ja koodin laatuun, eli lisännyt kommentteja ja refaktoroinut tai siistinyt koodia joiltain osin.


## Miten ohjelma on edistynyt? 

Ohjelma on edistynyt hyvin tällä viikolla. Olikin tiedossa, että itse Shunting-Yard -algoritmin ja evaluoinnin toteutus on nopeaa, kunhan syöte on oikeanlainen, mutta ehkä jopa yllätti miten yksinkertaista niiden toteuttaminen oli. Etenkin, kun on tuntikaupalla paininut validoinnin kanssa.

Dokumentaatio on pysynyt ajan tasalla, mutta testikattavuus on jäänyt hieman jälkeen.


## Mitä opin tällä viikolla / tänään?

Olen perehtynyt PEP-ohjeistuksiin ja pyrkinyt omaksumaan yleisesti hyvänä pidettyä Python-ohjelmointityyliä. 

Olen lisäksi perehtynyt joidenkin suoritettujen laskutoimitusten (etenkin funktioiden) yksityiskohtiin ja sallittuihin/ei-sallittuihin syötetyyppeihin. 


## Mikä jäi epäselväksi tai tuottanut vaikeuksia?

Olen jatkanut pohdintaa validoinnin toiminnan ja rakenteen osalta. Koodi ei ole aivan niin modulaarista, kun haluaisin ja toiminnassakin on pieniä puutteita. Olisi myös mukavaa saada käyttäjille joissain tapauksessa kuvaavampia virheilmoituksia, koska on kohtuullisen todennäköistä, että käyttäjälle sattuu virheitä, etenkin pitkän lausekkeen kansssa.

Käyttöliittymään en myöskään ole täysin tyytyväinen. Käyttäjää on tarpeen ohjeistaa paljon, mikä tarkoittaa että ohjetekstiä on paljon. Missä määrin käytettävyyteen ja visuaalisuuteen on syytä panostaa? Jotain parannuksia tähän pyrin joka tapauksessa tekemään.

Alkaako laskimen toiminnallisuus olla kunnossa?: 

- Tällä hetkellä käyttäjä saa asettaa arvon muuttujalle. Tämä validoidaan ja muutetaan tokeneiksi vasta, kun muuttujaa käytetään lausekkeessa. Toinen vaihtoehto olisi validoida ja tokenisoida muuttujan arvo heti, jolloin käyttäjälle voisi antaa palautetta sen oikeellisuudesta. En ole toteuttanut tätä, koska muuttujan käsitteleminen on turhaa työtä, jos sitä ei ikinä käytetä. Toisaalta normaalikäytössä käyttäjä tuskin tallentaisi turhia muuttujia. Jos muuttuja validoitaisiin ja tokenisoitaisiin heti, tämän tokenisoidun version voisi tallentaa uuteen sanakirjaan (tai samaan sanakirjaan niin että value on tuple, jonka ensimmäinen osa on alkup. str ja toinen osa token list) ja muuttujat saisi sieltä käyttöön nopeasti myöhemmin.

- Muuttujien asettamisen ja katselemisen lisäksi käyttäjä saa syöttää lausekkeen arvoitavaksi. Käyttäjälle tulostetaan muutamia välivaiheita, joista osa tulostetaan kehitystä ajatellen ja poistetaan myöhemmin. Ainakin lauseke RPN-muodossa ja laskun lopputulos tulee tulostaa. Ehkä käyttäjälle voisi myös antaa mahdollisuuden tallentaa laskun tulos muuttujaan.


## Mitä teen seuraavaksi?

Parantelen yhä validointia, jotta saan muutamat [bugit](./IMPLEMENTATION.md#bugs) korjattua ja koodista hieman modulaarisempaa. Aion myös tehdä lisää testejä. Tämän jälkeen alan katsoa käyttöliittymää. 
