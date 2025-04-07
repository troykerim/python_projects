def convert(amount, currency):
    exchange_rates = {
        'EUR': 0.95,    # Euro
        'GBP': 0.82,    # British Pound
        'JPY': 145.6,   # Japanese Yen
        'CAD': 1.43,    # Canadian Dollar
        'AUD': 1.52,    # Australian Dollar
        'INR': 83.16    # Indian Rupee
    }
    return round(amount*exchange_rates.get(currency, 1), 2) 

x = float(input("Enter an amount in USD $: "))
currency = input("Enter currency (EUR, GDP, JPY, CAD, AUD, INR): ").upper()
converted_amount = convert(x, currency)
print(f"{x} USD is equivalent to {converted_amount} {currency}")