import json
import math
from datetime import datetime, timedelta
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
#Actual signature def time_transformer(today,time):
def time_transformer(current_date,time):
    #replace with time and now with parameter
    print("current is :", current_date)
    print("time is :", time)
    x = time.split()
    match x[1]:
        case "months" | "months," | "month" | "month,":
            new_date= current_date + timedelta(hours=-24*int(x[0]), minutes=0, seconds=0)
        case "days" | "days," | "day" | "day,":
            new_date= current_date + timedelta(hours=-24*int(x[0]), minutes=0, seconds=0)
        case "hours" | "hours," | "hour" | "hour,":
            new_date= current_date + timedelta(hours=-int(x[0]), minutes=0, seconds=0)
        case "minutes" | "minutes," | "minute" | "minute,":
            new_date= current_date + timedelta(hours=0, minutes=-int(x[0]), seconds=0)
        case "seconds" | "seconds," | "second" | "second,":
            new_date= current_date + timedelta(hours=0, minutes=0, seconds=-int(x[0]))
    return new_date

print(all_paint_list())

def dummy_function():
    print("test")

#TODO get more granular hour minute data