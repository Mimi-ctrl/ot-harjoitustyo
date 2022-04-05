# Ohjelmistotekniikka, harjoitustyö
## Dokumentaatiot
[vaatimusmaarittely.md](https://github.com/Mimi-ctrl/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[tuntikirjanpito.md](https://github.com/Mimi-ctrl/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[changelog.md](https://github.com/Mimi-ctrl/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

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
