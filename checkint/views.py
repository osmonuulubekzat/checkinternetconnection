from django.shortcuts import render
from urllib import request
import requests


# Create your views here.
def Index(request):
    text = ""

    def connected_to_internet(url='http://www.google.com/', timeout=5):
        try:
            _ = requests.head(url, timeout=timeout)
            return "yes internet"
        except requests.ConnectionError:
            return "No internet connection available"

    text = connected_to_internet()
    context = {"context": text}
    return render(request, "index.html", context)
