from database import db_session
import json
from models import AzureUsage
from datetime import datetime

vm = set()
meter_category = set()
instance = []

class Azure(object):
    
    def __init__(self):
        pass
    
    def import_usage(self):
      with open('usage-hourly.json') as usage_file:
          usage_data = json.load(usage_file)

      for usage in usage_data['value']:
          # if usage['properties']['meterCategory'] == 'Virtual Machines':
          instance_data = json.loads(usage['properties']['instanceData'])
          resourceUri = str(instance_data['Microsoft.Resources']['resourceUri']).split(sep='/')
          record = AzureUsage(resourceUri[4],
                              resourceUri[6],
                              resourceUri[8],
                              usage['properties']['subscriptionId'],
                              datetime.strptime(usage['properties']['usageStartTime'], '%Y-%m-%dT%H:%M:%S+00:00'),
                              datetime.strptime(usage['properties']['usageEndTime'], '%Y-%m-%dT%H:%M:%S+00:00'),
                              usage['properties']['meterName'],
                              usage['properties']['meterCategory'],
                              usage['properties']['meterId'],
                              usage['properties']['quantity'])
          db_session.add(record)
      db_session.commit()
              # vm.add((usage['properties']['meterId'], usage['properties']['quantity']))
              # instance.append(usage['properties']['instanceData'])
        # instance_data = json.loads(usage['properties']['instanceData'])
        # print(instance_data['Microsoft.Resources'])
        #   if usage['properties'][vm]['meterCategory'] == 'Virtual Machines':
        #       print(usage['id'])
def main():
  AzureUsage.query.delete()
  azure = Azure()
  azure.import_usage()
  print(meter_category)
  # print(instance)
  # for record in instance:
  #   # print(record)
  #   print(json.loads(record))
  #   print('\n')

if __name__ == '__main__':
  main()