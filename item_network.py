import requests
import json
import item_class

def run_query(query):
    headers = {"Content-Type": "application/json"}
    response = requests.post('https://api.tarkov.dev/graphql', headers=headers, json={'query': query})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))

def GetInformation(itemName):
    print("ICIIII : " + itemName)
    req = """
          {
              items(name: "%s") {
                name,
                shortName,
                normalizedName,
                sellFor {
                    vendor {
                        name
                    }
                    price
                    currency
                }
              }
          }
          """ % itemName.strip().replace('\n', '')
    return deserialize_item(run_query(req))

def deserialize_item(dataserialized):
# Mapper les données en objets Python
    items = []
    for item_data in dataserialized["data"]["items"]:
        name = item_data["name"]
        short_name = item_data["shortName"]
        normalized_name = item_data["normalizedName"]
        
        sell_for = []
        for sell_data in item_data["sellFor"]:
            vendor = item_class.Vendor(sell_data["vendor"]["name"])
            price = sell_data["price"]
            currency = sell_data["currency"]
            sell_for.append(item_class.Price(vendor, price, currency))
        items.append(item_class.Item(name, short_name, normalized_name, sell_for))

        return items;








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