# WeatherForecastThingSpeak

This is a used case where we are using a website named "http://www.weather-forecast.com/locations/" to find 
the current weather of the particular city or particular location.

Then according to the weather we are sending actuation in form of 1 and 0 to the ThingSpeak cloud where further 
we can use notification to control actuations.

You can get your ThingSpeak update API by:
 ->Login to the thingSpeak account.
 ->Go to My Profile 
 ->There you will find update API requests at the end which can be used to send data.

Moreover here we are generating sitimulated values using Random function(in real case a temperature sensor can be used) 
and current temperature can be send to cloud and if any unusual case happens an alert can be generated further.

Hence overall becomes a good used case for Smart Agriculture system where we are monitoring temperature and controlling 
actuation according to the weather.

