#  CURRENCY CONVERTER
rates = {
    'USD': 1.0,
    'EUR': 0.25,
    'GBP': 0.35,
    'NGN': 200
}

while True:   
    from_currency = input('Enter the currency you want to convert from ( USD, EUR, GBP, NGN): ').strip().upper()
    if from_currency in rates:
        break
    else:
        print('Invalid currency please input a valid currency')

while True:
    to_currency = input('Enter the currency you want to convert to ( USD, EUR, GBP, NGN): ').strip().upper()
    if to_currency in rates:
        break
    else:
        print('Invalid currency please input a valid currency')
amount = float(input('Enter an amount'))

usd_amount = amount / rates[from_currency]
converted_amount = usd_amount * rates [to_currency]
print (f'{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}')