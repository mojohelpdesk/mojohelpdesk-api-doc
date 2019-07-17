# Mojo Helpdesk API v2 Documentation

Mojo Helpdesk (www.MojoHelpdesk.com) is a ticket tracking service developed by
Metadot. This document describes its public API v2. [API v1](https://github.com/mojohelpdesk/mojohelpdesk-api-doc/tree/master/v1) is deprecated.

## About Mojo Helpdesk API

Mojo Helpdesk API is easy to use. Mojo Helpdesk API allows
3rd party developers to build web, desktop, and server applications or simple
scripts that can communicate directly with the Mojo Helpdesk service.
The communication is done by using `RESTful` `HTTP` requests in JSON format.
XML is not supported.

## Example usage in Python

A Mojo Helpdesk example API usage Python script is available [here](https://github.com/mojohelpdesk/mojohelpdesk-api-doc/tree/master/examples/python).

## Authentication

In the code below, replace `access_key` parameter with your access key
(it can be found in your profile).

The Mojo Helpdesk API requires an access key that is found
in the Mojo Helpdesk user profile.

## Tickets

### List tickets

    curl https://app.mojohelpdesk.com/api/v2/tickets?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

List of tickets API call supports **paging**, with optional parameters
`per_page` and `page` parameters. `per_page` default value is 30, the maximum - 100:

    curl https://app.mojohelpdesk.com/api/v2/tickets?access_key=9c9745101d12aed4d5a67d43747824451f9251d4\&per_page=20\&page=3

Sorting parameters:

- **sort_by** - id, title, description, user_id, assigned_to_id, status_id,
ticket_form_id, priority_id, ticket_queue_id, company_id, rating, rated_on,
created_on, updated_on, status_changed_on, solved_on, assigned_on,
ticket_type_id, due_on, scheduled_on
- **sort_order** - asc, desc

Default sorting is by 'id', descending.

### Show ticket

    curl https://app.mojohelpdesk.com/api/v2/tickets/88?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

### Create ticket

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/tickets?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X POST -d '{"title":"Test ticket","description":"Testing API for ticket creation","ticket_queue_id":"8","priority_id":"30"}'

### Update ticket

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/tickets/113?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X PUT -d '{"title":"Test ticket API"}'

### List of events for a ticket

    curl https://app.mojohelpdesk.com/api/v2/tickets/113/events?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

### Add tag to a ticket

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/tickets/113/add_tag?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X POST -d '{"tag_label":"Test"}'

### Remove tag from a ticket

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/tickets/113/remove_tag?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X POST -d '{"tag_label":"Test"}'

### Destroy ticket

    curl https://app.mojohelpdesk.com/api/v2/tickets/113?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X DELETE

### Ticket input fields  

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
- custom_field_XXX - String (where XXX is the name of the custom field,
i.e. custom_field_my_awesome_field)
- user_id - Integer
- cc - String

## Ticket comments

### Listing comments for a ticket

    curl https://app.mojohelpdesk.com/api/v2/tickets/114/comments?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

### Create comment

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/tickets/88/comments?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X POST -d '{"body":"New comment"}'

### Comment input fields  

- body - String
- is_private - Boolean
- time_spent - Integer
- cc - String

### Additional parameters

- suppress_user_notification - Boolean

## Ticket search

The last part of the urls is the search query - the format is the same as the
one generated for the advanced search on the web interface. Note the usage of
`%20` instead of space, `\&` instead of just `&`, `\(` instead of `(`, `\<`
instead of `<`.

Additional url params:

- `sf` - sort field name (same as the web form search, i.e. priority_id)
- `r` - 0/1 - reverse sort
- `per_page` - results per page (default 10, min 10)
- `page`  - page number (default 1)

### All open tickets

    curl https://app.mojohelpdesk.com/api/v2/tickets/search?query=status.id:\(\<50\)\&sf=created_on\&r=0\&access_key=9c9745101d12aed4d5a67d43747824451f9251d4

### All urgent open tickets

    curl https://app.mojohelpdesk.com/api/v2/tickets/search?query=priority.id:\(\<=20\)%20AND%20status.id:\(\<50\)&sf=created_on\&r=0\&access_key=9c9745101d12aed4d5a67d43747824451f9251d4

### All open tickets in certain queue

    curl https://app.mojohelpdesk.com/api/v2/tickets/search?query=queue.id:19647%20AND%20status.id:\(\<50\)\&sf=created_on\&r=0\&access_key=9c9745101d12aed4d5a67d43747824451f9251d4

### All tickets with due date

    curl https://app.mojohelpdesk.com/api/v2/tickets/search?query=_exists_:due_on\&sf=created_on\&r=0\&access_key=9c9745101d12aed4d5a67d43747824451f9251d4

### List of searchable fields

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

#### Search notes

- Format of all date fields is: 2013-11-11T21:37:02Z
- To search for range of date/time (i.e. for created_on field):
  - created_on:\[2013-11-11T21:37:02Z TO *\] (for dates after the given)
  - created_on:\[* TO 2013-11-11T21:37:02Z\] (for dates before the given)
  - created_on:\[2013-10-11T21:37:02Z TO 2013-11-11T21:37:02Z\] (for dates
between the given)
  - Surround all string values with parentheses and double quotes like the
following examples:
  - created_by.email:("myemail@somedomain.com")
  - company.name:("My Company, Ltd")
  - comments.user.email:("tester@mycompany.com")
  
## Ticket queues

### List of ticket queues

    curl https://app.mojohelpdesk.com/api/v2/ticket_queues?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

### List of ticket queues supports paging, with optional parameters per_page and page parameters. If per_page is missing, by default it will return 30 items per page

    curl https://app.mojohelpdesk.com/api/v2/ticket_queues?access_key=9c9745101d12aed4d5a67d43747824451f9251d4\&per_page=10\&page=2

### Show ticket queue

    curl https://app.mojohelpdesk.com/api/v2/ticket_queues/8?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

### Create ticket queue

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/ticket_queues?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X POST -d '{"name":"My queue"}'

### Update ticket queue

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/ticket_queues/11?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X PUT -d '{"name":"My precios queue"}'

### Destroy ticket queue

    curl https://app.mojohelpdesk.com/api/v2/ticket_queues/10?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X DELETE

### Ticket queue of input fields

- name
- email_alias
- email_forward

## Groups (formerly called companies)

### List of groups

    curl https://app.mojohelpdesk.com/api/v2/groups?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

### List of groups supports paging, with optional parameters per_page and page parameters. If per_page is missing, by default it will return 30 items per page

    curl https://app.mojohelpdesk.com/api/v2/groups?access_key=9c9745101d12aed4d5a67d43747824451f9251d4\&per_page=10\&page=2

### Create group

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/groups?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X POST -d '{"name":"My very own group"}'

### Update group

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/groups/1999?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X PUT -d '{"website-url":"www.google.com"}'

### Destroy group

    curl https://app.mojohelpdesk.com/api/v2/groups/1999?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X DELETE

### Group input fields  

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

### List of users

    curl https://app.mojohelpdesk.com/api/v2/users?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

### List of agents

    curl https://app.mojohelpdesk.com/api/v2/users/techs?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

### List of users supports paging, with optional parameters per_page and page parameters. If per_page is missing, by default it will return 30 items per page

    curl https://app.mojohelpdesk.com/api/v2/users?access_key=9c9745101d12aed4d5a67d43747824451f9251d4\&per_page=10\&page=2

### Show user

    curl https://app.mojohelpdesk.com/api/v2/users/1?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

### Get user by email address

    curl https://app.mojohelpdesk.com/api/v2/users/get_by_email?email=someone@company.com&access_key=9c9745101d12aed4d5a67d43747824451f9251d4

### Create user

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/users?access_key=9c9745101d12aed4d5a67d43747824451f9251d4\&send_welcome_email=1 -X POST -d '{"email":"ivaylo+test@metadot.com","first_name":"Ivaylo","last_name":"Georgiev","company_id":"888","password":"111111"}'

### Update user

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/users/1999?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X PUT -d '{"user_notes":"Thats me again."}'

### Destroy user

    curl https://app.mojohelpdesk.com/api/v2/users/1999?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X DELETE

### User input fields  

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

### role_id values

- 10 - regular user
- 15 - restricted technician
- 20 - technician
- 30 - manager
- 35 - admin
- 40 - owner
  
## Ticket tags

### List of ticket tags

    curl https://app.mojohelpdesk.com/api/v2/tags?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

### List of tags supports paging, with optional parameters per_page and page parameters. If per_page is missing, by default it will return 30 items per page

    curl https://app.mojohelpdesk.com/api/v2/tags?access_key=9c9745101d12aed4d5a67d43747824451f9251d4\&per_page=10\&page=2

### Show tag

    curl https://app.mojohelpdesk.com/api/v2/tags/8?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

### Create tag

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/tags?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X POST -d '{"label":"Test","color":"#777777"}'

### Update tag

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/tags/11?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X PUT -d '{"color":"#ff0000"}'

### Destroy tag

    curl https://app.mojohelpdesk.com/api/v2/tags/10?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X DELETE

### Tag input fields  

- label
- color

## Ticket tasks

### List of ticket tasks

    curl https://app.mojohelpdesk.com/api/v2/tickets/88/tasks?access_key=9c9745101d12aed4d5a67d43747824451f9251d4

### Create ticket task

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/tickets/88/tasks?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X POST -d '{"title":"Test"}'

### Update ticket task

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/tickets/88/tasks/777?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X PUT -d '{"notes":"Help"}'

### Destroy ticket task

    curl https://app.mojohelpdesk.com/api/v2/tickets/88/tasks/777?access_key=9c9745101d12aed4d5a67d43747824451f9251d4 -X DELETE

### Task input fields  

- title
- notes
- is_completed
