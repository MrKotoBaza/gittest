import requests

def unpack(dikt, tabs):
    tabs_s = "\t"*tabs
    for i in dikt.keys():
        if type(dikt[i]) is dict:
        
            print(f"{tabs_s}{i} : {dikt[i]}")
        else:
            print(f"{tabs_s}{i} :")
            print("started")
            unpack(dikt[i], tabs+1)

resp = requests.get("https://api.github.com/search/repositories", params = {'q':"requests+language:python"})

jsoned = resp.json()

repository = jsoned['items'][0]



unpack(repository, 0)