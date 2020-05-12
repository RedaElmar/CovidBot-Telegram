import requests


def casesapi():
    url = "https://moroccostats.herokuapp.com/stats/coronavirus/countries/morocco"
    my_json = requests.get(url).json()
    return (" عدد الحالات " + my_json['totalcases'] + " ماتو" + my_json[
        'totaldeaths'] + " الله يرحمهم " + " وتشافاو الحمد لله" + my_json['recovered'])


# print(casesapi())
"""
def casesperregion(city):
    url = "https://moroccostats.herokuapp.com/stats/coronavirus/countries/morocco/regions"
    response = requests.request("GET", url)
    my_json=json.loads(response.text)
    print("CasaSettat: ", my_json['CasaSettat'])
    print("RabatSalKenitra: ", my_json['RabatSalKenitra'])
    print("MarrakechSafi: ", my_json['MarrakechSafi'])
    print("Fsmeknes: ", my_json['Fsmeknes'])
    print("TangerTetouanAlHoceima: ", my_json['TangerTetouanAlHoceima'])
    print("BeniMellalKhnifra: ", my_json['BeniMellalKhnifra'])
    print("Oriental: ", my_json['Oriental'])
    print("SoussMassa: ", my_json['SoussMassa'])
    print("DakhlaOuedEdDahab: ", my_json['DakhlaOuedEdDahab'])
    print("GuelmimOuedNoun: ", my_json['GuelmimOuedNoun'])
    print("LayouneSakiaElHamra: ", my_json['LayouneSakiaElHamra'])
    print("Daraatafilalet: ", my_json['Daraatafilalet'])
casesperregion()
"""
