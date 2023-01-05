from django.shortcuts import render , HttpResponse
import folium
from folium import plugins
import pandas as pd
import ipywidgets
import os
import json
from IPython.display import display
import datetime

from base.models import House, ways

# Create your views here.
def index(request):
    return render(request , "index.html")
    # return HttpResponse('<h1>this is the home page</h1>')

def about(request):
    return HttpResponse('<h1>this is About Page</h1>')

def services(request):
    return HttpResponse('<h1>this is Services Page</h1>')

def product(request):
    return HttpResponse('<h1>this is Product Page</h1>')

def choose(request):
    context = {
        'Haus' : ['' , 'Haus1' , 'Haus2' ,'Haus3' ,'Haus4' ,'Haus5' ,'Haus6' ,'Haus7' ,'Haus8' ,'Haus9' ,'Haus10' ,'Haus11' ,'Haus12' ,'Haus13' ,'Haus14' ,'Haus15' ,'Haus16' ,'Haus17' ,'Haus18' ,'Haus19' ,'Haus20' ,'Haus21' ,'Haus22' ,'Haus23' ,'Haus24' ,'Haus25' ,'Haus26' ,'Haus27' ,'Haus28' ,'Haus29' ,'Haus30' ,'Haus31' ,'Haus32' ,'Haus33' ,'Haus34' ,'Haus35' ,'Haus36' ,'Haus37' ,'Haus38' ,'Haus39' ,'Haus40' ,'Haus41' ,'Haus42' ,'Haus43' ]
    }
    return render(request , 'path_choose_page.html' , context)

