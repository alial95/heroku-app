from django.shortcuts import render
from .models import AreaNames
import json
from requests import get

def covid_home(request):
    form = AreaNames
    ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"


    structure = {
        "date": "date",
        "name": "areaName",
        "dailyCases": "newCasesByPublishDate",
        "cumulative": "cumCasesByPublishDate",
        "CumulativeDeaths": "cumDeathsByDeathDate",
        'dailyDeaths': 'newDeathsByPublishDate'
        }

    

    
    if request.method == 'POST':
        area_name = request.POST['area_name']

        AREA_TYPE = 'region'
        AREA_NAME = area_name
        filters = [
        f"areaType={ AREA_TYPE }",
        f"areaName={ AREA_NAME }"
        ]
        api_params = {
        "filters": str.join(";", filters),
        "structure": json.dumps(structure, separators=(",", ":")),
        "latestBy": "cumCasesByPublishDate"
    
        }
        response = get(ENDPOINT, params=api_params, timeout=10)
        data = response.json()['data'][0]
        context = {
            'Date': data['date'],
            'Area': data['name'],
            'Cases': data['dailyCases'],
            'TotalCases': data['cumulative'],
            'form': form
        }
    else:
        context = {
            'form': form
        }
        
    return render(request, 'covid_home.html', context)