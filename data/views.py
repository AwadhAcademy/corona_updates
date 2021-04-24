from django.shortcuts import render
import requests
import json
from datetime import date


def start(request):
    data = True
    result = None
    Countries = None
    india = None
    text = 0
    counter = 0
    delhi_data = None
    flag = 0
    server_counter = 0
    # print(final)
    while(data):
        try:
            server_counter += 1
            # state=requests.get('https://api.rootnet.in/covid19-in/stats/latest')
            result = requests.get('https://api.covid19api.com/summary')

            india = requests.get('https://api.covid19india.org/data.json')

            # india1 = india.json()['statewise']
            data = False
        except:
            data = True
        
        
        print(server_counter)
        if(server_counter >= 2):
            data = False
            flag = 1

    # End Data Loding Processs///////////////////////////

    if flag == 1:
        india = json.load(open('india.json'))
        result = json.load(open('world.json'))
    print(india)
        

    india1 = india.json()['statewise']

    result1 = result.json()['Global']
    Countries = result.json()['Countries']
    #    ////////////////// average Counter and calculator

    for i in Countries:
        text = text+i['NewDeaths']
        counter += 1
        average = text/counter

    # /////////////////////// end Of average/////////////

    # ////////////// filtering delhi state data from API
    for i in india1:
        if i['state'] == 'Delhi':
            delhi_data = i
            # //////////////  end filteringfiltering
    return render(request, 'index.html', {'result1': result1, 'Countries': Countries, 'india1': india1, 'average': average, 'delhi_data': delhi_data})
# Create your views here.
