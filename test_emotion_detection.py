'''unit test for emotion_detection'''
from EmotionDetection.emotion_detection import emotion_detector #import to test
import unittest #Import testing framework

class TestEmotionDetection(unittest.TestCase): #Testing Class
    def test_emotion_detector(self): #testing function for emotion_detector
        input1 = emotion_detector('I am glad this happened') #input for test 1 
        result1 = 'joy' #expected result for test 1
        self.assertEqual(input1['dominante_emotion'], result1) #Test 1

        input2 = emotion_detector('I am really mad about this') #input for test 2
        result2 = 'anger' #expected result for test 2
        self.assertEqual(input2['dominante_emotion'], result2) #Test 2

        input3 = emotion_detector('I feel disgusted just hearing about this') #input for test 3
        result3 = 'disgust' #expected result for test 3
        self.assertEqual(input3['dominante_emotion'], result3) #Test 3

        input4 = emotion_detector('I am so sad about this') #input for test 4
        result4 = 'sadness' #expected result for test 4
        self.assertEqual(input4['dominante_emotion'], result4) #Test 4

        input5 = emotion_detector('I am really afraid that this will happen') #input for test 5
        result5 = 'fear' #expected result for test 5
        self.assertEqual(input5['dominante_emotion'], result5) #Test 5

unittest.main() #Call for unit tests
