import requests

response = requests.get('https://chain.so/api/v2/get_price/BTC/USD',verify=True)

response = response.json()['data']['prices']
cumulative = 0
for i in response:
    cumulative += float(i['price'])
    for key in i:
        print key, i[key]
    print
print cumulative
print 'avg:', cumulative / len(i) 
