## 1. happy path, location specified 
* greet
  - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_verified":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_verified": true}
    - utter_ask_budget
* restaurant_search{"budget":  "Lesser than Rs.300"}
    - slot{"budget":  "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget":  "Lesser than Rs.300"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "Lesser than Rs.300"}
    - slot{"found_restaurants":true}
    - slot{"emailbody":"value"}
    - action_check_continuity
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailId":"tom12@gmail.com"}
    - slot{"emailId":"tom12@gmail.com"}
    - action_mail_customer
    - utter_sent_email
    - utter_useful_info
    - utter_goodbye
    
## 2. happy path, cuisine specified 
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_verified": true}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_verified":true}
    - utter_ask_budget
* restaurant_search{"budget":  "Lesser than Rs.300"}
    - slot{"budget":  "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget":  "Lesser than Rs.300"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "Lesser than Rs.300"}
    - slot{"found_restaurants":true}
    - slot{"emailbody":"value"}
    - action_check_continuity
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailId":"tom12@gmail.com"}
    - slot{"emailId":"tom12@gmail.com"}
    - action_mail_customer
    - utter_sent_email
    - utter_useful_info
    - utter_goodbye
    
## 3. happy path, budget specified 
* greet
  - utter_greet
* restaurant_search{"budget":  "Lesser than Rs.300"}
    - slot{"budget":  "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget":  "Lesser than Rs.300"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_verified":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_verified": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "Lesser than Rs.300"}
    - slot{"found_restaurants":true}
    - slot{"emailbody":"value"}
    - action_check_continuity
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailId":"tom12@gmail.com"}
    - slot{"emailId":"tom12@gmail.com"}
    - action_mail_customer
    - utter_sent_email
    - utter_useful_info
    - utter_goodbye
    
## 4. happy path, location specified, no greet 
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mysore"}
    - slot{"location": "mysore"}
    - action_check_location
    - slot{"location": "mysore"}
    - slot{"location_verified":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_verified": true}
    - utter_ask_budget
* restaurant_search{"budget":  "Lesser than Rs.300"}
    - slot{"budget":  "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget":  "Lesser than Rs.300"}
    - action_search_restaurants
    - slot{"location": "mysore"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "Lesser than Rs.300"}
    - slot{"found_restaurants":true}
    - slot{"emailbody":"value"}
    - action_check_continuity
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailId":"tom12@gmail.com"}
    - slot{"emailId":"tom12@gmail.com"}
    - action_mail_customer
    - utter_sent_email
    - utter_useful_info
    - utter_goodbye
    
## 5. happy path, cuisine specified, no greet  
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_verified": true}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_verified":true}
    - utter_ask_budget
* restaurant_search{"budget":  "Lesser than Rs.300"}
    - slot{"budget":  "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget":  "Lesser than Rs.300"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "Lesser than Rs.300"}
    - slot{"found_restaurants":true}
    - slot{"emailbody":"value"}
    - action_check_continuity
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailId":"tom12@gmail.com"}
    - slot{"emailId":"tom12@gmail.com"}
    - action_mail_customer
    - utter_sent_email
    - utter_useful_info
    - utter_goodbye
    
## 6. happy path, budget specified, no greet  
* restaurant_search{"budget":  "Lesser than Rs.300"}
    - slot{"budget":  "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget":  "Lesser than Rs.300"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_verified":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_verified": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "Lesser than Rs.300"}
    - slot{"found_restaurants":true}
    - slot{"emailbody":"value"}
    - action_check_continuity
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailId":"tom12@gmail.com"}
    - slot{"emailId":"tom12@gmail.com"}
    - action_mail_customer
    - utter_sent_email
    - utter_useful_info
    - utter_goodbye

## 7. happy path, location specified, no mail
* greet
  - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - action_check_location
    - slot{"location": "goa"}
    - slot{"location_verified":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_verified": true}
    - utter_ask_budget
* restaurant_search{"budget":  "Lesser than Rs.300"}
    - slot{"budget":  "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget":  "Lesser than Rs.300"}
    - action_search_restaurants
    - slot{"location": "goa"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "Lesser than Rs.300"}
    - slot{"found_restaurants":true}
    - slot{"emailbody":"value"}
    - action_check_continuity
    - utter_ask_sendmail
* deny
    - utter_useful_info
    - utter_goodbye
    
## 8. happy path, cuisine specified, no greet  
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_verified": true}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_verified":true}
    - utter_ask_budget
