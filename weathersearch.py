import random
import re
import urllib
import urllib.request
ip=input("Enter the Location : ")
url="http://www.weather-forecast.com/locations/"+ip+"/forecasts/latest"      #url used to check the weather report of the input location
print(url)

data1= urllib.request.urlopen(url).read()
d=data1.decode("utf-8")

#Here reg-ex is used to reterive information from the source page of the requested url
ans=re.search('Day Weather Forecast Summary:</b><span class="read-more-small"><span class="read-more-content"> <span class="phrase">',d)
start=ans.end()
end =start+10
an=d[start:end]
print(an)
temp=random.randint(20,30)     #Generating random temperature values of Temperature
print(temp)

#sending temp data to thingSpeak field using rest-update api 
data3=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=*****************&field1="+str(temp))

print(data3)

#controlling the switching of pump by sending 1 and 0 values to another field of thingSpeak
if an=="Mostly dry":
	data2=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=*****************&field1="+str(1))
	print(data2)
elif an=="Light rain":
	data2=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=*****************&field1="+str(0))
	print(data2)
