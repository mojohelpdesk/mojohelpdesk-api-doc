mojohelpdesk-api-doc
====================

## WORKING IN PROGRESS...
While we are migrating it to Github, please find the doc API here:
 - https://help.mojohelpdesk.com/help/topic/129798
 

==
This is the official Mojo Helpdesk API documentation.  Learn about Mojo Helpdesk at www.mojohelpdesk.com.


Mojo Helpdesk is a product of Metadot. www.metadot.com.

==

Replace 'mysupport.mojohelpdesk.com' with your helpdesk address, and access_key parameter with your access key (it can be found in your profile).

## Mojo Helpdesk API documentation
 
The Mojo Helpdesk API can return XML or JSON. It requires an access key that is found in the Mojo Helpdesk user profile.

## Tickets
### List tickets

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets?access_key=9c9745101d12aed4d5a67d43747824451f9251d4
    
    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets.xml?access_key=9c9745101d12aed4d5a67d43747824451f9251d4
    
    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets.json?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

 

### List of tickets supports paging, with optional parameters per_page and page parameters. If per_page is missing, by default it will return 30 items per page:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets?access_key=9c9745101d12aed4d5a67d43747824451f9251d4\&per_page=20\&page=3

 

###  Show ticket

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets/88?access_key=9c9745101d12aed4d5a67d43747824451f9251d4
    
    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets/88.xml?access_key=9c9745101d12aed4d5a67d43747824451f9251d4
    
    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets/88.json?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

 

### Create ticket

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X POST -d "<ticket><title>Test ticket</title><description>Testing API for ticket creation</description><ticket_queue_id>8</ticket_queue_id><priority_id>30</priority_id></ticket>"

###  Update ticket

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets/113?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X PUT -d "<ticket><title>Test ticket API</title></ticket>"

 

### Destroy ticket

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets/113?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X DELETE

### List of input fields  

 - title
 - description
 - ticket_queue_id
 - priority_id
   - 10 emergency 
   - 20 urgent 
   - 30 normal
   - 40 low 
 - status_id  
   - 10 new 
   - 15 assigned
   - 20 in progress
   - 30 on hold
   - 40 information requested
   - 50 solved
   - 60 closed
 - assigned_to_id
 - custom_field_XXX (where XXX is the name of the custom field, i.e. custom_field_my_awesome_field)
 - user_id

## Ticket comments
### Listing comments for a ticket:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets/114/comments?access_key=9c9745101d12aed4d5a67d43747824451f9251d4
    
    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets/114/comments.xml?access_key=9c9745101d12aed4d5a67d43747824451f9251d4
    
    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets/114/comments.json?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

 

### Create comment:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets/88/comments?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X POST -d "<comment><body>New comment</body></comment>"

### Comment input fields  

 - body
 - is_private
 - time_spent

 


