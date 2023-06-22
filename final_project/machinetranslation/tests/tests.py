import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslation(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('Hi'), 'Bonjour')
        self.assertNotEqual(englishToFrench('Yes'), 'Au Revoir')

    def test_frenchToEnglish(self):
       self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
       self.assertNotEqual(frenchToEnglish('Au Revoir'), 'Yes')

unittest.main()
