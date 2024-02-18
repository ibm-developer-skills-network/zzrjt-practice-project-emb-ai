import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        test_1 = "I love working with Python"
        intended_result_1 = "SENT_POSITIVE"
        test_2 = "I hate working with Pyhton"
        intended_result_2 = "SENT_NEGATIVE"
        test_3 = "I am neutral on Python"
        intended_result_3 = "SENT_NEUTRAL"

        result_1 = sentiment_analyzer(test_1)
        result_2 = sentiment_analyzer(test_2)
        result_3 = sentiment_analyzer(test_3)

        self.assertAlmostEqual(result_1["label"], intended_result_1)
        self.assertAlmostEqual(result_2["label"], intended_result_2)
        self.assertAlmostEqual(result_3["label"], intended_result_3)

unittest.main()