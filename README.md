# Mojo Helpdesk API Documentation

Mojo Helpdesk (www.MojoHelpdesk.com) is a ticket tracking service developed by Metadot. This document describes its public API.


## About Mojo Helpdesk API

Mojo Helpdesk API is simplistic and very easy to use. Mojo Helpdesk API allows 3rd party developers to build web, desktop, and server applications or simple scripts that can communicate directly with the Mojo Helpdesk service. The communication is done by using `RESTful` `HTTP` requests and `XML` or `JSON` responses and requires that all requests are ascii encoded.

## Authentication

In the code below, replace `mysupport.mojohelpdesk.com` with your helpdesk address, and `access_key` parameter with your access key (it can be found in your profile).
 
The Mojo Helpdesk API can return XML or JSON. It requires an access key that is found in the Mojo Helpdesk user profile.


## Tickets
### List tickets

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets?access_key=9c9745101d12aed4d5a67d43747824451f9251d4
    
    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets.xml?access_key=9c9745101d12aed4d5a67d43747824451f9251d4
    
    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets.json?access_key=9c9745101d12aed4d5a67d43747824451f9251d4



List of tickets API call supports **paging**, with optional parameters `per_page` and `page` parameters. `per_page` default value is 30, the maximum - 100:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets?access_key=9c9745101d12aed4d5a67d43747824451f9251d4\&per_page=20\&page=3

Sorting parameters:
  - **sort_by** - id, title, description, user_id, assigned_to_id, status_id, ticket_form_id, priority_id, ticket_queue_id, company_id, rating, rated_on, created_on, updated_on, status_changed_on, solved_on, assinged_on, ticket_type_id, due_on, scheduled_on
  - **sort_order** - asc, desc
 
Default sorting is by 'id', descending. 
 

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

 - title - String
 - description - String
 - ticket_queue_id - Integer
 - priority_id - Integer
   - 10 emergency 
   - 20 urgent 
   - 30 normal
   - 40 low 
 - status_id - Integer
   - 10 new 
   - 20 in progress
   - 30 on hold
   - 40 information requested
   - 50 solved
   - 60 closed
 - ticket_type_id - Integer
 - assigned_to_id - Integer
 - ticket_form_id - Integer (if omitted, the default form would be used)
 - custom_field_XXX - String (where XXX is the name of the custom field, i.e. custom_field_my_awesome_field)
 - user_id - Integer
 - cc - String


## Ticket comments
### Listing comments for a ticket:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets/114/comments?access_key=9c9745101d12aed4d5a67d43747824451f9251d4
    
    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets/114/comments.xml?access_key=9c9745101d12aed4d5a67d43747824451f9251d4
    
    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets/114/comments.json?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

 

### Create comment:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets/88/comments?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X POST -d "<comment><body>New comment</body></comment>"

### Comment input fields  

 - body - String
 - is_private - Boolean
 - time_spent - Integer
 - cc - String

### Additional parameters

 - suppress_user_notification - Boolean
 


## Ticket search

The last part of the urls is the search query - the format is the same as the one generated for 
the advanced search on the web interface. Note the usage of `%20` instead 
of space, `\&` instead of just `&`, `\(` instead of `(`, `\<` instead of `<`.

Additional url params:

 - `sf` - sort field name (same as the web form search, i.e. priority_id)
 - `r` - 0/1 - reverse sort
 - `per_page` - results per page (default 10, min 10)
 - `page`  - page number (default 1)

#### All open tickets:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets/search?query=status.id:\(\<50\)\&sf=created_on\&r=0\&access_key=9c9745101d12aed4d5a67d43747824451f9251d4

#### All urgent open tickets:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets/search?query=priority.id:\(\<=20\)%20AND%20status.id:\(\<50\)&sf=created_on\&r=0\&access_key=9c9745101d12aed4d5a67d43747824451f9251d4

#### All open tickets in certain queue:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/tickets/search?query=queue.id:19647%20AND%20status.id:\(\<50\)\&sf=created_on\&r=0\&access_key=9c9745101d12aed4d5a67d43747824451f9251d4

