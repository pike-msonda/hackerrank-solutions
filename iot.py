import requests
import json
BASE_URL = 'https://jsonmock.hackerrank.com'

# conn = http.client.HTTPSConnection(BASE_URL)

def totolNumberOfPages(statusQuery):
    response = requests.get(BASE_URL+'/api/iot_devices/search', params={'status':statusQuery}).json()
    return response['total_pages']
 
def avgRotorSpeed(statusQuery, parentId):
    rotorSpeeds = []
    pageNumber = totolNumberOfPages(statusQuery)
    for p in range(1, pageNumber + 1):
        response = requests.get(BASE_URL+'/api/iot_devices/search', params={'status':statusQuery, 'page' : p}).json()
        print('Page '+ str(p))
        pageNumber = response['total_pages']
        for device in response['data']:
            if device['status'] ==  statusQuery and 'parent' in device and device['parent'] is not None:
                if(device['parent']['id'] == parentId):
                    rotorSpeeds.append(device['operatingParams']['rotorSpeed'])

    try:
        avgSpeed = int(sum(rotorSpeeds) / len(rotorSpeeds))
    except ZeroDivisionError: 
        return int(sum(rotorSpeeds))
    
if __name__ == "__main__":
    
    print(avgRotorSpeed('RUNNING', 7))
