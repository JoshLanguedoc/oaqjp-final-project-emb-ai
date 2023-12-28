import json #Import Json to format response
import requests #Import requests to talk to watson
import pprint

def emotion_detector(text_to_analyse):
    '''Analyse a block of text and predict the emotion behind it'''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' #URL for Watson't Emotion predict function
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} #header to send to watson
    myobj = { "raw_document": { "text": text_to_analyse } } #put text to analyse in an object to send
    response = requests.post(url, json = myobj, headers = header, timeout = 5.000) #send request and populate response with

    formatted = json.loads(response.text) #Format json response as python dictionary

    emotions = formatted['emotionPredictions'][0]['emotion'] #Grab the emotions dictionary out of the formatted dictionary

    pprint(emotions)
    #pick up at Task 3:4
