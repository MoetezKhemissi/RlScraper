import json
  
# Opening JSON file
f = open('testing.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)

# Iterating through the json
# list
def check_equal_item(item_to_check,item):
    test=True
    #TODO Mutiple items division for quantity
    if (item_to_check["name"]==item["name"]):
        pass
    else:
        test=False
    if ( 'color' in item_to_check and 'color' in item):
        if(item_to_check["color"]==item["color"]):
            pass
        else:
            test=False
    else:
        test=False
    if ('quantity' in item_to_check and 'quantity' in item):
        if(item_to_check["quantity"]==item["quantity"]):
            pass
        else:
            test=False
    else:
        test=False
    return test
item={"name":"Zigzag","color":"Titanium White"}
def get_selling_prices_for_item(item):
    for trade in data:
        print(trade["trader"])
        #verify one to one items
        if(len(trade["Hasitems"])==len(trade["WantItems"])):
        #verify is selling for credits
            for has, want in zip(trade["Hasitems"], trade["WantItems"]):
                if(want["name"]=="Credits" and check_equal_item(has,item)  ):
                    print("selling " , has,"for",want["quantity"] , "credits")
#print('color' in item1)
print(get_selling_prices_for_item(item))
f.close()