import json

meterCategory = set()
vm = set()

with open('usage-daily.json') as usage_file:
  usage_data = json.load(usage_file)

for usage in usage_data['value']:
    meterCategory.add(usage['properties']['meterCategory'])
    # instance_data = json.loads(usage['properties']['instanceData'])
    # print(instance_data['Microsoft.Resources'])
    if usage['properties']['meterCategory'] == 'Virtual Machines':
        vm.add((usage['properties']['meterId'], usage['properties']['quantity']))


print(meterCategory)
print(vm)


# with open('ratecard-TWD.json') as ratecard_file:
#   ratecard_data = json.load(ratecard_file)


    #   if usage['properties'][vm]['meterCategory'] == 'Virtual Machines':
    #       print(usage['id'])

# for price in ratecard_data['Meters']:
#   print(price)