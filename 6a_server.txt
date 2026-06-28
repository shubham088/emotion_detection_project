'''
server code to run emotion detection app
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import text_to_analyze

app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def get_text_for_emotion_analysis():
    ''' function to get emotional analysis '''
    txt = request.args.get('textToAnalyze')

    result = text_to_analyze(txt)
    if result['dominant_emotion'] is None:
        print("got None ")
        return "Invalid text! Please try again!.", 200
    return f"""For the given statement , the system response
        is 'anger': {result['anger']} , 'disgust': {result['disgust']},
        'fear': {result['fear']}, 'joy': {result['joy']}
        and 'sadness': {result['sadness']}. The dominant emotion 
        is {result['dominant_emotion']}""", 200

@app.route('/')
def home():
    ''' function to render html '''
    return render_template("index.html", title="Home Page", debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
