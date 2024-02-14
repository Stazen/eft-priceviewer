import requests

def run_query(query):
    headers = {"Content-Type": "application/json"}
    response = requests.post('https://api.tarkov.dev/graphql', headers=headers, json={'query': query})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))

def GetInformation(itemName):
    req = f"""
        {{
            items(name: "{itemName}") {{
                name,
                shortName,
                normalizedName,
                sellFor {{
                    vendor {{
                        name
                    }}
                    price
                    currency
                }}
            }}  
        }}
        """
    return run_query(req)








test = """{
  items(name: "salewa") {
    name,
    shortName,
    normalizedName,
    basePrice
    avg24hPrice
    historicalPrices {
      price
      timestamp
    }
    sellFor {
      vendor {
        name
      }
      price
    }
  }  
}"""