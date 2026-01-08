import unittest

def calcular_media(notas):
    """
    Recebe uma lista de notas e retorna a média.
    """
    if not notas:
        return 0
    
    soma = 0
    for nota in notas:
        soma += nota
    
    media = (soma / len(notas))
    return media


class TestMedia(unittest.TestCase):

    def test_media(self):
        self.assertEqual(calcular_media([5, 5, 5]), 5)
        self.assertEqual(calcular_media([10, 8, 9]), 9)
        self.assertEqual(calcular_media([7, 8, 9]), 8)
        self.assertEqual(calcular_media([7, 9]), 8)
        self.assertEqual(calcular_media([]), 0)


if __name__ == '__main__':
    unittest.main()