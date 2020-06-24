import json
import matplotlib.pyplot as plt
import requests


def covid_live(location="Salford"):
    """Uses latest JSON from data.gov.uk and shows confirmed cases for location from March onwards"""
    json_link = "https://coronavirus.data.gov.uk/downloads/json/coronavirus-cases_latest.json"
    response = requests.get(json_link)
    data = json.loads(response.text)
    for area in data["ltlas"]:
        if area["areaName"]==location:
            print("Date:", area["specimenDate"])
            print("Number of lab confirmed cases:", area["dailyLabConfirmedCases"])
            print("Total number of lab confirmed cases:", area["totalLabConfirmedCases"])
    return


def covid_local(location="Salford"):
    """Uses JSON from local data folder and shows confirmed cases for location from March onwards"""
    with open("data/coronavirus-cases_latest.json", "r") as data_file:
        data = json.load(data_file)
    for area in data["ltlas"]:
        if area["areaName"] == location:
            print("Date:", area["specimenDate"])
            print("Number of lab confirmed cases:", area["dailyLabConfirmedCases"])
            print("Total number of lab confirmed cases:", area["totalLabConfirmedCases"])
    return


def covid_data_download():
    """Downloads latest JSON file from data.gov.uk and saves to data/cornonavirus-cases_latest.json"""
    json_link = "https://coronavirus.data.gov.uk/downloads/json/coronavirus-cases_latest.json"
    response = requests.get(json_link)
    with open("data/coronavirus-cases_latest.json", "w") as data_file:
        json.dump(response.text, data_file)
    return


def covid_list_locations_live():
    """Uses latest JSON from data.gov.uk and shows location names"""
    json_link = "https://coronavirus.data.gov.uk/downloads/json/coronavirus-cases_latest.json"
    response = requests.get(json_link)
    data = json.loads(response.text)
    areas = []
    for area in data["ltlas"]:
        if area['areaName'] not in areas:
            areas.append(area['areaName'])
    areas_sorted = sorted(areas)
    for location in areas_sorted:
        print(location)
    return


def covid_list_locations_local():
    """Uses JSON from local data folder and shows location names"""
    with open("data/coronavirus-cases_latest.json", "r") as data_file:
        data = json.load(data_file)
    areas = []
    for area in data["ltlas"]:
        if area['areaName'] not in areas:
            areas.append(area['areaName'])
    areas_sorted = sorted(areas)
    for location in areas_sorted:
        print(location)
    return


def covid_local_chart(location="Salford"):
    """Uses JSON from local data folder, shows confirmed cases in scatter graph for location from March onwards"""
    with open("data/coronavirus-cases_latest.json", "r") as data_file:
        data = json.load(data_file)
    confirmed_cases = []
    specimen_date = []
    for area in data["ltlas"]:
        if area["areaName"] == location:
            specimen_date.append(area["specimenDate"])
            confirmed_cases.append(area["dailyLabConfirmedCases"])
    plt.scatter(specimen_date, confirmed_cases)
    plt.ylabel('Number of confirmed lab cases')
    plt.xlabel('Date')
    plt.show()
    return


def covid_list_locations_live(location="Salford"):
    """Uses latest JSON from data.gov.uk and shows confirmed cases in scatter graph for location from March onwards"""
    json_link = "https://coronavirus.data.gov.uk/downloads/json/coronavirus-cases_latest.json"
    response = requests.get(json_link)
    data = json.loads(response.text)
    confirmed_cases = []
    specimen_date = []
    for area in data["ltlas"]:
        if area["areaName"] == location:
            specimen_date.append(area["specimenDate"])
            confirmed_cases.append(area["dailyLabConfirmedCases"])
    plt.scatter(specimen_date, confirmed_cases)
    plt.ylabel('Number of confirmed lab cases')
    plt.xlabel('Date')
    plt.show()
    return


covid_local_chart()