# Viikkoraportti 4 

Käytetty tuntimäärä: 28


## Mitä olen tehnyt tällä viikolla? 

CI + testaus: Tein workflowt testaukselle ja koodin tarkistukselle (linting). Tein lisää yksikkötestejä ja testikattavuus on nyt hyvä. Laitoin Codecovin pystyyn, joten testikattavuutta pääsee tarkastelemaan siellä. Tein alustavan testausdokumentin ja päivitin myös muita dokumentteja.

Olen jatkanut ohjelman perustoiminnallisuuksien työstämistä: Käyttäjän syötteen (osittainen) validointi ja muuntaminen tokeneiksi. Syötteessä (mathematical expression) olevien muuttujien avaaminen ja muuntaminen tokeneiksi.


## Miten ohjelma on edistynyt? 

Luokka InpuValidator on mahdollisesti valmis ja ShuntingYard algoritmin toteutus on alkanut. Dokumentaatio on kunnossa ja heijastaa nykyistä tilannetta. 

Olen työskennellyt hieman viipyilevästi ja käyttänyt paljon aikaa toimintalogiikan säätämiseen ja refaktorointiin, koska tehtävän on tarkoitus olla oppimisprosessi. Olen myös panostanut InputValidatoriin sillä ajatuksella, että kun se toimii hyvin, ovat RPN-konversio ja lausekkeen arviointi astetta helpompia operaatioita.  


## Mitä opin tällä viikolla / tänään?

Olen miettinyt paljon sovelluksen sisäistä rakennetta, siinä käytettyä logiikkaa ja missä järjestyksessä asioita kannattaisi tehdä. Olen pyrkinyt pitämään kiinni modulaarisuudesta ja selkeydestä, vaikka välillä olisi kiusaus tehdä useampia asioita yhdellä kertaa. Usein huomaa vanhempaa koodinpätkää lukiessa, että selkeys on merkittävä prioriteetti.


## Mikä jäi epäselväksi tai tuottanut vaikeuksia?

Olen kohtuullisen tyytyväinen InputValidatorin toimintaan, mutta toisaalta haluaisin lisätä sinne vielä validointia (esim. sulkujen tarkastus). En kuitenkaan haluaisi käydä läpi lausekemerkkijonoa (monesti?) turhaan, koska se tulee käytyä läpi myöhemmin joka tapauksessa. Kuitenkin olisi ehkä parempi, että "validaattori" hoitaa validoinnin. Merkkijonon läpikäynti ei kuitenkaan ole erityisen kallis/hidas operaatio kun syöte on käyttäjän kirjoittama, kohtuullisen lyhyt lauseke.


## Mitä teen seuraavaksi?

Jatkan perustoimintojen parissa ja pyrin saamaan sovelluksen hyvään ”vertaisarviokuntoon”.
