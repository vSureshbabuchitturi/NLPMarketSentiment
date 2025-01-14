from flask import Flask, request, render_template, jsonify
from textblob import TextBlob
import finnhub
import pandas as pd
import os

app = Flask(__name__, template_folder="../templates")

# Function to process news data
def process_news_data(api_key, symbol, start_date, end_date, output_file):
    # Setup Finnhub client
    finnhub_client = finnhub.Client(api_key=api_key)

    # Fetch company news
    news = finnhub_client.company_news(symbol, _from=start_date, to=end_date)
    news_df = pd.DataFrame(news)

    if news_df.empty:
        raise ValueError("No news data found for the given parameters.")

    # Perform sentiment analysis
    news_df['headline_sentiment'] = news_df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    news_df['summary_sentiment'] = news_df['summary'].apply(lambda x: TextBlob(x).sentiment.polarity)

    # Save to CSV
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    news_df.to_csv(output_file, index=False)

# Flask routes
@app.route("/")
def home():
    # Render the HTML form
    
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    # Get form data
    api_key = request.form.get("api_key")
    symbol = request.form.get("symbol", "AAPL")
    start_date = request.form.get("start_date", "2024-01-01")
    end_date = request.form.get("end_date", "2024-01-31")
    output_dir = "output"
    output_file = os.path.join(output_dir, f"{symbol}_news_analysis.csv")

    try:
        # Process news data
        process_news_data(api_key, symbol, start_date, end_date, output_file)
        # Render the results page
        return render_template("result.html", message="Analysis completed successfully.", output_file=output_file)
    except Exception as e:
        # Render an error message
        return render_template("result.html", message=f"Error: {str(e)}", output_file=None)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
