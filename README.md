# Pong peli :red_circle:

## Dokumentaatiot
[Vaatimusmaarittely](https://github.com/Mimi-ctrl/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/Mimi-ctrl/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/Mimi-ctrl/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/Mimi-ctrl/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Releases](https://github.com/Mimi-ctrl/ot-harjoitustyo/releases)

[Käyttöohje](https://github.com/Mimi-ctrl/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

## Asennus

‼️ Ennen asennusta lataa viimeisin [releasen](https://github.com/Mimi-ctrl/ot-harjoitustyo/releases) lähdekoodi.

1. Avaa terminaali ja siirry kansioon "ot-harjoitustyo" ja sieltä kansioon "src". Asenna riippuvuudet komennolla:
```
poetry install
```
2. Käynnistä sovellus komennolla:
```
poetry run invoke start
```

## Komentorivitoiminnot

‼️ Ennen kuin suoritat komentorivitoimintoja siirry kansioon "ot-harjoitustyo" ja sieltä kansioon "src". 

#### Ohjelman suorittaminen
Ohjelma käynnistyy komennolla:
```
poetry run invoke start
```
#### Testaus
Suorita testit komennolla:
```
poetry run invoke test
```
#### Testikattavuus
Muodosta selaimessa avattava HTML-muotoinen testikattavuusraportti komennolla:
```
poetry run invoke coverage-report
```
#### Pylint
‼️ Siirry ensin kansion "ot-harjoitustyo" sisälle.

Suorita tiedoston [.pylintrc](https://github.com/Mimi-ctrl/ot-harjoitustyo/blob/master/.pylintrc) määrittelemät tarkistukset komennolla:
```
poetry run invoke lint
```
## HUOM‼️
Sovellusta on testattu Python 3.8. versiolla.
