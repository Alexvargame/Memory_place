import folium
from django.shortcuts import render,redirect
from . import get_coord


def showmap(request):
    return render(request,'map/showmap.html')

def showpoint(request,lat1,long1):
    figure = folium.Figure()
    lat1,long1=float(lat1),float(long1)
    route=get_coord.get_route(long1,lat1)

    #m = folium.Map(location=[(route['point'][0]),(route['point'][1])],zoom_start=10)
    #m.add_to(figure)
    #folium.PolyLine(route['route'],weight=8,color='blue',opacity=0.6).add_to(m)
    #folium.Marker(location=route['point'], icon=folium.Icon(icon='play', color='green')).add_to(m)
    #folium.Marker(location=route['start_point'],icon=folium.Icon(icon='play', color='green')).add_to(m)
    #folium.Marker(location=route['end_point'],icon=folium.Icon(icon='stop', color='red')).add_to(m)
    #figure.render()
    #context={'map':figure}
    return route['point']
        #render(request,'map/showpoint.html',context)