from boltiot import Bolt
api_key = "b19b11ae-3124-4686-ac2b-8d554b6d7870"
device_id  = "BOLT294229"
mybolt = Bolt(api_key, device_id)
response = mybolt.restart()
print (response)
