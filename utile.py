import json
import math
def json_write(name,Parsed_trades):
    json_trades = json.dumps(Parsed_trades)
    full_name=name+'.json'
    with open(full_name, 'w') as outfile:
        outfile.write(json_trades)
def all_platform_list():
    with open("platform.json", 'r') as outfile:
        return(json.load(outfile))
def all_item_list():
    with open("item.json", 'r') as outfile:
        return(json.load(outfile))
def all_paint_list():
    with open("paint.json", 'r') as outfile:
        return(json.load(outfile))
def progress_bar(progress,total):
    percent= 100 * (progress / float(total))
    #add wier symbol
    bar ='*' * int(percent)+'-'*(100-int(percent))
    print(f"\r|{bar}| {percent:.2f}%")



def dummy_function():
    print("test")