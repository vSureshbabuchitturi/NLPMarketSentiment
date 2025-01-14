# Stock News Sentiment Analysis Application

This project is a Flask-based web application that analyzes the sentiment of stock market news. The application uses the Finnhub API to fetch news articles for a given stock symbol and performs sentiment analysis using the TextBlob library. It provides both a web-based user interface and a programmatic endpoint for analysis.

## Project Structure
```
/NLPMarket
    /templates
        index.html         # HTML form for user input
        result.html        # HTML page to display results
    /src
        nlp_main.py        # Main logic for sentiment analysis
        nlp_flaskapp.py    # Flask app combining backend and frontend
    README.md             # Project documentation
```

## Features
- **User-Friendly Web Interface**: Accepts API key, stock symbol, and date range for analysis.
- **Sentiment Analysis**: Computes polarity of news headlines and summaries using TextBlob.
- **CSV Output**: Saves the analysis results to a CSV file.
- **REST API Endpoint**: Allows programmatic access for sentiment analysis.

## Prerequisites
- Python 3.7+
- Finnhub API key (create one at [Finnhub](https://finnhub.io/))

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository/nlpmarket.git
   cd nlpmarket
   ```

2. Install dependencies:
   ```bash
   pip install flask finnhub-python textblob pandas
   ```

3. Set up the project directory structure as described above.

## Usage

### Running the Application
1. Navigate to the `/src` directory:
   ```bash
   cd /NLPMarket/src
   ```

2. Start the Flask server:
   ```bash
   python nlp_flaskapp.py
   ```

3. Open a browser and visit:
   ```
   http://127.0.0.1:5002/
   ```

4. Enter your API key, stock symbol, and date range in the form, then click "Analyze".

### API Endpoint
You can also interact with the application programmatically:

#### Endpoint
```
POST /analyze
```

#### Request Body
```json
{
  "api_key": "your_finnhub_api_key",
  "symbol": "AAPL",
  "start_date": "2024-01-01",
  "end_date": "2024-01-31"
}
```

#### Curl Example
```bash
curl -X POST http://127.0.0.1:5002/analyze \
-H "Content-Type: application/json" \
-d '{"api_key": "your_api_key", "symbol": "AAPL", "start_date": "2024-01-01", "end_date": "2024-01-31"}'
```

#### Response
```json
{
  "message": "Analysis completed successfully.",
  "output_file": "output/AAPL_news_analysis.csv"
}
```

## Example Output
The output CSV file contains the following columns:
- `id`: News ID
- `headline`: News headline
- `headline_sentiment`: Sentiment polarity of the headline
- `summary`: News summary
- `summary_sentiment`: Sentiment polarity of the summary

## Customization
You can customize the application by modifying the HTML templates or the sentiment analysis logic in `nlp_main.py`.

## Notes
- This is a development server. Do not use it in a production environment.
- Ensure your Finnhub API key has sufficient permissions for the requested data.

## License
This project is licensed under the MIT License.

## Author
Chitturi V Suresh Babu

