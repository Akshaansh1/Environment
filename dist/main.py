import requests
API_KEY = "aa22fbdd743bed8919c5ce3dce8727d2"
city = input()
api_endpoint = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={API_KEY}'


response = requests.get(api_endpoint)
locations = response.json()

first_location = locations[0]
lat = first_location.get('lat')
lon= first_location.get('lon')

aqi_api_endpoint = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"

response2 = requests.get(aqi_api_endpoint)

data = response2.json()

aqi_value = data['list'][0]['main']['aqi']

if aqi_value == 1:
    print("Good")
if aqi_value == 2:
    print("Fair")
if aqi_value == 3:
    print("Moderate")
if aqi_value == 4:
    print("Poor")
if aqi_value == 5:
    print("Very Poor")
