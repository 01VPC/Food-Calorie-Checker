from django.shortcuts import render
import json
import requests

# Create your views here.
def home(request):
    
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': 'P0kwMuYxOx6asTfwq8IsPA==cLIiFqly8UafATmy'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
            if api is None:
                flag = True
            else:
                flag = False
        except Exception as e:
            api = "Oops! There was an error"
            print(e)
            flag = True  # Set flag to True in case of an error
        return render(request, 'home.html', {'api': api, 'query': query})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})
