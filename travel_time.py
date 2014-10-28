import pandas
import requests

URL = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={visitor_postcode}&destinations={museum}"

postcodes_raw = pandas.read_csv("sample_postcodes.csv", header=None)
postcodes = [postcode.replace(" ", "") for postcode in postcodes_raw[0].values]
unique_postcodes = set(postcodes)
travel_times = {}


for postcode in unique_postcodes:
    try:
        formatted_url = URL.format(visitor_postcode=postcode, museum="G769HR")
        response_json = requests.get(formatted_url).json()
        travel_times[postcode] = response_json["rows"][0]["elements"][0]["duration"]["text"]
    except Exception:
        pass

postcodes_with_times = []

for postcode in postcodes:
    travel_time = travel_times[postcode]
    postcodes_with_times.append("{},{}\n".format(postcode, travel_time))

with open("postcodes_with_times.csv", "w") as output:
    output.writelines(postcodes_with_times)
