import ratecard
import usage
from models import AzureRateCard, AzureUsage
import yaml

AzureRateCard.query.delete()
AzureUsage.query.delete()
ratecard = ratecard.Azure()
usage = usage.Azure()
ratecard.import_ratecard()
usage.import_usage()

results = []
prices = []

vms = AzureUsage.query.filter(AzureUsage.Providers == 'Microsoft.Compute').all()

for record in vms:
    results.append((record.MeterId, record.Quantity))

for result in results:
    meterid, quantity = result
    record = AzureRateCard.query.filter(AzureRateCard.MeterId == meterid).first()
    aa = yaml.load(record.MeterRates)
    prices.append(quantity*aa['0'])

print(prices)
