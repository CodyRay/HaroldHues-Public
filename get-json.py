import requests
import json
data = requests.get('http://google.com/complete/search?q=Goo&hl=en')
print data.json() # if response type was set to JSON, then you'll automatically have a JSON response here...
