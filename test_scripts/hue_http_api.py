import requests
url = "http://192.168.86.39/api/gWRltHp0b809X1c3yPcWown9AMN8NYhmKkx2LSG0/lights/12/state"
birds_come_data={"on":True, "xy":[0.1792,0.0641]}
birds_gone_data = {"on":False}
x = requests.put(url, json=birds_come_data)

print(x.text)