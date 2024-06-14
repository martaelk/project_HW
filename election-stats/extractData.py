import requests

def getPollingStationData():
    response = requests.get('https://data.gov.lv/dati/dataset/c5cc30b1-0dce-403b-a0b2-370defe4de6d/resource/e9bd1c65-8cb7-4216-8e82-c5db8eca88e4/download/locations.json')
    data =  response.json()
    return data    

def getCandidates():
    response = requests.get('https://data.gov.lv/dati/dataset/c5cc30b1-0dce-403b-a0b2-370defe4de6d/resource/bde3f657-959d-4bd3-9c52-fdb1539f1a40/download/candidates.json')
    data =  response.json()
    return data

def getPartyData():
    response = requests.get('https://data.gov.lv/dati/dataset/c5cc30b1-0dce-403b-a0b2-370defe4de6d/resource/f416c669-c702-4f8c-95c7-2811301146a7/download/candidatelists.json')
    data =  response.json()
    return data
   
def getElectedCandiateData():
    response = requests.get('https://data.gov.lv/dati/dataset/c5cc30b1-0dce-403b-a0b2-370defe4de6d/resource/02a08965-01d3-4c83-b1b5-a1e736f91cca/download/elected.json')
    data =  response.json()
    return data

def getCandidateDemographicData():
    response = requests.get('https://data.gov.lv/dati/dataset/c5cc30b1-0dce-403b-a0b2-370defe4de6d/resource/3d67a4d0-f29b-4a8d-b962-c06df12190f6/download/candidatesstatistic.json')
    data =  response.json()
    return data
