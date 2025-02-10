# Mojo Helpdesk API v2 Documentation

[![Services Health](https://mojohelpdesk.montastic.io/badge)](https://mojohelpdesk.montastic.io)

[Mojo Helpdesk](https://www.mojohelpdesk.com) is a ticket tracking software as a service (Saas).
It is developed by [Metadot](https://www.metadot.com).

This document describes its public API v2. API v1 is deprecated.

## About Mojo Helpdesk API

Mojo Helpdesk API is easy to use. It allows
3rd party developers to build web, desktop, and server applications or simple
scripts that can communicate directly with the Mojo Helpdesk service.
The communication is done by using `RESTful` `HTTP` requests in `JSON` format.
`XML` is not supported.

## Example usage in Python

A Mojo Helpdesk example API usage Python script is available
[here](https://github.com/mojohelpdesk/mojohelpdesk-api-doc/tree/master/examples/python).

## Authentication

In the code below, replace `access_key` parameter with your access key
(it can be found in your profile).

The Mojo Helpdesk API requires an access key that is found
in the Mojo Helpdesk user profile.

## Requirements

- curl version 8.6 or higher

## Tickets

### List tickets

    curl https://app.mojohelpdesk.com/api/v2/tickets?access_key=XXX

List of tickets API call supports **paging**, with optional parameters
`per_page` and `page` parameters. `per_page` default value is 30, the maximum - 100:

CURL:

    curl https://app.mojohelpdesk.com/api/v2/tickets?access_key=xxx\&per_page=20\&page=3

JavaScript:

    const Http = new XMLHttpRequest();
    const url='https://app.mojohelpdesk.com/api/v2/tickets?access_key=XXX';
    Http.open("GET", url);
    Http.setRequestHeader("Content-Type", "application/json");
    Http.send();
    Http.onreadystatechange = (e) => {
      console.log(Http.responseText)
    }

Sorting parameters:

- **sort_by** - id, title, description, user_id, assigned_to_id, status_id,
  ticket_form_id, priority_id, ticket_queue_id, company_id, rating, rated_on,
  created_on, updated_on, status_changed_on, solved_on, assigned_on,
  ticket_type_id, due_on, scheduled_on
- **sort_order** - asc, desc

Default sorting is by 'id', descending.

### Show ticket

CURL:

    curl https://app.mojohelpdesk.com/api/v2/tickets/123456?access_key=XXX

JavaScript:

    const Http = new XMLHttpRequest();
    const url='https://app.mojohelpdesk.com/api/v2/tickets/123456?access_key=XXX';
    Http.open("GET", url);
    Http.setRequestHeader("Content-Type", "application/json");
    Http.send();
    Http.onreadystatechange = (e) => {
      console.log(Http.responseText)
    }

### Create ticket

CURL:

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/tickets?access_key=XXX -X POST -d '{"title":"Test ticket","description":"Testing API for ticket creation","ticket_queue_id":"8","priority_id":"30"}'

JavaScript:

    const formData = new FormData();
    formData.append('title', 'Test ticket');
    formData.append('description', 'description');
    formData.append('ticket_queue_id', 8);
    formData.append('priority_id', 30);
    formData.append('access_key', 'XXX');

    const Http = new XMLHttpRequest();
    Http.open("POST", "https://app.mojohelpdesk.com/api/v2/tickets");
    Http.setRequestHeader("Content-Disposition", "multipart/form-data");
    Http.send(formData);

    Http.onreadystatechange = (e) => {
      console.log(Http.responseText)
    }

### Create ticket with attachments

HTML/JavaScript:

    <input type="file" id="file-selector" multiple>
    <button onclick="createTicket()">create ticket</button>
    <script>
      var fileList;
      const fileSelector = document.getElementById('file-selector');
      fileSelector.addEventListener('change', (event) => {
        fileList = event.target.files;
      });
      function createTicket() {
        const formData = new FormData();
        for (let i = 0; i < fileList.length; i++) {
          formData.append('attachment['+i+'][content]', fileList[i]);
        }
        formData.append('title', 'Test ticket');
        formData.append('description', 'description');
        formData.append('ticket_queue_id', 8);
        formData.append('priority_id', 30);
        formData.append('access_key', 'XXX');

        const Http = new XMLHttpRequest();
        Http.open("POST", "http://localhost:3000/api/v2/tickets");
        Http.setRequestHeader("Content-Disposition", "multipart/form-data");
        Http.send(formData);

        Http.onreadystatechange = (e) => {
          console.log(Http.responseText)
        }
      }
    </script>

### Create ticket with user

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/tickets?access_key=XXX -X POST -d '{"title":"Test ticket","description":"Testing API for ticket creation","ticket_queue_id":"8","priority_id":"30", "user":{"email":"customer@someplace.com"}}'

#### Additional parameters for ticket creation

- suppress_user_notification - Boolean when set to `true` will not send any email to notify for the ticket creation

### Update ticket

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/tickets/113?access_key=XXX -X PUT -d '{"title":"Test ticket API"}'

### List of events for a ticket

    curl https://app.mojohelpdesk.com/api/v2/tickets/113/events?access_key=XXX

### Add tag to a ticket

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/tickets/113/add_tag?access_key=XXX -X POST -d '{"tag_label":"Test"}'

### Remove tag from a ticket

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/tickets/113/remove_tag?access_key=XXX -X POST -d '{"tag_label":"Test"}'

### Destroy ticket

    curl https://app.mojohelpdesk.com/api/v2/tickets/113?access_key=XXX -X DELETE

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
- asset_tag - String
- asset_id - Integer

## Ticket comments

### Listing comments for a ticket

    curl https://app.mojohelpdesk.com/api/v2/tickets/114/comments?access_key=XXX

### Create comment

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/tickets/88/comments?access_key=XXX -X POST -d '{"body":"New comment"}'

### Comment input fields

- body - String
- time_spent - Integer
- cc - String

### Additional parameters for comment creation

- suppress_user_notification - Boolean

## Ticket staff notes

### Listing staff notes for a ticket

    curl https://app.mojohelpdesk.com/api/v2/tickets/114/staff_notes?access_key=XXX

### Create staff note

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/tickets/88/staff_notes?access_key=XXX -X POST -d '{"body":"New staff note"}'

### Staff note input fields

- body - String
- cc - String
- time_spent - Integer

## Ticket attachments

### List attachments for a ticket

    curl https://app.mojohelpdesk.com/api/v2/tickets/211402/attachments?access_key=XXX

### Add attachment to a ticket

    curl -F "file=@/home/user/my-file.txt" https://app.mojohelpdesk.com/api/v2/tickets/211402/attachments?staff_only=true\&access_key=XXX -X POST

Additional url params:

- `staff_only` - true/false

### Download an attachment

    curl https://app.mojohelpdesk.com/api/v2/attachments/6422878?access_key=XXX

### Delete an attachment

    curl https://app.mojohelpdesk.com/api/v2/attachments/6422878?access_key=XXX -X DELETE

## Ticket search

The last part of the urls is the search query - the format is the same as the
one generated for the advanced search on the web interface. Note the usage of
`%20` instead of space, `\&` instead of just `&`, `\(` instead of `(`, `\<`
instead of `<`.

Additional url params:

- `sf` - sort field name (same as the web form search, i.e. priority_id)
- `r` - 0/1 - reverse sort
- `per_page` - results per page (default 10, min 10)
- `page` - page number (default 1)

### All open tickets

    curl https://app.mojohelpdesk.com/api/v2/tickets/search?query=status.id:\(\<50\)\&sf=created_on\&r=0\&access_key=XXX

### All urgent open tickets

    curl https://app.mojohelpdesk.com/api/v2/tickets/search?query=priority.id:\(\<=20\)%20AND%20status.id:\(\<50\)&sf=created_on\&r=0\&access_key=XXX

### All open tickets in certain queue

    curl https://app.mojohelpdesk.com/api/v2/tickets/search?query=queue.id:19647%20AND%20status.id:\(\<50\)\&sf=created_on\&r=0\&access_key=XXX

### All tickets with due date

    curl https://app.mojohelpdesk.com/api/v2/tickets/search?query=_exists_:due_on\&sf=created_on\&r=0\&access_key=XXX

### List of sortable fields

- created_on
- due_on
- rated_on
- scheduled_on
- solved_on
- updated_on

### List of searchable fields

- assignee.id
- ~~assignee.name~~ - **DEPRECATED**
  → Retrieve the user ID and use it in the assignee.id search parameter instead.
- assignee.email
- ~~comments.id~~ - **DEPRECATED**
- comments.body
- ~~comments.created_on~~ - **DEPRECATED**
- ~~comments.time_spent~~ - **DEPRECATED**
- ~~comments.user.id~~ - **DEPRECATED**
- ~~comments.user.name~~ - **DEPRECATED**
- ~~comments.user.email~~ - **DEPRECATED**
- company.id
- ~~company.name~~ - **DEPRECATED**
  → Retrieve the company ID and use it in the company.id search parameter instead.
- created_by.id
- created_by.name
- created_by.email
- created_on
- custom_fields
- description
- due_on
- priority.id
- ~~priority.name~~ - **DEPRECATED**
  → Retrieve the priority ID and use it in the priority.id search parameter instead.
- queue.id
- ~~queue.name~~ - **DEPRECATED**
  → Retrieve the queue ID and use it in the queue.id search parameter instead.
- rating
- rated_on
- scheduled_on
- solved_on
- status.id
- ~~status.name~~ - **DEPRECATED**
  → Retrieve the status ID and use it in the status.id search parameter instead.
- status_changed_on
- type.id
- ~~type.name~~ - **DEPRECATED**
  → Retrieve the type ID and use it in the type.id search parameter instead.
- title
- updated_on

#### Search notes

- Format of all date fields is: 2013-11-11T21:37:02Z
- To search for range of date/time (i.e. for created_on field):
  - created_on:\[2013-11-11T21:37:02Z TO \*\] (for dates after the given)
  - created_on:\[\* TO 2013-11-11T21:37:02Z\] (for dates before the given)
  - created_on:\[2013-10-11T21:37:02Z TO 2013-11-11T21:37:02Z\] (for dates
    between the given)
  - Surround all string values with parentheses and double quotes like the
    following examples:
  - created_by.email:("<myemail@somedomain.com>")

## Ticket queues

### List of ticket queues

    curl https://app.mojohelpdesk.com/api/v2/ticket_queues?access_key=XXX

### List of ticket queues supports paging, with optional parameters per_page and page parameters. If per_page is missing, by default it will return 30 items per page

    curl https://app.mojohelpdesk.com/api/v2/ticket_queues?access_key=XXX\&per_page=10\&page=2

### Show ticket queue

    curl https://app.mojohelpdesk.com/api/v2/ticket_queues/8?access_key=XXX

### Create ticket queue

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/ticket_queues?access_key=XXX -X POST -d '{"name":"My queue"}'

### Update ticket queue

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/ticket_queues/11?access_key=XXX -X PUT -d '{"name":"My precious queue"}'

### Destroy ticket queue

    curl https://app.mojohelpdesk.com/api/v2/ticket_queues/10?access_key=XXX -X DELETE

### Ticket queue input fields

- name
- email_alias
- email_forward

## Groups (formerly called companies)

### List of groups

    curl https://app.mojohelpdesk.com/api/v2/groups?access_key=XXX

### List of groups supports paging, with optional parameters per_page and page parameters. If per_page is missing, by default it will return 30 items per page

    curl https://app.mojohelpdesk.com/api/v2/groups?access_key=XXX\&per_page=10\&page=2

### Create group

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/groups?access_key=XXX -X POST -d '{"name":"My very own group"}'

### Update group

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/groups/1999?access_key=XXX -X PUT -d '{"website-url":"www.google.com"}'

### Destroy group

    curl https://app.mojohelpdesk.com/api/v2/groups/1999?access_key=XXX -X DELETE

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

    curl https://app.mojohelpdesk.com/api/v2/users?access_key=XXX

### List of agents

    curl https://app.mojohelpdesk.com/api/v2/users/techs?access_key=XXX

### List of users supports paging, with optional parameters per_page and page parameters. If per_page is missing, by default it will return 30 items per page

    curl https://app.mojohelpdesk.com/api/v2/users?access_key=XXX\&per_page=10\&page=2

### Show user

    curl https://app.mojohelpdesk.com/api/v2/users/1?access_key=XXX

### Get user by email address

    curl https://app.mojohelpdesk.com/api/v2/users/get_by_email?email=someone@company.com&access_key=XXX

### Create user

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/users?access_key=XXX\&send_welcome_email=1 -X POST -d '{"email":"ivaylo+test@metadot.com","first_name":"Ivaylo","last_name":"Georgiev","company_id":"888","password":"111111"}'

### Update user

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/users/1999?access_key=XXX -X PUT -d '{"user_notes":"Thats me again."}'

### Destroy user

    curl https://app.mojohelpdesk.com/api/v2/users/1999?access_key=XXX -X DELETE

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

    curl https://app.mojohelpdesk.com/api/v2/tags?access_key=XXX

### List of tags supports paging, with optional parameters per_page and page parameters. If per_page is missing, by default it will return 30 items per page

    curl https://app.mojohelpdesk.com/api/v2/tags?access_key=XXX\&per_page=10\&page=2

### Show tag

    curl https://app.mojohelpdesk.com/api/v2/tags/8?access_key=XXX

### Create tag

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/tags?access_key=XXX -X POST -d '{"label":"Test","color":"#777777"}'

### Update tag

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/tags/11?access_key=XXX -X PUT -d '{"color":"#ff0000"}'

### Destroy tag

    curl https://app.mojohelpdesk.com/api/v2/tags/10?access_key=XXX -X DELETE

### Tag input fields

- label
- color

## Ticket tasks

### List of ticket tasks

    curl https://app.mojohelpdesk.com/api/v2/tickets/88/tasks?access_key=XXX

### Create ticket task

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/tickets/88/tasks?access_key=XXX -X POST -d '{"title":"Test"}'

### Update ticket task

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/tickets/88/tasks/777?access_key=XXX -X PUT -d '{"notes":"Help"}'

### Destroy ticket task

    curl https://app.mojohelpdesk.com/api/v2/tickets/88/tasks/777?access_key=XXX -X DELETE

### Task input fields

- title
- notes
- is_completed

## Access rights on ticket queues

### List access rights for restricted agents

    curl https://app.mojohelpdesk.com/api/v2/access_rights/restricted_agents?access_key=XXX

### List access rights for groups

    curl https://app.mojohelpdesk.com/api/v2/access_rights/groups?access_key=XXX

### Show access rights for a restricted agent

    curl https://app.mojohelpdesk.com/api/v2/users/1819458/access_rights?access_key=XXX

### Show access rights for a group

    curl https://app.mojohelpdesk.com/api/v2/groups/124147/access_rights?access_key=XXX

### Set access right for a restricted agent on a single queue

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/users/1819458/access_rights?access_key=XXX -X POST -d '{"ticket_queue_id":"94748","has_access":"true"}'

### Set access right for a restricted agent on multiple queues

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/users/1819458/access_rights/set?access_key=XXX -X POST -d '{"keys":["94748","15"],"has_access":"true"}'

### Set access right for a group on a single queue

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/groups/124147/access_rights?access_key=XXX -X POST -d '{"ticket_queue_id":"94748","has_access":"true"}'

### Set access right for a group on all queues

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/groups/124147/access_rights?access_key=XXX -X POST -d '{"has_access_to_all_ticket_queues":"true"}'

### Set access right for a group on multiple queues

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/groups/124147/access_rights/set?access_key=XXX -X POST -d '{"keys":["94748","15"],"has_access":"true"}'

## Ticket forms

### List of ticket forms

    curl https://app.mojohelpdesk.com/api/v2/ticket_forms?access_key=XXX

List all forms with some basic information for them.

### Show ticket forms

    curl https://app.mojohelpdesk.com/api/v2/ticket_forms/2700?access_key=XXX

Returns all relevant information for a form, including the list of field attributes, and field rules.

## Group tickets access for users

### List all groups tickets access for a user

    curl https://app.mojohelpdesk.com/api/v2/users/14/group_access?access_key=XXX

### Get single group tickets access for a user

    curl https://app.mojohelpdesk.com/api/v2/users/14/group_access/1234?access_key=XXX

### Set single group tickets access for a user

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/users/14/group_access/1234?access_key=XXX -X POST -d '{"access":"1"}'

Possible access values:

- 0 - no access
- 1 - full access
- 2 - comment only

## Ticket types

### List of ticket types

    curl https://app.mojohelpdesk.com/api/v2/ticket_types?access_key=XXX

### Show ticket type

    curl https://app.mojohelpdesk.com/api/v2/ticket_type/8?access_key=XXX

### Create ticket type

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/ticket_types?access_key=XXX -X POST -d '{"name":"My type"}'

### Update ticket type

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/ticket_types/11?access_key=XXX -X PUT -d '{"name":"My precious type"}'

### Destroy ticket type

    curl https://app.mojohelpdesk.com/api/v2/ticket_types/10?access_key=XXX -X DELETE

### Ticket type input fields

- name

## Assets Management

### List of assets

    curl https://app.mojohelpdesk.com/api/v2/assets?access_key=XXX

### Show asset

    curl https://app.mojohelpdesk.com/api/v2/assets/1?access_key=XXX

### Create asset

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/assets?access_key=XXX -X POST -d '{"display_name":"My asset", "description":"My very own asset"}'

### Update asset

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/assets/1?access_key=XXX -X PUT -d '{"display_name":"My precious asset"}'

### Destroy asset

    curl https://app.mojohelpdesk.com/api/v2/assets/1?access_key=XXX -X DELETE

### Asset input fields

- asset_tag - string
- serial_number - string
- legacy_reference_number - string
- display_name - string
- description - string
- asset_type_id - integer
- location_id - integer
- department_id - integer
- managed_by_id - integer
- used_by_id - integer
- asset_status_id - integer
- notes - string
- purchased_on - date
- cost - float
- purchase_order_number - string
- vendor - string
- replaced_on - date
- warranty_info - string
- end_of_contract_on - date
- contract_notes - string
- create_ticket_days_before - integer
- birthday - date
- visibility - 'staff_only', 'all_users' or 'logged_in_users'

### Search assets

The last part of the urls is the search query - the format is similar as
the one for ticket search. Note the usage of `%20` instead of space,
`\&` instead of just `&`, `\(` instead of `(`, `\<` instead of `<`.

Url params:

- `query` - the search query
- `sort_field` - sort field name (same as the web form search, i.e. location_name)
- `sort_order` - 'asc' or 'desc'
- `per_page` - results per page (default 10, min 10, max 100)
- `page` - page number (default 1)

Sort fields:

- name
- tag
- asset_type_name
- location_name
- department_name
- managed_by_name
- used_by_name
- status_name
- birthday_sort
- serial_number
- created_on
- updated_on

Searchable fields:

- asset_tag
- display_name
- description
- asset_type.id
- ~~asset_type.name~~ - **DEPRECATED**
  → Retrieve the asset type ID and use it in the asset_type.id search parameter instead.
- location.id
- ~~location.name~~ - **DEPRECATED**
  → Retrieve the location ID and use it in the location.id search parameter instead.
- department.id
- ~~department.name~~ - **DEPRECATED**
  → Retrieve the department ID and use it in the department.id search parameter instead.
- managed_by.email
- managed_by.id
- ~~managed_by.name~~ - **DEPRECATED**
  → Retrieve the user ID and use it in the managed_by.id search parameter instead.
- used_by.email
- used_by.id
- ~~used_by.name~~ - **DEPRECATED**
  → Retrieve the user ID and use it in the used_by.id search parameter instead.
- created_on
- updated_on
- status
- purchased_on
- vendor
- end_of_contract_on
- replaced_on
- serial_number
- birthday

#### Search all assets in certain location

    curl https://app.mojohelpdesk.com/api/v2/assets/search?query=location.id:123\&sort_field=created_on\&sort_order=asc\&access_key=XXX

#### Search all assets which display name has 'laptop' in it

    curl https://app.mojohelpdesk.com/api/v2/assets/search?query=display_name:*laptop*\&sort_field=created_on\&sort_order=asc\&access_key=XXX

### List of asset statuses

    curl https://app.mojohelpdesk.com/api/v2/asset_statuses?access_key=XXX

### Show asset status

    curl https://app.mojohelpdesk.com/api/v2/asset_statuses/1?access_key=XXX

### Create asset status

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/asset_statuses?access_key=XXX -X POST -d '{"name":"My asset type"}'

### Update asset status

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/asset_statuses/1?access_key=XXX -X PUT -d '{"name":"My precious asset type"}'

### Destroy asset status

    curl https://app.mojohelpdesk.com/api/v2/asset_statuses/1?access_key=XXX -X DELETE

### Asset status input fields

- name - string

### List of asset types

    curl https://app.mojohelpdesk.com/api/v2/asset_types?access_key=XXX

### List of asset types in tree order

    curl https://app.mojohelpdesk.com/api/v2/asset_types/tree?access_key=XXX

### Show asset type

    curl https://app.mojohelpdesk.com/api/v2/asset_types/1?access_key=XXX

### Create asset type

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/asset_types?access_key=XXX -X POST -d '{"name":"My asset type", "description":"My very own asset type"}'

### Update asset type

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/asset_types/1?access_key=XXX -X PUT -d '{"name":"My precious asset type"}'

### Destroy asset type

    curl https://app.mojohelpdesk.com/api/v2/asset_types/1?access_key=XXX -X DELETE

### Asset type input fields

- name - string
- description - string
- parent_id - integer

### List of departments

    curl https://app.mojohelpdesk.com/api/v2/departments?access_key=XXX

### List of departments in tree order

    curl https://app.mojohelpdesk.com/api/v2/departments/tree?access_key=XXX

### Show department

    curl https://app.mojohelpdesk.com/api/v2/departments/1?access_key=XXX

### Create department

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/departments?access_key=XXX -X POST -d '{"name":"My department", "description":"My very own department"}'

### Update department

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/departments/1?access_key=XXX -X PUT -d '{"name":"My precious department"}'

### Destroy department

    curl https://app.mojohelpdesk.com/api/v2/departments/1?access_key=XXX -X DELETE

### Department input fields

- name - string
- description - string
- parent_id - integer

### List of locations

    curl https://app.mojohelpdesk.com/api/v2/locations?access_key=XXX

### List of locations in tree order

    curl https://app.mojohelpdesk.com/api/v2/locations/tree?access_key=XXX

### Show location

    curl https://app.mojohelpdesk.com/api/v2/locations/1?access_key=XXX

### Create location

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/locations?access_key=XXX -X POST -d '{"name":"My location", "description":"My very own location"}'

### Update location

    curl -H 'Content-type: application/json' https://app.mojohelpdesk.com/api/v2/locations/1?access_key=XXX -X PUT -d '{"name":"My precious location"}'

### Destroy location

    curl https://app.mojohelpdesk.com/api/v2/locations/1?access_key=XXX -X DELETE

### Location input fields

- name - string
- description - string
- parent_id - integer
