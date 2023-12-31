''' 
    A server to access EmotionDetection package and return results.
    port: 5000
'''
from flask import Flask, render_template, request #flask things for server stuff
from EmotionDetection.emotion_detection import emotion_detector #to detect the emotions

app = Flask('Emotion Detection') #initialize Flask as 'Emotion Detection'

@app.route("/emotionDetector") #route decorator for /emptionDetector
def emot_detect():
    '''Pass request arguments to emotion_detector then format and return response'''
    text_to_analyse = request.args.get('textToAnalyze') #set text_to_analyse to request argument 'textToAnalyze'

    detector_output = emotion_detector(text_to_analyse) #sets response to

    if detector_output['dominant_emotion'] is None: #if dominant emotion is None...
        return 'Invalid text! Please try again!.' #return invalid input message

    response = "For the given statement, the system response is " #starts forming the response

    for emotion, score in detector_output.items(): #iterate throuhg detector_output
        if emotion != 'dominant_emotion': #if current emotion is not 'dominant_emotion'...
            response = response+"'"+emotion+"': "+str(score)+", " #Append current emotion and value to response

    response = response+". The dominant emotion is "+detector_output['dominant_emotion'] #finish off response by appending dominant emotion phrase

    return response, 200 #return response with a success(200) status code

@app.route('/') #Default route decorator
def render_index():
    '''Render index.html'''
    return render_template('index.html') #retunr rendered html

if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 5000) #executes the flask app and deploys it on localhost:5000
