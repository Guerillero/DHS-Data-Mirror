import urllib.request
import json
import re
import wget
import os

from ParseFileName import FileNameParts


pubsjson = urllib.request.urlopen(
    "https://api.dhsprogram.com/rest/dhs/publications/ZW"
).read()

pubs = json.loads(pubsjson.decode())

for pub in pubs["Data"]:
    if (
        re.findall(
            "(FR[0-9]+|MIS[0-9]+|AIS[0-9]+|SPA[0-9]+|FRIND[0-9]+)",
            pub["PublicationURL"],
        )
        != []
    ):
        if not os.path.isdir(
            os.path.join(
                "Final Reports", FileNameParts.DHSCountryCode[pub["SurveyId"][:2]]
            )
        ):
            os.mkdir(
                os.path.join(
                    "Final Reports", FileNameParts.DHSCountryCode[pub["SurveyId"][:2]]
                )
            )
        wget.download(
            pub["PublicationURL"],
            os.path.join(
                "Final Reports", FileNameParts.DHSCountryCode[pub["SurveyId"][:2]]
            )
            + "\\"
            + FileNameParts.DHSCountryCode[pub["SurveyId"][:2]]
            + " "
            + pub["SurveyId"][2:6]
            + " "
            + pub["SurveyId"][6:]
            + ".pdf",
        )
