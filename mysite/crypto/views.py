from django.shortcuts import render
import requests
from json import loads


def home(request):
    # crypto price

    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,EUR,ETH,XRP,LTC,BCH,EOS,ADA,TRX,NEO,ETC,&tsyms=USD")
    price = loads(price_request.content)

    # crypto news.
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")

    api = loads(api_request.content)
    return render(request, 'home.html', {'api': api ,'price' : price})


def prices(request):
    if request.method == "POST":
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        crypto = loads(crypto_request.content)


        return render(request, 'prices.html' , {'quote':quote , 'crypto': crypto})
    else:

     return render(request, 'prices.html', {})

