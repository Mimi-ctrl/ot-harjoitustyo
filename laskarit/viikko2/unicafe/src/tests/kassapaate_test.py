import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(500)

    def test_rahamaara_ja_myytyjen_lounaiden_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_kassassa_oleva_rahamaara_kasvaa_lounaan_hinnalla_ja_vaihtorahan_suuruus_on_oikea_edullisesti(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(260), 20)

    def test_kassassa_oleva_rahamaara_kasvaa_lounaan_hinnalla_ja_vaihtorahan_suuruus_on_oikea_maukkaasti(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(450), 50)

    def test_maksu_on_riittava_ja_myytyjen_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maksu_ei_ole_riittava_edulliseen(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maksu_ei_ole_riittava_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortilla_on_tarpeeksi_rahaa_edulliseen_joten_veloitetaan_summa_kortilta_ja_palautetaan_true(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertTrue(str(self.maksukortti), "saldo: 2.6" )
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortilla_on_tarpeeksi_rahaa_maukkaaseen_joten_veloitetaan_summa_kortilta_ja_palautetaan_true(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertTrue(str(self.maksukortti), "saldo: 1.0" )
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortilla_ei_ole_riittavasti_maukkaaseen(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertTrue(str(self.maksukortti), "saldo: 1.0" )
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortilla_ei_ole_riittavasti_edulliseen(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertTrue(str(self.maksukortti), "saldo: 1.0" )
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kassassa_oleva_rahamaara_ei_muutu_kortilla_ostettaessa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu_ja_kassassa_oleva_rahamaara_kasvaa_ladatulla_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(str(self.maksukortti), "saldo: 7.0" )
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -2)
        self.assertEqual(str(self.maksukortti), "saldo: 7.0" )
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)
