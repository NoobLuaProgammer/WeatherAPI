import requests
# this converts lat long to city e.g 51.5073219:-0.1276474
latlon = input("Latitude % Lonitude in Lat:Lon please: ")
lat, lon = latlon.split(':')

response = requests.get(
    f'http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit=1&appid=3356d213048d8a42a5f5fa1608140756'
)

if response.status_code == 200:
    data = response.json()
    if data:
        city = data[0]['name']
        print(f"City: {city}")
    else:
        print("Location not found.")
else:
    print(f"Error: {response.status_code}")
