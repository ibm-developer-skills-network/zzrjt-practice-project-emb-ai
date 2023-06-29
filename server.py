''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
# Import the sentiment_analysis function from the package created

app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sentiment_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output is returned only as the sentiment label
        as received for the function. 
    '''
    # TODO

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    #TODO

if __name__ == "__main__":
    #TODO
