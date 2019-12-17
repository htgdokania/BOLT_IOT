from boltiot import Bolt
api_key = "b19b11ae-3124-4686-ac2b-8d554b6d7870"
device_id  = "BOLT294229"
mybolt = Bolt(api_key, device_id)
i='0'
for i in range(255):
	response = mybolt.analogWrite('0', i)
	print (response,i)

