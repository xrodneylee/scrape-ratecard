from database import db_session
from models import AzureRateCard
import json


class Azure:

    meter_status = set()

    with open('ratecard-TWD.json') as ratecard_file:
      ratecard_data = json.load(ratecard_file)


        #   if usage['properties'][vm]['meterCategory'] == 'Virtual Machines':
        #       print(usage['id'])

    for price in ratecard_data['Meters']:
      meter_status.add(price['MeterStatus'])
      if price['MeterStatus'] == 'Active':
        record = AzureRateCard(price['MeterId'], str(price['MeterRates']))
        db_session.add(record)
    db_session.commit()

# temp = AzureRateCard.query.filter(AzureRateCard.MeterId == '8d29e058-214a-4ec5-a52a-df7d76ce1683').first()
# print(json.loads((temp.MeterRates).replace("'", '"')).get('0'))
# print(meter_status)