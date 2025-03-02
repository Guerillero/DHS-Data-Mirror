import wget
import os
import urllib.request

root = "Analytical Reports"
errorList = []

os.mkdir(root)

reportTypes = [
    {"short": "AS", "long": "Analytical Studies", "count": 89},
    {"short": "CR", "long": "Comparative Reports", "count": 52},
    {"short": "FA", "long": "Further Analysis", "count": 157},
    {"short": "MR", "long": "Methodological Reports", "count": 36},
    {"short": "NUT", "long": "Nutrition Reports", "count": 6},
    {"short": "OP", "long": "Occasional Papers", "count": 14},
    {"short": "QRS", "long": "Qualitative Research Studies", "count": 25},
    {"short": "TR", "long": "Trend Reports", "count": 8},
    {"short": "WP", "long": "Working Papers", "count": 201},
]

for report in reportTypes:
    os.mkdir(os.path.join(root, report["long"]))
    for i in range(1, report["count"]):
        reportSlug = report["short"] + str(i)
        print(reportSlug)
        try:
            a = urllib.request.urlopen(
                "https://www.dhsprogram.com/pubs/pdf/"
                + reportSlug
                + "/"
                + reportSlug
                + ".pdf"
            ).read()
            wget.download(
                "https://www.dhsprogram.com/pubs/pdf/"
                + reportSlug
                + "/"
                + reportSlug
                + ".pdf",
                os.path.join(root, report["long"], reportSlug + ".pdf"),
            )
        except:
            errorList += [reportSlug]

fout = open("src\\errors.txt", "w")
for error in errorList:
    fout.write(error)
