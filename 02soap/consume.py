from zeep import Client

client = Client(
    "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
)
result1 = client.service.NumberToWords(5)
result2 = client.service.NumberToDollars(50)
print(result1, result2)