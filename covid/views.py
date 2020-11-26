from django.shortcuts import render
from .models import AreaNames
from .forms import AreaForm
import json
from requests import get
import io
import base64, urllib
from matplotlib import pyplot as plt


def covid_home(request):

    def make_graph():
        # fig, ax = plt.subplots()
        # x = [1, 2, 3, 4, 5]
        # y1 = [4, 5, 6, 7, 8]
        # y2 = [5, 6, 7, 8, 9]
        # # y = np.vstack((y1, y2))
        # labels = ['x', 'y']
        # ax.stackplot(x, y1, y2, labels=labels)
        plt.plot(range(100))
        fig = plt.gcf()
        buf = io.BytesIO()
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)
        return uri
    form = AreaForm
    uri = make_graph()
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
        area_id = request.POST['model_choice']
        area_name = AreaNames.objects.get(pk=area_id)
        # area_name = form.objects.get(pk=request.POST['area_name'])

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
            'form': form,
            'data': uri
        }
    else:
        context = {
            'form': form,
            'data': uri
        }
        
    return render(request, 'covid_home.html', context)