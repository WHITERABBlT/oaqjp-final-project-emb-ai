''' 
Executing this function initiates the application of emotion
analysis to be executed over the Flask channel and deployed on
localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_analyzer():
    ''' 
    This code receives the text from the HTML interface and 
    runs emotion analysis over it using emotion_detector()
    function. The output returned shows the emotion scores and the dominant emotion 
    for the provided text.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    output = emotion_detector(text_to_analyze)
    return f"For the given statement, the system response is {output[0:4]}. The dominant emotion is {output['dominant_emotion']}."

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)