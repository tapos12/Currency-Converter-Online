
This short task implements an online currency converter with a Web API endpoint.

The program accepts four parameters for the /convert endpoint:

- **amount**: the amount to convert
- **src_currency**: ISO currency code for source currency
- **dest_currency**: ISO currency code for destination currency
- **reference_date**: date for the exchange rate in YYYY-MM-DD format.

The output is a json object of **amount** and the **destination currency**.

### File structure
- Dockerfile, to containerize the project
- app.py, main python file
- saved_currency.pickle, saved currency information from the link as a dictionary
- test_converter.py, sample automated test for some functionalities

### Requirements

- Python 3.x 
- Flask framework
- libraries are included in requirements.txt. Please install via `pip install -r requirements.txt`
- Run the `python app.py`
- open on the browser `localhost:5000/convert` (with approapriate parameter
e.g., `localhost:5000/convert?src_currency=GBP&dest_currency=EUR&amount=30&reference_date=2020-03-19`)