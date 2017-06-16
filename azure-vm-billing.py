from database import db_session
from models import AzureRateCard
import json

meter_category = set()
vm = set()
meter_status = set()

with open('usage-daily.json') as usage_file:
  usage_data = json.load(usage_file)

for usage in usage_data['value']:
    meter_category.add(usage['properties']['meterCategory'])
    # instance_data = json.loads(usage['properties']['instanceData'])
    # print(instance_data['Microsoft.Resources'])
    if usage['properties']['meterCategory'] == 'Virtual Machines':
        vm.add((usage['properties']['meterId'], usage['properties']['quantity']))


print(meter_category)
print(vm)


with open('ratecard-TWD.json') as ratecard_file:
  ratecard_data = json.load(ratecard_file)


    #   if usage['properties'][vm]['meterCategory'] == 'Virtual Machines':
    #       print(usage['id'])

for price in ratecard_data['Meters']:
  meter_status.add(price['MeterStatus'])
  if price['MeterStatus'] == 'Active':
    record = AzureRateCard(price['MeterId'], price['Unit'])
    db_session.add(record)
db_session.commit()

# print(AzureRateCard.query.filter(AzureRateCard.MeterId == '8d29e058-214a-4ec5-a52a-df7d76ce1683').first())
print(meter_status)