import json
  
# Opening JSON file
f = open('TW_Octane.json')
import plotly.express as px

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
        if('color' not in item_to_check and 'color' not in item):
            pass
        else:
            test=False
    if ('quantity' in item_to_check and 'quantity' in item ):
        if(item_to_check["quantity"]==item["quantity"]):
            pass
        else:
            test=False
    else:
        if('quantity' not in item_to_check and 'quantity' not in item):
            pass
        else:
            test=False
    return test
item={'name':'Octane','color':'Titanium White'}
def get_selling_prices_for_item(item):
    prices=[]
    for trade in data:
        print(trade["trader"])
        #verify one to one items
        if(len(trade["Hasitems"])==len(trade["WantItems"])):
        #verify is selling for credits
            for has, want in zip(trade["Hasitems"], trade["WantItems"]):
                if(want["name"]=="Credits" and check_equal_item(has,item)  ):
                    prices.append(want["quantity"])
                    print("selling " , has,"for",want["quantity"] , "credits")
    return prices
#print('color' in item1)
prices = get_selling_prices_for_item(item)
int_prices=[]
for price in prices:
    int_prices.append(int(price))
int_prices.sort()
print(int_prices)
fig = px.histogram(prices)
fig.update_layout(xaxis={'categoryorder':'total ascending'})
fig.show()
print(prices)
f.close()

#TODO add timestamps and thus add liquitity bous ( if seller was afk too long affect action speed and pricing)
#TODO selling idea check for time and flag old times and new times