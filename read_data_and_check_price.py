import json
import numpy as np
import pandas as pd
# Opening JSON file

import plotly.express as px



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
def get_selling_prices_for_item(item,data):
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
def get_buying_prices_for_item(item,data):
    prices=[]
    for trade in data:
        print(trade["trader"])
        #verify one to one items
        if(len(trade["Hasitems"])==len(trade["WantItems"])):
        #verify is selling for credits
            for has, want in zip(trade["Hasitems"], trade["WantItems"]):
                if(has["name"]=="Credits" and check_equal_item(want,item)  ):
                    prices.append(has["quantity"])
                    print("selling " , want,"for",has["quantity"] , "credits")
    return prices
#print('color' in item1)
def graph_Demand_offer(item):
    pass
    filename1="Buying_"+item["name"]+".json"
    f = open(filename1)
    data = json.load(f)
    buying_prices = get_buying_prices_for_item(item,data)
    filename2="selling_"+item["name"]+".json"
    f2 = open(filename2)
    data2 = json.load(f2)
    selling_prices=get_selling_prices_for_item(item,data2)
    int_buying_prices=[]
    int_selling_prices=[]
    for price in buying_prices:
        int_buying_prices.append(int(price))
    for price in selling_prices:
        int_selling_prices.append(int(price))
    x = np.arange(0, len(int_selling_prices), 1)
    print("selling size " ,len(int_selling_prices))
    print("buying size " ,len(int_buying_prices))
    #TODO PAdding function
    diff= len(int_selling_prices)-len(int_buying_prices)
    for i in range(0,diff):
        int_buying_prices.append(0)
    GraphToShow = {'To_be_replaced_with_time':x,'selling_price':int_selling_prices,'buying_price':int_buying_prices}
    df = pd.DataFrame(GraphToShow)
    fig = px.line(df)
    fig.update_layout(xaxis={'categoryorder':'total ascending'})
    fig.show()
    f.close()
    f2.close()



item={'name':'Zomba','color':'Titanium White'}
graph_Demand_offer(item)

#TODO add timestamps and thus add liquitity bous ( if seller was afk too long affect action speed and pricing do absolute parameters and then make it depend)
#TODO selling idea check for time and flag old times and new times