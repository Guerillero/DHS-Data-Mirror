import os
import urllib.request
import json
import shutil

def buildFileName(a, b, c):
    return a + " " + b + " " + c + ".zip"

root = "Geospatial Covariates"

fin = urllib.request.urlopen("https://api.dhsprogram.com/rest/dhs/v8/datasets?fileType=GC").read()

jsondata = json.loads(fin.decode())

print()

for fin in os.listdir(os.path.join(root, "_ALL")):
    for dataset in jsondata["Data"]:
        if dataset['FileName'] == fin:
            try: 
                shutil.copy2( os.path.join(root, "_ALL", fin), os.path.join(root, dataset['CountryName'], buildFileName(dataset['CountryName'], dataset['SurveyYear'], dataset['SurveyType']) ) )
            except:
                os.mkdir(os.path.join(root, dataset['CountryName']))
                shutil.copy2( os.path.join(root, "_ALL", fin), os.path.join(root, dataset['CountryName'], buildFileName(dataset['CountryName'], dataset['SurveyYear'], dataset['SurveyType']) ) )
