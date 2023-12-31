'''A module to utilize Watson's emotion detection capabilities'''
import json #Import Json to format response
import requests #Import requests to talk to watson

def emotion_detector(text_to_analyse):
    '''Analyse a block of text and predict the emotion behind it'''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' #URL for Watson't Emotion predict function
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} #header to send to watson
    myobj = { "raw_document": { "text": text_to_analyse } } #put text to analyse in an object to send
    response = requests.post(url, json = myobj, headers = header, timeout = 5.000) #send request and populate response with
    
    if response.status_code == 400: #if text_to_analyse is empty...
        return{ #return a dictionary with emotion keys and all values equal None
                'anger': None, 
                'disgust': None,
                'fear': None,
                'Joy': None,
                'sadness': None,
                'dominant_emotion': None,
            }
    
    formatted = json.loads(response.text) #Format json response as python dictionary

    emotions = formatted['emotionPredictions'][0]['emotion'] #Grab the emotions dictionary out of the formatted dictionary
    
    dominant_emotion = 'default' #set dominant_emotion as default
    dominant_value = 0 #set dominant_value as default

    for emotion, score in emotions.items(): #iterate through eotions
        if dominant_value < score: #If dominant_value is less than current emotions value...
            dominant_emotion = emotion #Set dominant_emotion to current emotion
            dominant_value = score #set dominant value to current emotion value

    response = {}

    print('{') #Print { for opening of dictionary
    i=0 #set i to 0
    for emotion in emotions: #iterate through emotions
        print("'",emotion,"': ",emotions[emotion],",", sep='') #print current emotion and value in format '<emotion>': <emotion value>,
        i = i+1 #increase i by 1
        response[emotion] = emotions[emotion]
    print("'dominant_emotion': '",dominant_emotion,"'",sep='') #print dominant emotion
    print("}") #Print } for end of dictionary

    response['dominant_emotion'] = dominant_emotion
    return response
