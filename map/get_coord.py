import requests
import json
import polyline
import folium


def get_route(pickup_lon, pickup_lat):

    loc = "{},{};{},{}".format(pickup_lon, pickup_lat,pickup_lon, pickup_lat)
    url = "http://router.project-osrm.org/route/v1/driving/"
    r = requests.get(url + loc)
    if r.status_code != 200:
        return {}
    res = r.json()
    #routes = polyline.decode(res['routes'][0]['geometry'])
    point = [res['waypoints'][0]['location'][1], res['waypoints'][0]['location'][0]]
    #start_point = [res['waypoints'][0]['location'][1], res['waypoints'][0]['location'][0]]
    #end_point = [res['waypoints'][1]['location'][1], res['waypoints'][1]['location'][0]]
    #distance = res['routes'][0]['distance']
    print(res)
    print(point)
    out = {#'route': routes,
           'point':point
           #'start_point': start_point,
           #'end_point': end_point,
           #'distance': distance
           }

    return out
