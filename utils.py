import json
def json_write(name,Parsed_trades):
    json_trades = json.dumps(Parsed_trades)
    full_name=name+'.json'
    with open(full_name, 'w') as outfile:
        outfile.write(json_trades)