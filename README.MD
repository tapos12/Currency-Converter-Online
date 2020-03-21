This short task implements an online currency converter with a Web API endpoint.

The program accepts four parameters for the /convert endpoint:

- amount: the amount to convert
- src_currency: ISO currency code for source currency
- dest_currency: ISO currency code for destination currency
- referce_date: date for the exchange rate in YYYY-MM-DD format.

The output is a json object of amount and the destination currency.

### Requirements

- Python 3.x 
- Flask framework
- libraries are included in requirements.txt. Please install via pip install requirements.txt -r
- Run the app.py
- open on the browser localhost:5000/convert