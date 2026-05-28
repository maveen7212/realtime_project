import requests

# API Key
api_key = "ycOrrj2NLYdzuOBr"

# League ID
league_id = 1639

# API URL
url = f"http://api.isportsapi.com/sport/football/schedule/basic?api_key={api_key}&leagueId={league_id}"

try:
    # Send GET request
    response = requests.get(url)

    # Check status
    response.raise_for_status()

    # Convert response to JSON
    data = response.json()

    # Print data
    print("API Response:")
    print(data)

except requests.exceptions.RequestException as e:
    print("Error:", e)


    