#### List of searchable fields:

 - assignee.id
 - assignee.name
 - assignee.email
 - comments.id
 - comments.body
 - comments.created_on
 - comments.time_spent
 - comments.user.id
 - comments.user.name
 - comments.user.email
 - company.id
 - company.name
 - created_by.id
 - created_by.name
 - created_by.email
 - created_on
 - custom_fields
 - description
 - due_on
 - priority.id
 - priority.name
 - queue.id
 - queue.name
 - rating
 - rated_on
 - scheduled_on
 - solved_on
 - status.id
 - status.name
 - status_changed_on
 - type.id
 - type.name
 - title
 - updated_on


#### Search notes:

 - Format of all date fields is: 2013-11-11T21:37:02Z
 - To search for range of date/time (i.e. for created_on field): 
  - created_on:\[2013-11-11T21:37:02Z TO *\] (for dates after the given)
  - created_on:\[* TO 2013-11-11T21:37:02Z\] (for dates before the given)
  - created_on:\[2013-10-11T21:37:02Z TO 2013-11-11T21:37:02Z\] (for dates between the given)
 - Surround all string values with parentheses and double quotes like the following examples:
  - created_by.email:("myemail@somedomain.com")
  - company.name:("My Company, Ltd")
  - comments.user.email:("tester@mycompany.com")
  

## Ticket queues


### List of ticket queues:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/ticket_queues?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/ticket_queues.xml?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/ticket_queues.json?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

 

### List of ticket queues supports paging, with optional parameters per_page and page parameters. If per_page is missing, by default it will return 30 items per page:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/ticket_queues?access_key=9c9745101d12aed4d5a67d43747824451f9251d4\&per_page=10\&page=2

 

### Show ticket queue:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/ticket_queues/8?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

 

### Create ticket queue:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/ticket_queues?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X POST -d "<ticket_queue><name>My queue</name></ticket_queue>"

 

### Update ticket queue:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/ticket_queues/11?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X PUT -d "<ticket_queue><name>My precios queue</name></ticket_queue>"

 

### Destroy ticket queue:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/ticket_queues/10?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X DELETE

### List of input fields  

 - `name`
 - `email_alias`
 - `email_forward`


## Groups (formerly called companies)


### List of companies:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/companies?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/companies.xml?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/companies.json?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

 

### List of companies supports paging, with optional parameters per_page and page parameters. If per_page is missing, by default it will return 30 items per page:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/companies?access_key=9c9745101d12aed4d5a67d43747824451f9251d4\&per_page=10\&page=2

 

### Create company:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/companies?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X POST -d "<company><name>My very own company</name></company>"

 

### Update company:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/companies/1999?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X PUT -d "<company><website-url>www.google.com</website-url></company>"

 

### Destroy company:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/companies/1999?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X DELETE

### List of input fields  

 - name
 - primary_contact_id (ID of existing helpdesk user)
 - billing_contact_id (ID of existing helpdesk user)
 - support_level_id
 - support_status_id (0 - active, 1 - delinquent)
 - support_start_date
 - support_end_date
 - support_info_url
 - address
 - address2
 - city
 - state
 - zip
 - country
 - website_url
 - notes
  
 
## Users


### List of users:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/users?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/users.xml?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/users.json?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

### List of agents:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/users/techs?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/users/techs.xml?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

 
### List of users supports paging, with optional parameters per_page and page parameters. If per_page is missing, by default it will return 30 items per page:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/users?access_key=9c9745101d12aed4d5a67d43747824451f9251d4\&per_page=10\&page=2

 

### Show user:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/users/1?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/users/1.xml?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/users/1.json?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

### Get user by email address:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/users/get_by_email?email=someone@company.com&access_key=9c9745101d12aed4d5a67d43747824451f9251d4

### Create user:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/users?access_key=9c9745101d12aed4d5a67d43747824451f9251d4\&send_welcome_email=1 -X POST -d "<user><email>ivaylo@metadot.com</email><first_name>Ivaylo</first_name><last_name>Georgiev</last_name><company_id>888</company_id><password>111111</password></user>"



### Update user:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/users/1999?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X PUT -d "<user><user_notes>Thats me again.</user_notes></user>"

 

### Destroy user:

    curl -H 'Accept: application/xml' -H 'Content-type: application/xml' http://mysupport.mojohelpdesk.com/api/users/1999?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X DELETE



### List of input fields  

 - email
 - first_name
 - last_name
 - work_phone
 - cell_phone
 - home_phone
 - user_notes
 - company_id
 - password
 - is_active
 - role_id



### role_id values:

 - 10 - regular user
 - 15 - restricted technician
 - 20 - technician
 - 30 - manager
 - 35 - admin
 - 40 - owner
  
 
