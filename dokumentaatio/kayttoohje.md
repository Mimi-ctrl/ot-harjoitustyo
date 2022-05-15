# Käyttöohje

Lataa viimeisin [releasen](https://github.com/Mimi-ctrl/ot-harjoitustyo/releases) lähdekoodi **Assets**-osion alta valitsemalla **Source code**.

## Pelin käynnistys

1. Avaa terminaali ja siirry kansioon "ot-harjoitustyo" ja sieltä kansioon "src". Asenna riippuvuudet komennolla:
```
poetry install
```
2. Käynnistä peli komennolla:
```
poetry run invoke start
```
## Pelin kulku

Pelin käynnistyksen jälkeen näytölle aukeaa peli ikkuna. Pelin aloitus näkymästä löytyy ohjeet. Peli alkaa painamalla `ENTER` näppäintä ja pelistä poistutaan painamalla `ESC` näppäintä.


![Kuvakaappaus - 2022-05-03 14-51-00](https://user-images.githubusercontent.com/56686737/166503077-beb1061a-14f5-4941-84f4-886d49c446e8.png)

Peliä pelataan nuolinäppäimillä `↑` ja `↓` sekä näppäimillä `w` ja `s`. Jos pallo ei osu lautaan, saa vasta pelaaja pisteen. Peli päättyy kun toisella pelaajista on 20 pistettä. Pelin saa tauolle painamalla `p` näppäintä ja peli jatkuu painamalla `ENTER` näppäintä.

![Kuvakaappaus - 2022-05-03 14-51-07](https://user-images.githubusercontent.com/56686737/166504193-ea314bf4-a598-4312-ade8-c75a9a5dce52.png)
![Kuvakaappaus - 2022-05-03 14-51-12](https://user-images.githubusercontent.com/56686737/166504661-9e199576-8c82-43c3-a1fe-06348f99c03e.png)

Kun peli loppuu niin pisteet nollautuvat ja pelin voi aloittaa alusta painamalla `ENTER` näppäintä.

![Kuvakaappaus - 2022-05-03 14-51-59](https://user-images.githubusercontent.com/56686737/166504996-440dc5f6-73ce-4bc6-bd3a-b49df35fbf68.png)

