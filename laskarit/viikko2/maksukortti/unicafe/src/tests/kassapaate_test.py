import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
       

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateisosto_edullinen_maksu_riittava(self):
        res = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(res, 60 )
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kateisosto_maukas_maksu_riittava(self):
        res = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(res, 100 )
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_edullinen_maksu_ei_riittava(self):
        res = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(res, 100 )
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kateisosto_maukas_maksu_ei_riittava(self):
        res = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(res, 200 )
        self.assertEqual(self.kassapaate.maukkaat, 0)

    
    def test_korttiosto_edullinen_maksu_riittava(self):
        maksukortti = Maksukortti(1000)
        res = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 760)
        self.assertEqual(res, True )
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_korttiosto_maukas_maksu_riittava(self):
        maksukortti = Maksukortti(1000)
        res = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 600)
        self.assertEqual(res, True )
        self.assertEqual(self.kassapaate.maukkaat, 1)
    

    def test_korttiosto_edullinen_maksu_ei_riittava(self):
        maksukortti = Maksukortti(100)
        res = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(res, False )
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_korttiosto_maukas_maksu_ei_riittava(self):
        maksukortti = Maksukortti(100)
        res = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(res, False )
        self.assertEqual(self.kassapaate.maukkaat, 0)
    

    def test_kortti_saldo_lataus(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 600)
        self.assertEqual(maksukortti.saldo, 700)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100600)
    

    def test_kortti_saldo_lataus_negatiivinen(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -600)
        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
       

    


        
        
    
    


    



    """ def syo_edullisesti_kateisella(self, maksu):
        if maksu >= 240:
            self.kassassa_rahaa = self.kassassa_rahaa + 240
            self.edulliset += 1
            return maksu - 240
        else:
            return maksu

    def syo_maukkaasti_kateisella(self, maksu):
        if maksu >= 400:
            self.kassassa_rahaa = self.kassassa_rahaa + 400
            self.maukkaat += 1
            return maksu - 400
        else:
            return maksu

    def syo_edullisesti_kortilla(self, kortti):
        if kortti.saldo >= 240:
            kortti.ota_rahaa(240)
            self.edulliset += 1
            return True
        else:
            return False

    def syo_maukkaasti_kortilla(self, kortti):
        if kortti.saldo >= 400:
            kortti.ota_rahaa(400)
            self.maukkaat += 1
            return True
        else:
            return False

    def lataa_rahaa_kortille(self, kortti, summa):
        if summa >= 0:
            kortti.lataa_rahaa(summa)
            self.kassassa_rahaa += summa
        else:
            return """