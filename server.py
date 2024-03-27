from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']
    return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)