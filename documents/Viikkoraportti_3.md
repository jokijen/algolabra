# Viikkoraportti 3

Käytetty tuntimäärä: 24


## Mitä olen tehnyt tällä viikolla?

Olen työstänyt ohjelman perustoiminnallisuuksia mm. käyttäjän antaman syötteen validointi ja käyttöliittymä. Olen lisäksi tehnyt yksikkötestejä. 


## Miten ohjelma on edistynyt?

Ohjelma on lähtenyt edistymään ihan mukavasti, mutta olen yhä jäljessä aikataulusta. Käyttäjän syötteen validointi on yllättänyt monimutkaisuudellaan ja sen suunnittelu tuntuu ajoittain hieman mudassa tarpomiselta. Alustava käyttöliittymä toimii, vaikkei olekaan visuaalisesti vielä kaikkein selkein. 


## Mitä opin tällä viikolla / tänään?

Olen palauttanut mieleen monia Python synytaksiin liittyviä yksityiskohtia. Käyttäjän syötteen validointi on monipuolinen tehtävä, jossa täytyy huomioida useita asioita, joten olen yrittänyt miettiä tähän hyviä "pythonisia" ja modulaarisia ratkaisuja, jotta koodi pysyy selkeänä ja voin myöhemmin tarpeen mukaan muokata sitä tai lisätä uutta helposti. 


## Mikä jäi epäselväksi tai tuottanut vaikeuksia?

Tuleeko käyttäjän voida määrittää muuttujan arvoksi jotain monimutkaisempaa, kuin lukuarvo? esim. A = 2 vs. A = 2+2*pi 

Toistuvasti mietin teenkö oikeita ratkaisuja ja missä menee järkevän koodin ja spagetin raja. Pyrin modulaarisuuteen ja siihen että asiat tehdään niiden omissa dedikoiduissa funktioissa/metodeissa. Ottaisin mielelläni vastaan palautetta koodin laadusta ja koko lähestymistavasta käyttäjän syötteen kanssa. En ole tyytyväinen UI:hin, sillä siellä on liian paljon kaikkea.

Luokan "InputValidator" metodissa "validate_expression" olisi seuraavaksi suunnitelmissa iteroida merkkijono läpi ja tunnistaa sieltä validit "tokenit", jotka sitten lisätään listaan ja palautetaan. Vaihtoehtoisesti, jos syöte ei ole validi, niin palautetaan kuvaava virhe, josta käy ilmi miksi näin on.


## Mitä teen seuraavaksi?

Jatkan perustoimintojen parissa. Yritän myös lisätä testejä ja saada GitHub Actionsin + Codecovin pystyyn.