def show_map(request):   
    print('*************************')
    Haus = request.GET.get('Haus')
    print(Haus)
    print('*************************')
    # context = {}
    #creation of map comes here + business logic , stack overflow main code 
    # m = folium.Map([19.234095,72.990364], zoom_start=18)
    # test = folium.Html('<b>Hello world</b>', script=True)
    # popup = folium.Popup(test, max_width=2650)
    # folium.RegularPolygonMarker(location=[51.5, -0.25], popup=popup).add_to(m)
    # m=m._repr_html_() #updated
    # context = {'my_map': m}
    # the latitude and Longitude coordinates


    # hauseOutline = 'HospitalNavigator/GeoResources/Haus22.geojson'
    # display(folium.GeoJson(hauseOutline, name="Haus22").add_to(map_UMM))


    # for houses , code from jupyter notebook
    # UMMlocation = (19.2007634168898,72.98231011452688)
    # map_UMM = folium.Map(location = UMMlocation, width = "75%", zoom_start = 17) # max zoom: 18
    # test = folium.Html('<b>Hello world</b>', script=True)
    # hauseOutline = 'maps/GeoResources/Haus13.geojson'
    # folium.GeoJson(hauseOutline, name="Haus13").add_to(map_UMM)
    # map_UMM=map_UMM._repr_html_() #updated
    # context = {'my_map': map_UMM}


    # for path 
    # UMMlocation = (19.2007634168898,72.98231011452688)
    # map_UMM = folium.Map(location = UMMlocation, width = "75%", zoom_start = 17) # max zoom: 18
    # test = folium.Html('<b>Hello world</b>', script=True)
    # hauseOutline = 'maps/GeoResources/path/w13.geojson'
    # folium.GeoJson(hauseOutline, name="w13").add_to(map_UMM)
    # map_UMM=map_UMM._repr_html_() #updated
    # context = {'my_map': map_UMM}
    
    class navigator:
        def __init__(self):
            self.geoResources = {}
            self.hospitalLocation =(19.197458724095526, 72.98346780904069)
            self.position = 'w'
            self.destination = 'Haus17'

            # obj = {}
            for i in House.objects.all():
                key = 'Haus' + str(i.id)
                self.geoResources[key] = i.des

            for j in ways.objects.all():
                key = 'w' +  str(j.id)
                self.geoResources[key] = j.way

            self.redrawMap()

        def changeDestination(self,newDestination):
            self.destination = newDestination
            self.redrawMap()

        def changeStartPoint(self, newStartPoint):
            
            #self.position = newStartPoint #does not work yet
            print(f'Selected Start: {newStartPoint}; Selected Target: {self.destination}')
            #self.redrawMap()
            

        def drawPathWay(self,hospitalMap):
        
            def switchPosition(coordinate):
                temp = coordinate[0]
                coordinate[0] = coordinate[1]
                coordinate[1] = temp
                return coordinate

            searchString = self.position + self.destination.split('Haus')[1]
            testWay = self.geoResources[searchString]
            for feature in testWay['features']:
                path = feature['geometry']['coordinates']

            finalPath = list(map(switchPosition,path))
            folium.plugins.AntPath(finalPath).add_to(hospitalMap)

        def drawBuilding(self,hospitalMap):
            hauseOutline = self.geoResources[self.destination]
            folium.GeoJson(hauseOutline, name="geojson").add_to(hospitalMap)

        def redrawMap(self):
            #print(f'position {self.position}, destination {self.destination}')
            hospitalMap = folium.Map(location = self.hospitalLocation, width = "75%", zoom_start = 17)
            self.drawPathWay(hospitalMap)
            self.drawBuilding(hospitalMap)
            hospitalMap.save('./templates/show_folium_map.html')

    myNavigator = navigator()
    def displayWay(whereTo):
        myNavigator.changeDestination(whereTo)
    def changePosition(whereFrom):
        myNavigator.changeStartPoint(whereFrom)

        # Destination Selector
    selectHouse_widget=ipywidgets.Select(
        
    options=['Haus1',
        'Haus10',
        'Haus11',
        'Haus12',
        'Haus13',
        'Haus14',
        'Haus15',
        'Haus16',
        'Haus17',
        'Haus18',
        'Haus19',
        'Haus2',
        'Haus20',
        'Haus22',
        'Haus24',
        'Haus25',
        'Haus26',
        'Haus27',
        'Haus28',
        'Haus29',
        'Haus3',
        'Haus30',
        'Haus31',
        'Haus32',
        'Haus33',
        'Haus34',
        'Haus35',
        'Haus36',
        'Haus37',
        'Haus39',
        'Haus4',
        'Haus40',
        'Haus41',
        'Haus42',
        'Haus43',
        'Haus5',
        'Haus6',
        'Haus7',
        'Haus8',
        'Haus9'],
        value=Haus,
        description='Target',
        disabled=False)

    # widget function
    def selectHouse(way):
        if way == 'Haus1' :
            displayWay('Haus1' ) 
        if way == 'Haus10':
            displayWay('Haus10')
        if way == 'Haus11':
            displayWay('Haus11')
        if way == 'Haus12':
            displayWay('Haus12')
        if way == 'Haus13':
            displayWay('Haus13')
        if way == 'Haus14':
            displayWay('Haus14')
        if way == 'Haus15':
            displayWay('Haus15')
        if way == 'Haus16':
            displayWay('Haus16')
        if way == 'Haus17':
            displayWay('Haus17')
        if way == 'Haus19':
            displayWay('Haus19')
        if way == 'Haus2' :
            displayWay('Haus2' ) 
        if way == 'Haus20':
            displayWay('Haus20')
        if way == 'Haus22':
            displayWay('Haus22')
        if way == 'Haus24':
            displayWay('Haus24')
        if way == 'Haus25':
            displayWay('Haus25')
        if way == 'Haus26':
            displayWay('Haus26')
        if way == 'Haus27':
            displayWay('Haus27')
        if way == 'Haus28':
            displayWay('Haus28')
        if way == 'Haus29':
            displayWay('Haus29')
        if way == 'Haus3' :
            displayWay('Haus3' ) 
        if way == 'Haus30':
            displayWay('Haus30')
        if way == 'Haus31':
            displayWay('Haus31')
        if way == 'Haus32':
            displayWay('Haus32')
        if way == 'Haus33':
            displayWay('Haus33')
        if way == 'Haus34':
            displayWay('Haus34')
        if way == 'Haus35':
            displayWay('Haus35')
        if way == 'Haus36':
            displayWay('Haus36')
        if way == 'Haus37':
            displayWay('Haus37')
        if way == 'Haus39':
            displayWay('Haus39')
        if way == 'Haus4' :
            displayWay('Haus4' ) 
        if way == 'Haus40':
            displayWay('Haus40')
        if way == 'Haus41':
            displayWay('Haus41')
        if way == 'Haus42':
            displayWay('Haus42')
        if way == 'Haus43':
            displayWay('Haus43')
        if way == 'Haus5' :
            displayWay('Haus5' ) 
        if way == 'Haus6' :
            displayWay('Haus6' ) 
        if way == 'Haus7' :
            displayWay('Haus7' ) 
        if way == 'Haus8' :
            displayWay('Haus8' ) 
        if way == 'Haus9' :
            displayWay('Haus9' ) 

    # Position Selector
    selectPosition_widget=ipywidgets.Select(
        options=['Aufnahme', 'Eingang West', 'Eingang Ost', 'Eingang Fahrzeuge'],
        value='Eingang West',
        description='Start',
        disabled=False)

    def selectPosition(position):
        if position == 'Aufnahme':
            changePosition('a')
        if position == 'Eingang West':
            changePosition('w')
        if position == 'Eingang Ost':
            changePosition('o')
        if position == 'Eingang Fahrzeuge':
            changePosition('f')
            
    #Initialization   
    ipywidgets.interact(selectPosition, position=selectPosition_widget)
    ipywidgets.interact(selectHouse, way=selectHouse_widget)

    return render(request, 'show_folium_map.html')