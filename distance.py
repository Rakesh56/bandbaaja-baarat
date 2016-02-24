import json
import requests
#This below function will use distancematrix api and gives the distance in kms from your locality to any place
def finddistance(current_add,city,destination):
    arr=[]
    origin=current_add+' '+city
    destination=destination+' '+city
    for obj in [origin,destination]:
        place=obj.replace(',',' ')
        new=place.replace(' ','+')
        arr.append(new)
    url='https://maps.googleapis.com/maps/api/distancematrix/json?origins='+arr[0]+'&destinations='+arr[1]+'&key=AIzaSyB0Z5xwCsHNYnkA1YSYFePn_qNOQ-R27MM'    
    response=requests.get(url) #accessing data from above url
    json_text=json.loads(response.content) #converting data into json format
    for link in json_text["rows"]:
        for link2 in link["elements"]:
            z=link2["distance"]["text"]
    return(z)
