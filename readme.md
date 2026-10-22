# Currency Converter CLI

A simple command-line tool that converts an amount from one currency to another using live exchange rates from the [Frankfurter API](https://frankfurter.dev/). No API key required.

## Features

- Live exchange rates
- Input validation (amount must be a valid, non-negative number)
- Clear error messages for invalid currencies, network problems and service errors
- Request timeout so the tool never hangs
- Unit tests with pytest

## Requirements

- Python 3.9+
- Packages listed in `requirements.txt`

## Installation

```
git clone https://github.com/Kekoo0/currency-converter.git
cd currency-converter
pip install -r requirements.txt
```

## Usage

```
python converter.py <amount> <from> <to>
```

Currency codes are case-insensitive.

Example:

```
python converter.py 100 usd egp
```

Output (the rate changes over time):

```
100.0 USD = 5336.70 EGP
```

## Error handling

| Case | Message |
|---|---|
| Wrong number of arguments | `Usage: python converter.py <amount> <from> <to>` |
| Amount is not a number | `Amount must be a number.` |
| Amount is negative | `Amount must be positive.` |
| Unknown currency code | `Invalid currency: <to> or <from>. Please enter a valid currency code.` |
| No internet connection or request timeout | `Could not connect to the exchange rate service. Check your internet connection and try again.` |
| Other API error | `Could not connect to the exchange rate service` |

## Running the tests

```
python -m pytest
```

Currently the tests cover the `convert` function. More tests are planned.

## Roadmap

- [x] v1: single conversion with validation and error handling
- [ ] More tests for argument validation and rate fetching
- [ ] v2: save conversion history to a CSV file

## Data source

Exchange rates are provided by [Frankfurter](https://frankfurter.dev/).