# Currency Converter CLI

A command-line tool that converts an amount from one currency to another using live exchange rates from the [Frankfurter API](https://frankfurter.dev/).

> Status: in development (v1)

## Usage

```
python converter.py <amount> <from_currency> <to_currency>
```

Example:

```
python converter.py 100 USD EGP
```

Output:

```
100 USD = 5285.10 EGP
```

## How it works

- Input is read from the command line (`sys.argv`).
- The tool fetches the current exchange rate from the Frankfurter API (no API key required).
- The conversion is calculated locally: `amount * rate`.

## Error handling

| Case | Message |
|---|---|
| Missing arguments | `Usage: python converter.py <amount> <from> <to>` |
| Amount is not a number | `Amount must be a number.` |
| Amount is negative | `Amount must be positive.` |
| Invalid currency code | `Invalid currency: <code>. Please enter a valid currency code.` |
| No internet or API unreachable | `Could not connect to the exchange rate service. Check your internet connection and try again.` |

## Roadmap

- v1: single conversion with error handling
- v2: automated tests
- v3: save conversion history / cache rates

## Data source

Exchange rates provided by [Frankfurter](https://frankfurter.dev/).