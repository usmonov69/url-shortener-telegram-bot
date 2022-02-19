
import requests


url = "https://url-shortener-service.p.rapidapi.com/shorten"

def shortener(url_id):
	payload = f"url={url_id}"
	headers = {
	    'content-type': "application/x-www-form-urlencoded",
	    'x-rapidapi-host': "url-shortener-service.p.rapidapi.com",
	    'x-rapidapi-key': "9c33c1c667msh7b56fe811d2de8dp1b2e49jsnee196e80ca61"
	    }

	response = requests.request("POST", url, data=payload, headers=headers)
	res = response.json()
	try:
		get_url = res['result_url']
	except:
		return False
	return get_url
