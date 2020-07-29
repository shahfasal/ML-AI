from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import Restarted
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.events import ActionReverted
import zomatopy
import json
import pandas as pd
import smtp_email


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        config = {"user_key": "b58e2fef567e259ed62c9d36f8df055e"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budget = tracker.get_slot('budget')
        print("budget", budget)
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        cuisines_dict = {'chinese': 25, 'america': 1, 'mexican': 73,
                         'italian': 55,  'north indian': 50, 'south indian': 85}
        results = zomato.restaurant_search(
            "", lat, lon, str(cuisines_dict.get(cuisine)), 1000)
        d = json.loads(results)
        name_list = []
        location_list = []
        rating_list = []
        budget_list = []
        response = ""
        
        if d['results_found'] == 0:
            dispatcher.utter_message("Sorry, could not retrieve information about restaurants!")
            return [UserUtteranceReverted()]
            #return [UserUtteranceReverted(), SlotSet('location', loc), SlotSet('cuisine', cuisine), SlotSet('budget', budget), SlotSet('found_restaurants', False)]
        else:
            name_list = [restaurant['restaurant']['name']
                         for restaurant in d['restaurants']]
            location_list = [restaurant['restaurant']['location']
                             ['address'] for restaurant in d['restaurants']]

            rating_list = [float(restaurant['restaurant']['user_rating']
                           ['aggregate_rating']) for restaurant in d['restaurants']]

            budget_list = [restaurant['restaurant']['average_cost_for_two']
                           for restaurant in d['restaurants']]

            # pd.set_option('display.max_colwidth', -1)
            rest_df = pd.DataFrame({'name': name_list, 'location': location_list,
                                    'rating': rating_list, 'avg_cost_for2': budget_list})
            print(rest_df.head(20))
            if budget == "Lesser than Rs.300":
                print("Lesser than Rs.300")
                rest_df_filter = rest_df[rest_df['avg_cost_for2'] < 300]
            elif budget == "Rs.300 to Rs.700":
                print("Rs.300 to Rs.700")
                rest_df_filter = rest_df[(rest_df['avg_cost_for2'] >= 300) & (rest_df['avg_cost_for2'] <= 700)]
            elif budget == "More than Rs.700":
                print("More than Rs.700")
                rest_df_filter = rest_df[(rest_df['avg_cost_for2'] > 700)]
            else:
                dispatcher.utter_message(
                    "Sorry select a valid budget. Please choose either Mid or High or Low as values !!")
                return [UserUtteranceReverted()]
            
            print(rest_df_filter.head(20))
            
            if len(rest_df_filter.index) > 0:
                print("budget : ", budget)
                print("location : ", loc)
                print("cuisine : ", cuisine)
                rest_df_sorted = rest_df_filter.sort_values(by=['rating'], ascending=False)
                print(rest_df_sorted.head(10))
                dispatcher.utter_message("Top " + cuisine + " restaurants in " + loc + " with avg. budget of " + budget + " Rs. for 2 people")
                for row in rest_df_sorted.head(5).iterrows():
                    dispatcher.utter_message(row[1]['name'] + " in " + row[1]['location'] + " has been rated " + str(row[1]['rating']) + "\n")
                # for email body
                for row in rest_df_sorted.head(10).iterrows():
                    response = response + \
                        row[1]['name']+ " in " + row[1]['location'] + \
                        " has been rated " + str(row[1]['rating']) + "\n"
                        
                return [SlotSet('location', loc), SlotSet('cuisine', cuisine), SlotSet('budget', budget), SlotSet('emailbody', response), SlotSet('found_restaurants', True)]
            else:
                dispatcher.utter_message("Sorry, could not find restaurants for location " + loc + " and cuisine " + cuisine + " with in budget " + budget + "!") 
                return [SlotSet('found_restaurants', False)]
        
            
class SendMail(Action):
    
    def name(self):
        return 'action_mail_customer'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budget = tracker.get_slot('budget')
        found_restaurants = tracker.get_slot('found_restaurants')
        subject = "Top " + cuisine + " Restaurants in " + loc + " for budget range " + budget 
        if found_restaurants:
            body = tracker.get_slot('emailbody')
            emailid = tracker.get_slot('emailId')
            emailid = emailid.split('|')[0] # Slack sends the emailId in the form of id@mail.com|id@mail.com. Remove the unwanted string.
            smtp_email.send_mail(emailid, body, subject)
            dispatcher.utter_message("E-mail sent to : " + emailid)
        return [Restarted()]


class CheckLocation(Action):

    def name(self):
        return 'action_check_location'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        print("check location", loc)
        cities = ['Ahmedabad', 'Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Pune',
                  'Agra', 'Ajmer', 'Aligarh', 'Amravati', 'Amritsar', 'Asansol', 'Aurangabad', 'Bareilly',
                  'Belgaum', 'Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bokaro Steel City',
                  'Chandigarh', 'Coimbatore', 'Cuttack', 'Dehradun', 'Dhanbad', 'Durg-Bhilai Nagar', 'Durgapur',
                  'Erode', 'Faridabad', 'Firozabad',    'Ghaziabad', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Gurgaon',
                  'Guwahati', 'Gwalior', 'Hubli-Dharwad', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar', 'Jammu', 'Jamnagar',
                  'Jamshedpur', 'Jhansi', 'Jodhpur', 'Kannur', 'Kanpur', 'Kakinada', 'Kochi', 'Kottayam', 'Kolhapur', 'Kollam',
                  'Kota', 'Kozhikode', 'Kurnool', 'Lucknow', 'Ludhiana', 'Madurai', 'Malappuram', 'Mathura', 'Goa', 'Mangalore',
                  'Meerut', 'Moradabad', 'Mysore', 'Nagpur', 'Nanded', 'Nashik', 'Nellore', 'Noida', 'Palakkad', 'Patna',
                  'Pondicherry', 'Prayagraj', 'Raipur', 'Rajkot', 'Rajahmundry', 'Ranchi', 'Rourkela', 'Salem', 'Sangli',
                  'Siliguri', 'Solapur', 'Srinagar', 'Sultanpur', 'Surat', 'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli',
                  'Tirunelveli', 'Tiruppur', 'Ujjain', 'Bijapur', 'Vadodara', 'Varanasi', 'Vasai-Virar City', 'Vijayawada', 'Warangal']

        cities_lower = [x.lower() for x in cities]
        print(cities_lower)
        if loc.lower() not in cities_lower:
            dispatcher.utter_message(
                "Sorry, we do not operate in this city. Please try with a different location.")
            return [UserUtteranceReverted(), SlotSet('location', loc), SlotSet("location_verified", False)]
        else:
            return [SlotSet('location', loc), SlotSet("location_verified", True)]

        
class VerifyCuisine(Action):

    def name(self):
        return "action_check_cuisine"

    def run(self, dispatcher, tracker, domain):
        cuisines = ['chinese', 'mexican', 'italian',
                    'american', 'south indian', 'north indian']
        error_msg = "Sorry!! specified cuisine is not supported. Supported cuisine types are (Chinese, Mexican, Italian, American, South Indian and North Indian). Please re-enter!!"
        cuisine = tracker.get_slot('cuisine')
        try:
            cuisine = cuisine.lower()
        except (RuntimeError, TypeError, NameError, AttributeError):
            dispatcher.utter_message(error_msg)
            return [SlotSet('cuisine', None), SlotSet('cuisine_verified', False)]
        if cuisine in cuisines:
            print("cuisine", cuisine)
            return [SlotSet('cuisine', cuisine), SlotSet('cuisine_verified', True)]
        else:
            dispatcher.utter_message(error_msg)
            return [UserUtteranceReverted(), SlotSet('cuisine', None), SlotSet('cuisine_verified', False)]
