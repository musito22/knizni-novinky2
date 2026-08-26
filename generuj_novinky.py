import json
import os
import urllib.request

API_KEY = os.environ.get("ALMA_API_KEY")
API_URL = f"https://api-eu.hosted.exlibrisgroup.com/primo/v1/search?vid=420CARDS_JCU:JCU&tab=LibraryCatalog&scope=MyInstitution&q=rtype,exact,books&qInclude=facet_tlevel,exact,available_p&sort=date_d&limit=25&apikey={API_KEY}"

try:
    req = urllib.request.Request(API_URL, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode("utf-8"))
        
        with open("novinky.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Soubor novinky.json byl úspěšně vygenerován.")
except Exception as e:
    print(f"Chyba při stahování dat: {e}")
    exit(1)
