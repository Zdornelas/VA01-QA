import unittest
from app.validacao import validar_cpf

class TestValidarCPF(unittest.TestCase):
    def test_cpfs_validos(self):
        self.assertTrue(validar_cpf("529.982.247-25"))
        self.assertTrue(validar_cpf("12345678909"))
        self.assertTrue(validar_cpf("111.444.777-35"))
    
    def test_cpfs_invalidos(self):
        self.assertFalse(validar_cpf("123.456.789-00"))
        self.assertFalse(validar_cpf("111.111.111-11"))  
        self.assertFalse(validar_cpf("00000000000"))   
    
    def test_entrada_invalida(self):
        self.assertFalse(validar_cpf(""))
        self.assertFalse(validar_cpf("abc.def.ghi-jk"))
        self.assertFalse(validar_cpf("123")) 
        self.assertFalse(validar_cpf("12345678909123"))
        