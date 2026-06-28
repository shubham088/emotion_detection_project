import unittest
from EmotionDetection.emotion_detection import text_to_analyze


class TestAddNumbers(unittest.TestCase):
    
    # Test case for standard positive integers
    def test_joy(self):
        result = text_to_analyze('I am glad this happened.')
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger(self):
        result = text_to_analyze('I am really mad about this.')
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust(self):
        result = text_to_analyze('I feel disgusted just hearing about this')
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness(self):
        result = text_to_analyze('I am so sad about this.')
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear(self):
        result = text_to_analyze('I am really afraid that this will happen')
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()