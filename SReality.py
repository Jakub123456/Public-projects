import requests

url = "https://www.sreality.cz/api/cs/v2/estates"

querystring = {"building_condition":"1","category_main_cb":"1","category_type_cb":"1","locality_region_id":"10","page":"1","per_page":"1","tms":"1677443206210"}

payload = ""
headers = {
    "cookie": "szncmpone=1; per_page=1",
    "authority": "www.sreality.cz",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "referer": "https://www.sreality.cz/hledani/prodej/byty/praha?stav=velmi-dobry-stav&strana=3",
    "sec-ch-ua": 'Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.json)