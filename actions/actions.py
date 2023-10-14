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
# actions.py
# from rasa_sdk import Action
# from rasa_sdk.events import SlotSet
# from rasa.core.policies.fallback import FallbackPolicy
#
#
# class FallbackAction(Action):
#     def name(self):
#         return "action_default_fallback"
#
#     def run(self, dispatcher, tracker, domain):
#         # Your fallback message
#         fallback_response = "'I appreciate your question, but it seems I'm currently stumped.😬😅. I'll be sure to add this to my bot head 😉. Is there anything else you'd like to ask, or can I assist you with something else?"
#
#         dispatcher.utter_message(fallback_response)
#
#         return [SlotSet("fallback_triggered", True)]
