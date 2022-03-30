# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from calendar import TextCalendar
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import os, requests

class ActionGetWeather(Action):

    def name(self)-> Text:
        return "action_get_weather"
    

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('GPE')
        print(loc)
        degree_sign= u'\N{DEGREE SIGN}'

        # need to get weather API key from openweathermap.org
        # and save to ENV variable
        payload = {'q': loc, 'units':'metric', 'appid': os.environ['WEATHER_API_KEY']}
        #http get method 
        response = requests.get('http://api.openweathermap.org/data/2.5/find', params=payload)
        
        try:
            # getting the data in JSON format
            data = response.json()
            print(data)
            print(type(data))   
            x = data['list'][0]

            temperature = x['main']['temp']
            description = x['weather'][0]['description']
            city = x['name']
            humidity = x['main']['humidity']
            windSpeed = x['wind']['speed']
            cloud = x['clouds']['all']
            
            weatherData = """In {}, it is {} at the moment at {}{}C. \nThe humidity level is: {}%, \nwind speed: {}m/s,\n cloudiness in the sky is {}%.""".format(city, description, degree_sign,temperature, humidity, windSpeed, cloud)
            
            
            dispatcher.utter_message(weatherData)

            return [SlotSet("GPE", None)]

        except requests.exceptions.HTTPError as e:
            dispatcher.utter_message(text="HTTP Error! City not found!")

        except Exception as e:
            dispatcher.utter_message(text="Could not find the city!")

