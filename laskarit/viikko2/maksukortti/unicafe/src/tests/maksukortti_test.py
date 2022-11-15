import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    

    def test_lataa_rahaa_lisaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa") 
    

    def test_ota_rahaa_vahentaa_saldoa_oikein(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa") 

    def test_ota_liikaa_rahaa_ei_vahenna_saldoa(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa") 
    
    def test_metodi_palauttaa_true(self):
        res = self.maksukortti.ota_rahaa(500)
        self.assertEqual(res, True) 

    def test_metodi_palauttaa_true(self):
        res = self.maksukortti.ota_rahaa(1500)
        self.assertEqual(res, False) 




