import unittest

from translator import english_to_french, french_to_english

class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        #self.assertIsEqual(english_to_french(None),None)
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(english_to_french('Hello'),'Kamusta')
        

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        #self.assertEqual(french_to_english(None),None)
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertNotEqual(french_to_english('Bonjour'),'Goodbye')

unittest.main()