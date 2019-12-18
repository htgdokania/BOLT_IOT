import conf
from boltiot import Sms, Bolt
import json, time

mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)
print("Making request to Twilio to send a SMS")
response = sms.send_sms("This is the trial message to be sent ")
print("Response received from Twilio is: " + str(response))
print("Status of SMS at Twilio is :" + str(response.status))
