from django.shortcuts import render
import json
from requests import get
ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"

AREA_TYPE = "region"
AREA_NAME = 'West Midlands'

filters = [
    f"areaType={ AREA_TYPE }",
    f"areaName={ AREA_NAME }"
]


structure = {
    "date": "date",
    "name": "areaName",
    "dailyCases": "newCasesByPublishDate",
    "cumulative": "cumCasesByPublishDate",
    "CumulativeDeaths": "cumDeathsByDeathDate",
    'dailyDeaths': 'newDeathsByPublishDate'
    }

api_params = {
    "filters": str.join(";", filters),
    "structure": json.dumps(structure, separators=(",", ":"))
   
}

response = get(ENDPOINT, params=api_params, timeout=10)
data = response.json()['data']
# Create your views here.
def covid_home(request):
    ENDPOINT = "https://api.coronavirus.data.gov.uk/v1/data"

    AREA_TYPE = area_type
    AREA_NAME = area_name

    filters = [
        f"areaType={ AREA_TYPE }",
        f"areaName={ AREA_NAME }"
    ]


    structure = {
        "date": "date",
        "name": "areaName",
        "dailyCases": "newCasesByPublishDate",
        "cumulative": "cumCasesByPublishDate",
        "CumulativeDeaths": "cumDeathsByDeathDate",
        'dailyDeaths': 'newDeathsByPublishDate'
        }

    api_params = {
        "filters": str.join(";", filters),
        "structure": json.dumps(structure, separators=(",", ":"))
    
    }

    response = get(ENDPOINT, params=api_params, timeout=10)
    data = response.json()['data']
    if request.method == 'POST':
        region = request.POST['region']
    return render(request, 'covid_home.html',)