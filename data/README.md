# Data Description

_**Dataset**: autos.csv_
_Kaynak:_ [Kaggle](https://www.kaggle.com/orgesleka/used-cars-database/version/3)

_Not: Dataset AutoScout degil Ebay-Kleinanzeigen'dan. Farkli degiskenler olabilir._

Over 370000 used cars scraped with Scrapy from Ebay-Kleinanzeigen. The content of the data is in german, so one has to translate it first if one can not speak german. Those fields are included: autos.csv:

dateCrawled : when this ad was first crawled, all field-values are taken from this date

name : "name" of the car

seller : private or dealer

offerType

price : the price on the ad to sell the car

abtest

vehicleType

yearOfRegistration : at which year the car was first registered

gearbox

powerPS : power of the car in PS

model

kilometer : how many kilometers the car has driven

monthOfRegistration : at which month the car was first registered

fuelType

brand

notRepairedDamage : if the car has a damage which is not repaired yet

dateCreated : the date for which the ad at ebay was created

nrOfPictures : number of pictures in the ad (unfortunately this field contains everywhere a 0 and is thus useless (bug in crawler!) )

postalCode

lastSeenOnline : when the crawler saw this ad last online

The fields lastSeen and dateCreated could be used to estimate how long a car will be at least online before it is sold.

**Ornek bir analiz:** https://www.kaggle.com/ddmngml/trying-to-predict-used-car-value