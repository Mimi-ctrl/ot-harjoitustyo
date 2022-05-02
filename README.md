# Pong peli :red_circle:

## Dokumentaatiot
[vaatimusmaarittely](https://github.com/Mimi-ctrl/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[tuntikirjanpito](https://github.com/Mimi-ctrl/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[changelog](https://github.com/Mimi-ctrl/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[arkkitehtuuri](https://github.com/Mimi-ctrl/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[releases](https://github.com/Mimi-ctrl/ot-harjoitustyo/releases)

## Asennus
1. Asenna riippuvuudet:
```
poetry install
```
2. Suorita vaadittavat alustustoimenpiteet:
```
poetry run invoke build
```
3. Käynnistä sovellus:
```
poetry run invoke start
```

## Komentorivitoiminnot
#### Ohjelman suorittaminen
Ohjelma käynnistyy:
```
poetry run invoke start
```
#### Testaus
Suorittaa testit pytestin avulla:
```
poetry run invoke test
```
#### Testikattavuus
Muodostaa selaimessa avattavan HTML-muotoisen testikattavuusraportin:
```
poetry run invoke coverage-report
```
#### Pylint
Suorittaa tiedoston [.pylintrc](https://github.com/Mimi-ctrl/ot-harjoitustyo/blob/master/.pylintrc) määrittelemät tarkistukset:
```
poetry run invoke lint
```
## HUOM‼️
Sovellusta on testattu Python 3.8. versiolla.
