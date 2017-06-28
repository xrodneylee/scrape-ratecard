from database import db_session
from models import AzureRateCard
import json
import yaml


class Azure(object):

    def __init__(self):
        pass

    def import_ratecard(self):
        with open('ratecard-TWD.json') as ratecard_file:
            ratecard_data = json.load(ratecard_file)

        for price in ratecard_data['Meters']:
            if price['MeterStatus'] == 'Active':
                record = AzureRateCard(price['MeterId'], str(price['MeterRates']))
                db_session.add(record)
        db_session.commit()

# temp = AzureRateCard.query.filter(AzureRateCard.MeterId == '8d29e058-214a-4ec5-a52a-df7d76ce1683').first()
# aa = yaml.load(temp.MeterRates)
# print(aa)
# print(aa['0'])
# print(json.loads((temp.MeterRates).replace("'", '"')).get('0'))
# print(meter_status)
def main():
    AzureRateCard.query.delete()
    azure = Azure()
    azure.import_ratecard()

if __name__ == '__main__':
    main()