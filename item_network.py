import requests
import json
import item_class
import os

def run_query(query):
    headers = {"Content-Type": "application/json"}
    response = requests.post('https://api.tarkov.dev/graphql', headers=headers, json={'query': query})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))

def save_items_to_json(items, filename):
    serialized_items = [serialize_item(item) for item in items]
    with open(filename, 'w') as file:
        json.dump(serialized_items, file, indent=4)

def load_items_from_json(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            serialized_items = json.load(file)
            return [deserialize_item(item) for item in serialized_items]

def GetInformation():
    filename = "items.json"
    if os.path.exists(filename):
        return load_items_from_json(filename)
    else:
        req = """
            {
                items {
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
            """
        result = run_query(req)
        save_items_to_json(result["data"]["items"], filename)
        return deserialize_item(result)
    
def serialize_item(item):
    return {
        "name": item.name,
        "short_name": item.short_name,
        "normalized_name": item.normalized_name,
        "sell_for": {
            "vendor": {"name": item.sell_for.vendor.name},
            "price": item.sell_for.price,
            "currency": item.sell_for.currency
        }
    }

def deserialize_item(dataserialized):
    items = []
    for item_data in dataserialized:
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

    return item_class.create_items_dictionary(items)

def find_item(name_to_find, items_dict):
    if name_to_find in items_dict:
        item = items_dict[name_to_find]
        print("Objet trouvé:", item.name)
    else:
        print("Objet non trouvé.")






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