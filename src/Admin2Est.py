import os
import urllib.request
import json
import shutil

def buildFileName(a, b, c):
    return a + " " + b + " " + c + ".zip"

root = "Admin 2 Estimates"

CountryInfoAPI = urllib.request.urlopen("https://api.dhsprogram.com/rest/dhs/countries").read()

countrydata = json.loads(CountryInfoAPI.decode())

for fin in os.listdir(os.path.join(root, "_ALL")):
    for country in countrydata["Data"]:
        if country["DHS_CountryCode"] == fin[:2]:
            try: 
                shutil.copy2( os.path.join(root, "_ALL", fin), os.path.join(root, country['CountryName'], buildFileName(country['CountryName'], fin[6:10], fin[3:6]) ) )
            except:
                os.mkdir(os.path.join(root, country['CountryName']))
                shutil.copy2( os.path.join(root, "_ALL", fin), os.path.join(root, country['CountryName'], buildFileName(country['CountryName'], fin[5:9], fin[2:5])) )