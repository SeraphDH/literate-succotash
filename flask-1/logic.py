from flask import flash, session
from forex_python.converter import CurrencyRates, CurrencyCodes

def Logic(ConvertFrom, ConvertTo, Ammount):
    cc = CurrencyCodes()
    cr = CurrencyRates()
    Proceed = True

    if cc.get_currency_name(ConvertFrom) == None:
        flash(f'{ConvertFrom} is not a valid currency.')
        Proceed = False
    if cc.get_currency_name(ConvertTo) == None:
        flash(f'{ConvertTo} is not a valid conversion.')
        Proceed = False
    if not Ammount.isdecimal():
        flash(f'{Ammount} is not a valid amount.')
        Proceed = False
    if not Proceed:
        return        
    s = cc.get_symbol(ConvertTo)
            
    Conversion = cr.convert(ConvertFrom, ConvertTo, float(Ammount))
    session['Conversion'] = Conversion
    session['s'] = s
    return True