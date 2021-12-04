from requests import get, utils


response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)


def currency_rates(forex):

    content = (response.content.decode(encoding=encodings)).split("</Value>")
    for i in content:
        if forex in i:
            print(f"{forex} = {float(i.split('<Value>')[-1].replace(',', '.'))}")


forex = (input('Введите код валюты: ')).upper()
currency_rates(forex)
