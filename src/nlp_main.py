# main_code.py
import os
import finnhub
import pandas as pd
from textblob import TextBlob
#pip install finnhub-python
#pip show finnhub-python
#pip install textblob
#pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("FINNHUB_API_KEY")


def fetch_company_news(api_key, symbol, start_date, end_date):
    """Fetch company news data using Finnhub API."""
    finnhub_client = finnhub.Client(api_key=api_key)
    news = finnhub_client.company_news(symbol, _from=start_date, to=end_date)
    return pd.DataFrame(news)

def analyze_sentiment(dataframe):
    """Perform sentiment analysis on news headlines and summaries."""
    dataframe['headline_sentiment'] = dataframe['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    dataframe['summary_sentiment'] = dataframe['summary'].apply(lambda x: TextBlob(x).sentiment.polarity)
    return dataframe

def save_to_csv(dataframe, file_path):
    """Save the processed data to a CSV file."""
    dataframe.to_csv(file_path, index=False)

def process_news_data(api_key, symbol, start_date, end_date, output_file):
    """Fetch, analyze, and save company news data."""
    news_df = fetch_company_news(api_key, symbol, start_date, end_date)
    analyzed_df = analyze_sentiment(news_df)
    save_to_csv(analyzed_df, output_file)