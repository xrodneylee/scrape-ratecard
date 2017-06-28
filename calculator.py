import ratecard
import usage
from models import AzureRateCard, AzureUsage

AzureRateCard.query.delete()
AzureUsage.query.delete()
ratecard = ratecard.Azure()
usage = usage.Azure()
ratecard.import_ratecard()
usage.import_usage()
