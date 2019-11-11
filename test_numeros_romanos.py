import unittest

"""def descobre_num_proximo(numero, chaves):
    for k in chaves:
        if k <= numero and k > (numero-2):
"""

def converte_decimal(decimal):
    dicionario_de_conversao = {
        1: "I",
        4: "IV",
        5: "V",
        10: "X"
    }


    if decimal in dicionario_de_conversao.keys():
        return dicionario_de_conversao[decimal]
    chaves = list(dicionario_de_conversao.keys())
    resposta = ""
    iteravel = decimal
    while iteravel>0:
        chave_anterior = 1
        for k  in chaves:
            if k>=iteravel:
                resposta += dicionario_de_conversao[chave_anterior]
                iteravel -= chave_anterior
                break
            chave_anterior = k


    """""
    chaves = list(dicionario_de_conversao.keys())
    for k in chaves:
        if k > iteravel:
            while (iteravel > 0):
                resposta += dicionario_de_conversao[chave_anterior]
                iteravel -= chave_anterior
            '''iteravel = iteravel % (chave_anterior)'''
        else:
            chave_anterior = k
        if iteravel == 0:
            break
    
    while iteravel > 0:
        resposta += dicionario_de_conversao[1]
        iteravel -= 1
    """

    return resposta


class TestNumerosRomanos(unittest.TestCase):
    def test_framework(self):
        self.assertTrue(True)

    def test_I(self):
        entrada = 1
        saida = "I"
        self.assertEqual(saida, converte_decimal(entrada))

    def test_II(self):
        entrada = 2
        saida = "II"
        self.assertEqual(saida, converte_decimal(entrada))

    def test_V(self):
        entrada = 5
        saida = "V"
        self.assertEqual(saida, converte_decimal(entrada))

    def test_XI(self):
        entrada = 11
        saida = "XI"
        self.assertEqual(saida, converte_decimal(entrada))

    def test_VI(self):
        entrada = 6
        saida = "VI"
        self.assertEqual(saida, converte_decimal(entrada))

if __name__ == '__main__':
    unittest.main()
