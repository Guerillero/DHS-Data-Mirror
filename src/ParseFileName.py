class FileNameParts:
    FileType = {
        "AI": "Accidents and Injuries Recode",
        "BR": "Births Recode",
        "CR": "Couples' Recode",
        "GR": "Pregnancies Recode",
        "HR": "Household Recode",
        "IR": "Individual Recode",
        "KR": "Children's Recode",
        "MR": "Men's Recode",
        "NR": "Pregnancy and Postnatal Care Recode",
        "PR": "Household Member Recode",
        "SR": "Siblings Recode",
        "XR": "Child Under 5 Recode",
        "AH": "Adult Health",
        "BQ": "Births Raw",
        "CH": "Children's Raw",
        "CP": "Couples' Raw",
        "EX": "Experimental",
        "FW": "Fieldworker Questionnaire",
        "HH": "Household Raw",
        "HW": "Height and Weight Scores",
        "ID": "In-depth",
        "IH": "Individual Household Raw",
        "IQ": "Individual Raw",
        "ML": "Men's Raw",
        "OD": "Other Data",
        "PQ": "Household Member Raw",
        "SM": "Safe Motherhood",
        "SQ": "Service Availability Raw",
        "VA": "Verbal Autopsy",
        "WI": "Wealth Index",
        "WS": "Women's Status",
        "XP": "Expenditure",
        "AR": "HIV Test Results Recode",
        "HT": "HIV Test Results Raw",
        "OB": "Other Biomarkers",
        "GC": "Geospatial Covariates",
        "GE": "Geographic Data",
        "AN": "Antenatal Care",
        "AT": "ART",
        "CL": "Unit Check List",
        "CN": "Consultations",
        "CS": "Country Specific",
        "CT": "VCT",
        "FC": "Facility",
        "FP": "Family Planning",
        "IN": "Safe Injection",
        "IP": "Inpatient Unit",
        "LB": "Laboratory",
        "LD": "Labor Delivery",
        "MS": "Health Information System",
        "OI": "Outpatient inpatient",
        "OP": "Outpatient Unit",
        "PH": "Pharmacy",
        "PI": "Personal Interview",
        "PM": "PMTCT",
        "PV": "Provider",
        "SC": "Sick Child",
        "SI": "Sexually Transmitted Infections",
        "SL": "Staff Provider Listing",
        "TB": "TB data",
        "CO": "Community",
        "VR": "Village Recode",
    }

    DHSCountryCode = {
        "AF": "Afghanistan",
        "LB": "Liberia",
        "AL": "Albania",
        "MD": "Madagascar",
        "AO": "Angola",
        "MW": "Malawi",
        "AM": "Armenia",
        "MV": "Maldives",
        "AZ": "Azerbaijan",
        "ML": "Mali",
        "BD": "Bangladesh",
        "MR": "Mauritania",
        "BJ": "Benin",
        "MX": "Mexico",
        "BO": "Bolivia",
        "MB": "Moldova",
        "BT": "Botswana",
        "MA": "Morocco",
        "BR": "Brazil",
        "MZ": "Mozambique",
        "BF": "Burkina Faso",
        "MM": "Myanmar",
        "BU": "Burundi",
        "NM": "Namibia",
        "KH": "Cambodia",
        "NP": "Nepal",
        "CM": "Cameroon",
        "NC": "Nicaragua",
        "CV": "Cape Verde",
        "NI": "Niger",
        "CF": "Central African Republic",
        "NG": "Nigeria",
        "TD": "Chad",
        "OS": "Nigeria (Ondo State)",
        "CO": "Colombia",
        "PK": "Pakistan",
        "KM": "Comoros",
        "PY": "Paraguay",
        "CG": "Congo",
        "PE": "Peru",
        "CD": "Congo Democratic Republic",
        "PH": "Philippines",
        "CI": "Cote d'Ivoire",
        "RW": "Rwanda",
        "DR": "Dominican Republic",
        "WS": "Samoa",
        "EC": "Ecuador",
        "ST": "Sao Tome and Principe",
        "EG": "Egypt",
        "SN": "Senegal",
        "ES": "El Salvador",
        "SL": "Sierra Leone",
        "EK": "Equatorial Guinea",
        "ZA": "South Africa",
        "ER": "Eritrea",
        "LK": "Sri Lanka",
        "ET": "Ethiopia",
        "SD": "Sudan",
        "GA": "Gabon",
        "SZ": "Swaziland",
        "GM": "Gambia",
        "TJ": "Tajikistan",
        "GH": "Ghana",
        "TZ": "Tanzania",
        "GU": "Guatemala",
        "TH": "Thailand",
        "GN": "Guinea",
        "TL": "Timor-Leste",
        "GY": "Guyana",
        "TG": "Togo",
        "HT": "Haiti",
        "TT": "Trinidad and Tobago",
        "HN": "Honduras",
        "TN": "Tunisia",
        "IA": "India",
        "TR": "Turkey",
        "ID": "Indonesia",
        "TM": "Turkmenistan",
        "JO": "Jordan",
        "UG": "Uganda",
        "KK": "Kazakhstan",
        "UA": "Ukraine",
        "KE": "Kenya",
        "UZ": "Uzbekistan",
        "KY": "Kyrgyz Republic",
        "VN": "Vietnam",
        "LA": "Lao People's Democratic Republic",
        "YE": "Yemen",
        "LS": "Lesotho",
        "ZM": "Zambia",
        "ZW": "Zimbabwe",
        "PG": "Papua New Guinea",
    }

    FileFormat = {"FL": "Flat", "SV": "SPSS", "DT": "Stata", "SD": "SAS"}


def FileVersion(FileName):
    Code = FileName[4:6]
    output = {"Phase": int(Code[:1]), "Release": "NaN"}
    if Code[1:] in "0123456789":
        output["Release"] = int(Code[1:])
    else:
        if Code[1:] == "H" or Code[1:] == "Q" or Code[1:] == "Z":
            output["Release"] = 0
        elif Code[1:] == "A" or Code[1:] == "I" or Code[1:] == "R":
            output["Release"] = 1
        elif Code[1:] == "B" or Code[1:] == "J" or Code[1:] == "S":
            output["Release"] = 2
        elif Code[1:] == "C" or Code[1:] == "K" or Code[1:] == "T":
            output["Release"] = 3
        elif Code[1:] == "D" or Code[1:] == "L" or Code[1:] == "U":
            output["Release"] = 4
        elif Code[1:] == "E" or Code[1:] == "M" or Code[1:] == "V":
            output["Release"] = 5
        elif Code[1:] == "F" or Code[1:] == "N" or Code[1:] == "W":
            output["Release"] = 6
        elif Code[1:] == "G" or Code[1:] == "O" or Code[1:] == "X":
            output["Release"] = 7
        elif Code[1:] == "H" or Code[1:] == "P" or Code[1:] == "Y":
            output["Release"] = 8
    return output


def Parse(FileName):
    output = {}
    output["Country"] = FileNameParts.DHSCountryCode[FileName[:2]]
    output["Type"] = FileNameParts.FileType[FileName[2:4]]
    output["Phase"] = FileVersion(FileName)["Phase"]
    output["Release"] = FileVersion(FileName)["Release"]
    output["Format"] = FileNameParts.FileFormat[FileName[6:8]]
    if len(FileName.split(".")[0]) == 10:
        if FileName[8:10] == "SP":
            output["DataStructure"] = "SPA Raw Data"
        elif FileName[8:10] == "SR":
            output["DataStructure"] = "SPA Recode Data"
    return output