* restaurant_search{"budget":  "Lesser than Rs.300"}
    - slot{"budget":  "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget":  "Lesser than Rs.300"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "Lesser than Rs.300"}
    - slot{"found_restaurants":true}
    - slot{"emailbody":"value"}
    - action_check_continuity
    - utter_ask_sendmail
* deny
    - utter_useful_info
    - utter_goodbye
    
## 9. happy path, budget specified, no greet  
* restaurant_search{"budget":  "Lesser than Rs.300"}
    - slot{"budget":  "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget":  "Lesser than Rs.300"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_verified":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_verified": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "Lesser than Rs.300"}
    - slot{"found_restaurants":true}
    - slot{"emailbody":"value"}
    - action_check_continuity
    - utter_ask_sendmail
* deny
    - utter_useful_info
    - utter_goodbye
    
## 10. happy path, location specified, no mail, no greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Ahmedabad"}
    - slot{"location": "Ahmedabad"}
    - action_check_location
    - slot{"location": "Ahmedabad"}
    - slot{"location_verified":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_verified": true}
    - utter_ask_budget
* restaurant_search{"budget":  "Lesser than Rs.300"}
    - slot{"budget":  "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget":  "Lesser than Rs.300"}
    - action_search_restaurants
    - slot{"location": "Ahmedabad"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "Lesser than Rs.300"}
    - slot{"found_restaurants":true}
    - slot{"emailbody":"value"}
    - action_check_continuity
    - utter_ask_sendmail
* deny
    - utter_useful_info
    - utter_goodbye
    

## 11. location specified deny
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"location": "Rishikesh"}
    - slot{"location_verified":false}
    - utter_ask_location
    
## 12. location specified deny, no greet
* restaurant_search{"location": "Hassan"}
    - slot{"location": "Hassan"}
    - action_check_location
    - slot{"location": "Hassan"}
    - slot{"location_verified":false}
    - utter_ask_location

