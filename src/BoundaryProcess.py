import os
import re
import shutil

root = "Boundaries"

for fin in os.listdir(os.path.join(root, "_ALL")):
    parse = re.findall('\A.+\d{4}\s[A-Z]{3}', fin)
    #surveyType = parse[0][-3:]
    #year = parse[0][-8:-4]
    country = parse[0][:-9]
    folder = os.path.join(root, country)
    try: 
        shutil.copy2( os.path.join(root, "raw", fin), os.path.join(root, country, parse[0] + ".zip") )
    except:
        os.mkdir(os.path.join(root, country))
        shutil.copy2( os.path.join(root, "raw", fin), os.path.join(root, country, parse[0] + ".zip") )
