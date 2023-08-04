import requests

def get_data(param):
    url = 'https://catfact.ninja/'
    result = requests.get(url+param)
    data = result.json()
    print(data)
    try:
        if data['code'] == 404:
           return False
    except:
        return True

print(get_data('f'))







# for fact in data_1['data']:
#     if fact['length'] > 30:
#         print('length error!')
#         break