## 13. location specified ok results deny
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_verified":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_check_cuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - slot{"budget":  "More than 700"}
    - action_check_budget
    - slot{"budget":  "More than 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"budget": "More than 700"}
    - slot{"found_restaurants":false}
    - action_check_continuity
    
## 14. location specified ok results deny, no greet
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_check_location
    - slot{"location": "Hyderabad"}
    - slot{"location_verified":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_check_cuisine
    - slot{"cuisine": "italian"}
    - slot{"cuisine_verified": true}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - slot{"budget":  "More than 700"}
    - action_check_budget
    - slot{"budget":  "More than 700"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - slot{"cuisine": "italian"}
    - slot{"budget": "More than 700"}
    - slot{"found_restaurants":false}
    - action_check_continuity

## 15. happy path, cuisine and location specified affirmative
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Meerut"}
    - slot{"cuisine": "Mexican"}
    - action_check_cuisine
    - slot{"cuisine": "Mexican"}
    - slot{"cuisine_verified": true}
    - slot{"location": "Meerut"}
    - action_check_location
    - slot{"location": "Meerut"}
    - slot{"location_verified":true}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_check_budget
    - slot{"budget":  "More than 700"}
    - action_search_restaurants
    - slot{"location": "Meerut"}
    - slot{"cuisine": "Mexican"}
    - slot{"budget": "More than 700"}
    - slot{"found_restaurants":true}
    - slot{"emailbody":"value"}
    - action_check_continuity
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailId":"catzz@hotmail.com"}
    - slot{"emailId":"catzz@hotmail.com"}
    - action_mail_customer   
    - utter_sent_email
    - utter_useful_info
    - utter_goodbye
    
## 16. happy path, cuisine and location specified affirmative, no greet
* restaurant_search{"cuisine": "Mexican", "location": "Bhilai"}
    - slot{"cuisine": "Mexican"}
    - action_check_cuisine
    - slot{"cuisine": "Mexican"}
    - slot{"cuisine_verified": true}
    - slot{"location": "Bhilai"}
    - action_check_location
    - slot{"location": "Bhilai"}
    - slot{"location_verified":true}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_check_budget
    - slot{"budget":  "More than 700"}
    - action_search_restaurants
    - slot{"location": "Bhilai"}
    - slot{"cuisine": "Mexican"}
    - slot{"budget": "More than 700"}
    - slot{"found_restaurants":true}
    - slot{"emailbody":"value"}
    - action_check_continuity
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailId":"catzz@hotmail.com"}
    - slot{"emailId":"catzz@hotmail.com"}
    - action_mail_customer   
    - utter_sent_email
    - utter_useful_info
    - utter_goodbye
    
## 17. happy path, cuisine and location specified affirmative, no mail
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Durgapur"}
    - slot{"cuisine": "Mexican"}
    - action_check_cuisine
    - slot{"cuisine": "Mexican"}
    - slot{"cuisine_verified": true}
    - slot{"location": "Durgapur"}
    - action_check_location
    - slot{"location": "Durgapur"}
    - slot{"location_verified":true}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_check_budget
    - slot{"budget":  "More than 700"}
    - action_search_restaurants
    - slot{"location": "Durgapur"}
    - slot{"cuisine": "Mexican"}
    - slot{"budget": "More than 700"}
    - slot{"found_restaurants":true}
    - slot{"emailbody":"value"}
    - action_check_continuity
    - utter_ask_sendmail
* deny
    - utter_useful_info
    - utter_goodbye
    
## 18. happy path, cuisine and location specified affirmative, no mail, no greet
* restaurant_search{"cuisine": "Mexican", "location": "Firozabad"}
    - slot{"cuisine": "Mexican"}
    - action_check_cuisine
    - slot{"cuisine": "Mexican"}
    - slot{"cuisine_verified": true}
    - slot{"location": "Firozabad"}
    - action_check_location
    - slot{"location": "Firozabad"}
    - slot{"location_verified":true}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_check_budget
    - slot{"budget":  "More than 700"}
    - action_search_restaurants
    - slot{"location": "Firozabad"}
    - slot{"cuisine": "Mexican"}
    - slot{"budget": "More than 700"}
    - slot{"found_restaurants":true}
    - slot{"emailbody":"value"}
    - action_check_continuity
    - utter_ask_sendmail
* deny
    - utter_useful_info
    - utter_goodbye
    
## 19. cuisine and location specified deny
* greet
    - utter_greet
* restaurant_search{"cuisine": "Thai", "location": "Najafgad"}
    - slot{"cuisine": "Thai"}
    - action_check_cuisine
    - slot{"cuisine": "Thai"}
    - slot{"cuisine_verified": true}
    - slot{"location": "Najafgad"}
    - action_check_location
    - slot{"location": "Najafgad"}
    - slot{"location_verified":false}
    - utter_ask_location
    
## 20. cuisine and location specified deny, no greet
* restaurant_search{"cuisine": "Thai", "location": "ballari"}
    - slot{"cuisine": "Thai"}
    - action_check_cuisine
    - slot{"cuisine": "Thai"}
    - slot{"cuisine_verified": true}
    - slot{"location": "ballari"}
    - action_check_location
    - slot{"location": "ballari"}
    - slot{"location_verified":false}
    - utter_ask_location

## 21. cuisine and location specified ok results deny
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Bhubaneswar"}
    - slot{"cuisine": "South Indian"}
    - action_check_cuisine
    - slot{"cuisine": "South Indian"}
    - slot{"cuisine_verified": true}
    - slot{"location": "Bhubaneswar"}
    - action_check_location
    - slot{"location": "Bhubaneswar"}
    - slot{"location_verified":true}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_check_budget
    - slot{"budget":  "More than 700"}
    - action_search_restaurants
    - slot{"location": "Bhubaneswar"}
    - slot{"cuisine": "South Indian"}
    - slot{"budget": "More than 700"}
    - slot{"found_restaurants":false}
    - action_check_continuity
    
## 22. cuisine and location specified ok results deny, no greet
* restaurant_search{"cuisine": "Mexican", "location": "Kanpur"}
    - slot{"cuisine": "South Indian"}
    - action_check_cuisine
    - slot{"cuisine": "South Indian"}
    - slot{"cuisine_verified": true}
    - slot{"location": "Kanpur"}
    - action_check_location
    - slot{"location": "Kanpur"}
    - slot{"location_verified":true}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_check_budget
    - slot{"budget":  "More than 700"}
    - action_search_restaurants
    - slot{"location": "Kanpur"}
    - slot{"cuisine": "South Indian"}
    - slot{"budget": "More than 700"}
    - slot{"found_restaurants":false}
    - action_check_continuity

## 23. happy path, cuisine and budget specified affirmative
* greet
    - utter_greet
* restaurant_search{"cuisine": "American", "budget": "Lesser than Rs.300"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"cuisine": "American"}
    - slot{"cuisine_verified": true}
    - slot{"budget": "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget": "Lesser than Rs.300"}
    - utter_ask_location
* restaurant_search{"location":  "Kolkata"}
    - slot{"location":  "Kolkata"}
    - action_check_location
    - slot{"location":  "Kolkata"}
    - slot{"location_verified":true}
    - action_search_restaurants
    - slot{"location":  "Kolkata"}
    - slot{"cuisine": "American"}
    - slot{"budget": "Lesser than Rs.300"}
    - slot{"found_restaurants":true}
    - slot{"emailbody":"value"}
    - action_check_continuity
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailId":"catzz@gmail.com"}
    - slot{"emailId":"catzz@gmail.com"}
    - action_mail_customer   
    - utter_sent_email
    - utter_useful_info
    - utter_goodbye

## 24. happy path, cuisine and budget specified affirmative, no greet
* restaurant_search{"cuisine": "American", "budget": "Lesser than Rs.300"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"cuisine": "American"}
    - slot{"cuisine_verified": true}
    - slot{"budget": "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget": "Lesser than Rs.300"}
    - utter_ask_location
* restaurant_search{"location":  "Indore"}
    - slot{"location":  "Indore"}
    - action_check_location
    - slot{"location":  "Indore"}
    - slot{"location_verified":true}
    - action_search_restaurants
    - slot{"location":  "Indore"}
    - slot{"cuisine": "American"}
    - slot{"budget": "Lesser than Rs.300"}
    - slot{"found_restaurants":true}
    - slot{"emailbody":"value"}
    - action_check_continuity
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailId":"catzz@gmail.com"}
    - slot{"emailId":"catzz@gmail.com"}
    - action_mail_customer   
    - utter_sent_email
    - utter_useful_info
    - utter_goodbye

## 25. happy path, cuisine and budget specified affirmative, no mail
* greet
    - utter_greet
* restaurant_search{"cuisine": "American", "budget": "Lesser than Rs.300"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"cuisine": "American"}
    - slot{"cuisine_verified": true}
    - slot{"budget": "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget": "Lesser than Rs.300"}
    - utter_ask_location
* restaurant_search{"location":  "Erode"}
    - slot{"location":  "Erode"}
    - action_check_location
    - slot{"location":  "Erode"}
    - slot{"location_verified":true}
    - action_search_restaurants
    - slot{"location":  "Erode"}
    - slot{"cuisine": "American"}
    - slot{"budget": "Lesser than Rs.300"}
    - slot{"found_restaurants":true}
    - slot{"emailbody":"value"}
    - action_check_continuity
    - utter_ask_sendmail
* deny
    - utter_useful_info
    - utter_goodbye
    
## 26. happy path, cuisine and budget specified affirmative, no mail, no greet
* restaurant_search{"cuisine": "American", "budget": "Lesser than Rs.300"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"cuisine": "American"}
    - slot{"cuisine_verified": true}
    - slot{"budget": "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget": "Lesser than Rs.300"}
    - utter_ask_location
* restaurant_search{"location":  "Jabalpur"}
    - slot{"location":  "Jabalpur"}
    - action_check_location
    - slot{"location":  "Jabalpur"}
    - slot{"location_verified":true}
    - action_search_restaurants
    - slot{"location":  "Jabalpur"}
    - slot{"cuisine": "American"}
    - slot{"budget": "Lesser than Rs.300"}
    - slot{"found_restaurants":true}
    - slot{"emailbody":"value"}
    - action_check_continuity
    - utter_ask_sendmail
* deny
    - utter_useful_info
    - utter_goodbye

## 27. cuisine and budget specified deny
* greet
    - utter_greet
* restaurant_search{"cuisine": "American", "budget": "Lesser than Rs.300"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"cuisine": "American"}
    - slot{"cuisine_verified": true}
    - slot{"budget": "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget": "Lesser than Rs.300"}
    - utter_ask_location
* restaurant_search{"location":  "Nainital"}
    - slot{"location":  "Nainital"}
    - action_check_location
    - slot{"location":  "Nainital"}
    - slot{"location_verified":false}
    - utter_ask_location
    
## 28. cuisine and budget specified deny, no greet
* restaurant_search{"cuisine": "American", "budget": "Lesser than Rs.300"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"cuisine": "American"}
    - slot{"cuisine_verified": true}
    - slot{"budget": "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget": "Lesser than Rs.300"}
    - utter_ask_location
* restaurant_search{"location":  "Nagaland"}
    - slot{"location":  "Nagaland"}
    - action_check_location
    - slot{"location":  "Nagaland"}
    - slot{"location_verified":false}
    - utter_ask_location
    
## 29. cuisine and budget specified ok results deny
* greet
    - utter_greet
* restaurant_search{"cuisine": "American", "budget": "Lesser than Rs.300"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"cuisine": "American"}
    - slot{"cuisine_verified": true}
    - slot{"budget": "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget": "Lesser than Rs.300"}
    - utter_ask_location
* restaurant_search{"location":  "Ludhiana"}
    - slot{"location":  "Ludhiana"}
    - action_check_location
    - slot{"location":  "Ludhiana"}
    - slot{"location_verified":true}
    - action_search_restaurants
    - slot{"location":  "Ludhiana"}
    - slot{"cuisine": "American"}
    - slot{"budget": "Lesser than Rs.300"}
    - slot{"found_restaurants":false}
    - action_check_continuity
    
## 30. cuisine and budget specified ok results deny, no greet
* restaurant_search{"cuisine": "American", "budget": "Lesser than Rs.300"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"cuisine": "American"}
    - slot{"cuisine_verified": true}
    - slot{"budget": "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget": "Lesser than Rs.300"}
    - utter_ask_location
* restaurant_search{"location":  "Madurai"}
    - slot{"location":  "Madurai"}
    - action_check_location
    - slot{"location":  "Madurai"}
    - slot{"location_verified":true}
    - action_search_restaurants
    - slot{"location":  "Madurai"}
    - slot{"cuisine": "American"}
    - slot{"budget": "Lesser than Rs.300"}
    - slot{"found_restaurants":false}
    - action_check_continuity
    
## 31. happy path, location and budget specified affirmative
* greet
    - utter_greet
* restaurant_search{"budget": "Rs.300 to 700", "location": "Chennai"}
    - slot{"budget": "Rs.300 to 700"}
    - action_check_budget
    - slot{"budget": "Rs.300 to 700"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"location": "Chennai"}
    - slot{"location_verified":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine":  "South Indian"}
    - slot{"cuisine":  "South Indian"}
    - action_check_cuisine
    - slot{"cuisine": "South Indian"}
    - slot{"cuisine_verified": true}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - slot{"cuisine":  "South Indian"}
    - slot{"budget": "Rs.300 to 700"}
    - slot{"found_restaurants":true}
    - slot{"emailbody":"value"}
    - action_check_continuity
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailId":"brick@gmail.com"}
    - slot{"emailId":"brick@gmail.com"}
    - action_mail_customer   
    - utter_sent_email
    - utter_useful_info
    - utter_goodbye
    
## 32. happy path, location and budget specified affirmative, no greet
* restaurant_search{"budget": "Rs.300 to 700", "location": "Nellore"}
    - slot{"budget": "Rs.300 to 700"}
    - slot{"location": "Nellore"}
    - action_check_location
    - slot{"location": "Nellore"}
    - slot{"location_verified":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine":  "South Indian"}
    - slot{"cuisine":  "South Indian"}
    - action_check_cuisine
    - slot{"cuisine": "South Indian"}
    - slot{"cuisine_verified": true}
    - action_search_restaurants
    - slot{"location": "Nellore"}
    - slot{"cuisine":  "South Indian"}
    - slot{"budget": "Rs.300 to 700"}
    - slot{"found_restaurants":true}
    - slot{"emailbody":"value"}
    - action_check_continuity
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailId":"brick@gmail.com"}
    - slot{"emailId":"brick@gmail.com"}
    - action_mail_customer   
    - utter_sent_email
    - utter_useful_info
    - utter_goodbye


## 33. happy path, location and budget specified affirmative, no mail
* greet
    - utter_greet
* restaurant_search{"budget": "Rs.300 to 700", "location": "Pondicherry"}
    - slot{"budget": "Rs.300 to 700"}
    - action_check_budget
    - slot{"budget": "Rs.300 to 700"}
    - slot{"location": "Pondicherry"}
    - action_check_location
    - slot{"location": "Pondicherry"}
    - slot{"location_verified":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine":  "South Indian"}
    - slot{"cuisine":  "South Indian"}
    - action_check_cuisine
    - slot{"cuisine": "South Indian"}
    - slot{"cuisine_verified": true}
    - action_search_restaurants
    - slot{"location": "Pondicherry"}
    - slot{"cuisine":  "South Indian"}
    - slot{"budget": "Rs.300 to 700"}
    - slot{"found_restaurants":true}
    - slot{"emailbody":"value"}
    - action_check_continuity
    - utter_ask_sendmail
* deny
    - utter_useful_info
    - utter_goodbye
    
## 34. happy path, location and budget specified affirmative, no mail, no greet
* restaurant_search{"budget": "Rs.300 to 700", "location": "Shimla"}
    - slot{"budget": "Rs.300 to 700"}
    - action_check_budget
    - slot{"budget": "Rs.300 to 700"}
    - slot{"location": "Shimla"}
    - action_check_location
    - slot{"location": "Shimla"}
    - slot{"location_verified":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine":  "South Indian"}
    - slot{"cuisine":  "South Indian"}
    - action_check_cuisine
    - slot{"cuisine": "South Indian"}
    - slot{"cuisine_verified": true}
    - action_search_restaurants
    - slot{"location": "Shimla"}
    - slot{"cuisine":  "South Indian"}
    - slot{"budget": "Rs.300 to 700"}
    - slot{"found_restaurants":true}
    - slot{"emailbody":"value"}
    - action_check_continuity
    - utter_ask_sendmail
* deny
    - utter_useful_info
    - utter_goodbye
    
## 35. location and budget specified deny
* greet
    - utter_greet
* restaurant_search{"budget": "Rs.300 to 700", "location": "Ludhiana"}
    - slot{"budget": "Rs.300 to 700"}
    - action_check_budget
    - slot{"budget": "Rs.300 to 700"}
    - slot{"location": "Ludhiana"}
    - action_check_location
    - slot{"location": "Ludhiana"}
    - slot{"location_verified":false}
    - utter_ask_location
    
## 36. location and budget specified deny, no greet
* restaurant_search{"budget": "Rs.300 to 700", "location": "Thrissur"}
    - slot{"budget": "Rs.300 to 700"}
    - action_check_budget
    - slot{"budget": "Rs.300 to 700"}
    - slot{"location": "Thrissur"}
    - action_check_location
    - slot{"location": "Thrissur"}
    - slot{"location_verified":false}
    - utter_ask_location


## 37. location and budget specified ok results deny
* greet
    - utter_greet
* restaurant_search{"budget": "Rs.300 to 700", "location": "Vadodara"}
    - slot{"budget": "Rs.300 to 700"}
    - action_check_budget
    - slot{"budget": "Rs.300 to 700"}
    - slot{"location": "Vadodara"}
    - action_check_location
    - slot{"location": "Vadodara"}
    - slot{"location_verified":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine":  "Mexican"}
    - slot{"cuisine":  "Mexican"}
    - action_check_cuisine
    - slot{"cuisine": "Mexican"}
    - slot{"cuisine_verified": true}
    - action_search_restaurants
    - slot{"location": "Vadodara"}
    - slot{"cuisine":  "Mexican"}
    - slot{"budget": "Rs.300 to 700"}
    - slot{"found_restaurants":false}
    - action_check_continuity

## 38. location and budget specified ok results deny, no greet
* restaurant_search{"budget": "Rs.300 to 700", "location": "Warangal"}
    - slot{"budget": "Rs.300 to 700"}
    - action_check_budget
    - slot{"budget": "Rs.300 to 700"}
    - slot{"location": "Warangal"}
    - action_check_location
    - slot{"location": "Warangal"}
    - slot{"location_verified":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine":  "Mexican"}
    - slot{"cuisine":  "Mexican"}
    - action_check_cuisine
    - slot{"cuisine": "Mexican"}
    - slot{"cuisine_verified": true}
    - action_search_restaurants
    - slot{"location": "Warangal"}
    - slot{"cuisine":  "Mexican"}
    - slot{"budget": "Rs.300 to 700"}
    - slot{"found_restaurants":false}
    - action_check_continuity

## 39. say goodbye
* goodbye
  - utter_goodbye

## 40. say greet and goodbye
* greet
  - utter_greet
* goodbye
  - utter_goodbye

## 41. happy path, location specified, invalid cuisine 
* greet
  - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_verified":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "kasmiri"}
    - slot{"cuisine": "kasmiri"}
    - action_check_cuisine
    - slot{"cuisine_verified":false}
    - slot{"cuisine": null}

## 42. happy path, cuisine specified, invalid cuisine 
* greet
    - utter_greet
* restaurant_search{"cuisine": "kasmiri"}
    - slot{"cuisine": "kasmiri"}
    - action_check_cuisine
    - slot{"cuisine_verified":false}
    - slot{"cuisine": null}
    
## 43. happy path, budget specified, invalid cuisine 
* greet
  - utter_greet
* restaurant_search{"budget":  "Lesser than Rs.300"}
    - slot{"budget":  "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget":  "Lesser than Rs.300"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_verified":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "kasmiri"}
    - slot{"cuisine": "kasmiri"}
    - action_check_cuisine
    - slot{"cuisine_verified":false}
    - slot{"cuisine": null}

## 44. happy path, location specified, no greet, invalid cuisine 
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mysore"}
    - slot{"location": "mysore"}
    - action_check_location
    - slot{"location": "mysore"}
    - slot{"location_verified":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "kasmiri"}
    - slot{"cuisine": "kasmiri"}
    - action_check_cuisine
    - slot{"cuisine_verified":false}
    - slot{"cuisine": null}
    
## 45. happy path, cuisine specified, no greet,invalid cuisine 
* restaurant_search{"cuisine": "kasmiri"}
    - slot{"cuisine": "kasmiri"}
    - action_check_cuisine
    - slot{"cuisine_verified":false}
    - slot{"cuisine": null}
    
## 46. happy path, budget specified, no greet, invalid cuisine 
* restaurant_search{"budget":  "Lesser than Rs.300"}
    - slot{"budget":  "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget":  "Lesser than Rs.300"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_verified":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "kasmiri"}
    - slot{"cuisine": "kasmiri"}
    - action_check_cuisine
    - slot{"cuisine_verified":false}
    - slot{"cuisine": null}
    
## 47. happy path, cuisine and location specified affirmative, invalid cuisine 
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Meerut"}
    - slot{"cuisine": "Mexican"}
    - action_check_cuisine
    - slot{"cuisine_verified":false}
    - slot{"cuisine": null}
    
## 48. happy path, cuisine and location specified affirmative, no greet, invalid cuisine 
* restaurant_search{"cuisine": "Mexican", "location": "Bhilai"}
    - slot{"cuisine": "Mexican"}
    - action_check_cuisine
    - slot{"cuisine_verified":false}
    - slot{"cuisine": null}
    
## 49. happy path, cuisine and budget specified affirmative, invalid cuisine 
* greet
    - utter_greet
* restaurant_search{"cuisine": "American", "budget": "Lesser than Rs.300"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"cuisine_verified":false}
    - slot{"cuisine": null}

## 50. happy path, cuisine and budget specified affirmative, no greet, invalid cuisine 
* restaurant_search{"cuisine": "American", "budget": "Lesser than Rs.300"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"cuisine_verified":false}
    - slot{"cuisine": null}
    
## 51. happy path, location and budget specified affirmative, invalid cuisine
* greet
    - utter_greet
* restaurant_search{"budget": "Rs.300 to 700", "location": "Chennai"}
    - slot{"budget": "Rs.300 to 700"}
    - action_check_budget
    - slot{"budget": "Rs.300 to 700"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"location": "Chennai"}
    - slot{"location_verified":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine":  "South Indian"}
    - slot{"cuisine":  "South Indian"}
    - action_check_cuisine
    - slot{"cuisine_verified":false}
    - slot{"cuisine": null}
    
## 52. happy path, location and budget specified affirmative, no greet, invalid cuisine
* restaurant_search{"budget": "Rs.300 to 700", "location": "Nellore"}
    - slot{"budget": "Rs.300 to 700"}
    - action_check_budget
    - slot{"budget": "Rs.300 to 700"}
    - slot{"location": "Nellore"}
    - action_check_location
    - slot{"location": "Nellore"}
    - slot{"location_verified":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine":  "South Indian"}
    - slot{"cuisine":  "South Indian"}
    - action_check_cuisine
    - slot{"cuisine_verified":false}
    - slot{"cuisine": null}
    
## 53. happy path, invalid budget 
* greet
  - utter_greet
* restaurant_search{"budget":  "Lesser than Rs.300"}
    - slot{"budget":  "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget":  null}
    
## 54. happy path, invalid budget, no greet
* restaurant_search{"budget":  "Lesser than Rs.300"}
    - slot{"budget":  "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget":  null}
    
## 55. happy path, cuisine and budget specified, invalid budget 
* greet
    - utter_greet
* restaurant_search{"cuisine": "American", "budget": "Lesser than Rs.300"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"cuisine_verified":true}
    - slot{"cuisine": "American"}
    - slot{"budget":  "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget":  null}
    
## 56. happy path, cuisine and budget specified, invalid budget, no greet 
* restaurant_search{"cuisine": "American", "budget": "Lesser than Rs.300"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"cuisine_verified":true}
    - slot{"cuisine": "American"}
    - slot{"budget":  "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget":  null}
    
## 57. happy path, location and budget specified, invalid budget
* greet
    - utter_greet
* restaurant_search{"budget": "Rs.300 to 700", "location": "Chennai"}
    - slot{"budget": "Rs.300 to 700"}
    - action_check_budget
    - slot{"budget":  null}

## 58. happy path, cuisine and location specified, invalid budget
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Firozabad"}
    - slot{"cuisine": "Mexican"}
    - action_check_cuisine
    - slot{"cuisine": "Mexican"}
    - slot{"cuisine_verified": true}
    - slot{"location": "Firozabad"}
    - action_check_location
    - slot{"location": "Firozabad"}
    - slot{"location_verified":true}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_check_budget
    - slot{"budget":  null}
    
## 59. happy path, cuisine and location specified, invalid budget, no greet
* restaurant_search{"cuisine": "Mexican", "location": "Firozabad"}
    - slot{"cuisine": "Mexican"}
    - action_check_cuisine
    - slot{"cuisine": "Mexican"}
    - slot{"cuisine_verified": true}
    - slot{"location": "Firozabad"}
    - action_check_location
    - slot{"location": "Firozabad"}
    - slot{"location_verified":true}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_check_budget
    - slot{"budget":  null}
    
## 60. happy path, location specified , invalid budget
* greet
  - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_verified":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_verified": true}
    - utter_ask_budget
* restaurant_search{"budget":  "Lesser than Rs.300"}
    - slot{"budget":  "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget":  null}
    
## 61. happy path, location specified, invalid budget, no greet 
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_verified":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_verified": true}
    - utter_ask_budget
* restaurant_search{"budget":  "Lesser than Rs.300"}
    - slot{"budget":  "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget":  null}
    
## 62. happy path, cuisine specified, invalid budget 
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_verified": true}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_verified":true}
    - utter_ask_budget
* restaurant_search{"budget":  "Lesser than Rs.300"}
    - slot{"budget":  "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget":  null}
    
## 63. happy path, cuisine specified, invalid budget, no greet 
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"cuisine_verified": true}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_verified":true}
    - utter_ask_budget
* restaurant_search{"budget":  "Lesser than Rs.300"}
    - slot{"budget":  "Lesser than Rs.300"}
    - action_check_budget
    - slot{"budget":  null}
    
    
## 64. say welcome
* gratitude
  - utter_welcome

## 65. say greet and welcome
* greet
  - utter_greet
* gratitude
  - utter_welcome

