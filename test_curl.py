#url = "http://router.project-osrm.org/route/v1/driving/"
import requests
url = "http://127.0.0.1:5000/route/v1/cycling/"

lat_1, lon_1 = 37.774003, -121.912118 #37.777158, -121.911073#

lat_2, lon_2 = 37.778167, -121.916807



# lon_1, lat_1,  = 13.388860, 52.517037

# lon_2, lat_2,  = 13.397634, 52.529407

params = {"overview": "full",# Optional: Return the full geometry
          "steps": "true",# Optional: Include turn-by-turn directions
          "geometries": "geojson" # Optional: Return route geometry as GeoJSON
          }



request_url = f"{url}{lon_1},{lat_1};{lon_2},{lat_2}"

print (f"Request URL: {request_url}")

response = requests.get(request_url, params=params)
print (response.json())
