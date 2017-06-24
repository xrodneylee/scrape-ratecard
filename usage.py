from database import db_session

vm = set()
meter_category = set()

with open('usage-daily.json') as usage_file:
  usage_data = json.load(usage_file)

for usage in usage_data['value']:
    meter_category.add(usage['properties']['meterCategory'])
    # instance_data = json.loads(usage['properties']['instanceData'])
    # print(instance_data['Microsoft.Resources'])
    #   if usage['properties'][vm]['meterCategory'] == 'Virtual Machines':
    #       print(usage['id'])
    if usage['properties']['meterCategory'] == 'Virtual Machines':
        vm.add((usage['properties']['meterId'], usage['properties']['quantity']))