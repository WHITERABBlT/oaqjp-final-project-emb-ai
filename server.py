''' 
Executing this function initiates the application of emotion
analysis to be executed over the Flask channel and deployed on
localhost:5000.
'''
# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    ''' 
    This code receives the text from the HTML interface and 
    runs emotion analysis over it using emotion_detector() function. 
    The output returned shows the emotion scores and 
    the dominant emotion for the provided text.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    output = emotion_detector(text_to_analyze)

    if output['dominant_emotion'] is None:
        return "<b>Invalid text! Please try again!</b>"
    
    return (
    f"For the given statement, the system response is "
    f"'anger': {output['anger']}, 'disgust': {output['disgust']}, "
    f"'fear': {output['fear']}, 'joy': {output['joy']} and 'sadness': {output['sadness']}. "
    f"The dominant emotion is <b>{output['dominant_emotion']}</b>.")
    
@app.route("/")
def render_index_page():
    ''' 
    This function initiates the rendering of the main application
    page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
    