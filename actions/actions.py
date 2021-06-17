# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from requests.models import Response

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
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


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World from first action!")

        return []


class ActionSearchRestaurant(Action):

    def name(self) -> Text:
        return "action_search_restaurant"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']

        for e in entities:
            if e['entity'] == 'hotel':
                name = e['value']

            if name == 'indian':
                message = 'Indian1, Indian2, Indian3, Indian4'

            if name == 'chinese':
                message = 'Chinese1, Chinese2, Chinese3'

            if name == 'italian':
                message = 'Italian1, Italian2'

            if name == 'thai':
                message = 'Thai1'

        dispatcher.utter_message(message)

        return []


class ActionCovidTracker(Action):

    def name(self) -> Text:
        return "action_covid_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get(
            "https://api.covid19india.org/data.json").json()

        entities = tracker.latest_message['entities']
        print("Last message now ", entities)
        state = None
        message = ''

        for e in entities:
            if e['entity'] == 'state':
                state = e['value']

        if state == "india":
            state = "Total"

        for data in response["statewise"]:
            if data["state"] == state.title():
                print(data)
                message = "Active: " + data['active'] + " Confirmed:" + data['confirmed'] + \
                    " Recovered:" + data['recovered'] + \
                    " Last Updated:" + data['lastupdatedtime']

        dispatcher.utter_message("Covid Tracker action! " + message)

        return []
