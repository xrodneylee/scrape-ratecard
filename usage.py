from database import db_session
import json

vm = set()
meter_category = set()
instance = []

class Azure(object):
    
    def __init__(self):
        pass
    
    def import_data(self):
      with open('usage-daily.json') as usage_file:
          usage_data = json.load(usage_file)

      for usage in usage_data['value']:
          meter_category.add(usage['properties']['meterCategory'])
          if usage['properties']['meterCategory'] == 'Virtual Machines':
              vm.add((usage['properties']['meterId'], usage['properties']['quantity']))
              instance.append(usage['properties']['instanceData'])
        # instance_data = json.loads(usage['properties']['instanceData'])
        # print(instance_data['Microsoft.Resources'])
        #   if usage['properties'][vm]['meterCategory'] == 'Virtual Machines':
        #       print(usage['id'])
def main():
  azure = Azure()
  azure.import_data()
  print(meter_category)
  # print(instance)
  # for record in instance:
  #   # print(record)
  #   print(json.loads(record))
  #   print('\n')

if __name__ == '__main__':
  main()