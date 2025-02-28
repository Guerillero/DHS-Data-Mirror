from ParseFileName import FileNameParts
import os
import shutil

root = "Modeled Surfaces"

for fin in os.listdir(os.path.join(root, "_ALL")):
    Country = FileNameParts.DHSCountryCode[fin[:2]]
    if not os.path.isdir(os.path.join(root, Country)):
        os.mkdir(os.path.join(root, Country))
    shutil.copy2(
        os.path.join(root, "_ALL", fin),
        os.path.join(root, Country, Country + " " + fin[2:6] + " " + fin[6:9] + ".zip"),
    )
