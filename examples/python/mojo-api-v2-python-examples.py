#!/usr/bin/env python

###
# Sample Python script to demo Mojo Helpdesk API for basic CRUD operation.
#
# Setup: pip install requests # do this only once.
#
# This Python script showcases and tests Mojo Helpdesk (https://mojohelpdesk.com) REST API.
# This script lives here: https://github.com/mojohelpdesk/mojohelpdesk-api-doc/tree/master/examples/python
#
# Requirement: use your API key that is located in your Mojo Helpdesk user profile.
#
# Usage - see help: ./mojo-helpdesk-api-tests.py
#
# Public domain.   
#
# Learn more about Mojo Helpdesk: www.mojohelpdesk.com
#
##
import requests  # pip install requests
import sys

dn = 'https://app.mojohelpdesk.com'


#
#
# Print a "." w/o a carriage return
def show_progress():
    sys.stdout.write(".")  # write w/o \n
    sys.stdout.flush()


if len(sys.argv) < 2:
    sys.exit(
        "Usage: %s <access-key> [server domain name (e.g.: http://localhost:3000), default: "
        "https://app.mojohelpdesk.com]" %
        sys.argv[0])

goodKey = sys.argv[1]  # get access key
badKey = "bad"

if len(sys.argv) >= 3:
    dn = sys.argv[2]  # get hostname

print("Using DN: %s" % dn)

#
# Ticket list endpoint / URL
# 
apiUrl = dn + '/api/v2/'

headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

#
# 
# get ticket list w/ good key
show_progress()
r = requests.get(apiUrl + 'tickets?access_key=' + goodKey, headers=headers)
assert r.status_code == 200, "Error getting ticket list. Expected 200, got: %d" % r.status_code

#
# 
# get w/ bad key => error 401
show_progress()
r = requests.get(apiUrl + 'tickets?access_key=' + badKey, headers=headers)
assert r.status_code == 401, "Should get 'not authorized' error, got: %d" % r.status_code

#
# 
# get ticket queue list
show_progress()
r = requests.get(apiUrl + 'ticket_queues?access_key=' + goodKey, headers=headers)
assert r.status_code == 200, "Error getting ticket queue list. Expected 200, got: %d" % r.status_code
ticket_queues = r.json()

#
# 
# get ticket form list
show_progress()
r = requests.get(apiUrl + 'ticket_forms?access_key=' + goodKey, headers=headers)
assert r.status_code == 200, "Error getting ticket form list. Expected 200, got: %d" % r.status_code
ticket_forms = r.json()

#
# 
# create ticket OK
show_progress()
data = {'title': 'Test ticket', 'description': 'Testing API for ticket creation', 'priority_id': 30,
        'ticket_queue_id': ticket_queues[0]['id']}
r = requests.post(apiUrl + 'tickets?access_key=' + goodKey, json=data, headers=headers)
assert r.status_code == 201, "Error creating: expected 201, got: %d." % r.status_code
ticket = r.json()

#
#
# create ticket without email notification OK
show_progress()
data = {'suppress_user_notification': 'true', 'title': 'Test ticket', 'description': 'Testing API for ticket creation',
        'priority_id': 30, 'ticket_queue_id': ticket_queues[0]['id']}
r = requests.post(apiUrl + 'tickets?access_key=' + goodKey, json=data, headers=headers)
assert r.status_code == 201, "Error creating: expected 201, got: %d." % r.status_code
ticket = r.json()

#
#
# create ticket with attachments
show_progress()
data = {
    'title': 'Test ticket',
    'description': 'Testing API for ticket creation',
    'priority_id': 30,
    'ticket_queue_id': ticket_queues[0]['id']
}
files = {
    'attachment[0][content]': open('testfile.txt', 'rb'),
    'attachment[1][content]': open('logo.png', 'rb')
}
r = requests.post(apiUrl + 'tickets?access_key=' + goodKey, files=files, data=data)
assert r.status_code == 201, "Error creating: expected 201, got: %d." % r.status_code
ticket = r.json()

#
# 
# show ticket OK
show_progress()
r = requests.get(apiUrl + 'tickets/%s' % ticket['id'] + '?access_key=' + goodKey, headers=headers)
assert r.status_code == 200, "Error showing: expected 200, got: %d." % r.status_code
ticket = r.json()

#
# 
# update ticket OK
show_progress()
data = {'title': 'Test ticket API'}
r = requests.put(apiUrl + 'tickets/%s' % ticket['id'] + '?access_key=' + goodKey, json=data, headers=headers)
assert r.status_code == 200, "Error updating: expected 200, got: %d." % r.status_code

#
# 
# get agents details OK
show_progress()
r = requests.get(apiUrl + 'users/techs?access_key=' + goodKey, headers=headers)
assert r.status_code == 200, "Error getting list of agents: expected 200, got: %d." % r.status_code
agents = r.json()

#
# 
# get access rights for restricted agents
show_progress()
r = requests.get(apiUrl + 'access_rights/restricted_agents?access_key=' + goodKey, headers=headers)
assert r.status_code == 200, "Error getting access rights for restricted agents. Expected 200, got: %d" % r.status_code
restricted_agents = r.json()

#
# 
# get access rights for groups
show_progress()
r = requests.get(apiUrl + 'access_rights/groups?access_key=' + goodKey, headers=headers)
assert r.status_code == 200, "Error getting access rights for restricted agents. Expected 200, got: %d" % r.status_code
groups = r.json()

#
# 
# assign ticket OK
show_progress()
data = {'assignee_id': agents[0]['id']}
r = requests.put(apiUrl + 'tickets/%s' % ticket['id'] + '?access_key=' + goodKey, json=data, headers=headers)
assert r.status_code == 200, "Error assigning: expected 200, got: %d." % r.status_code

#
#
# Add tag to a ticket
show_progress()
data = {'tag_label': 'Test'}
r = requests.post(apiUrl + 'tickets/%s' % ticket['id'] + '/add_tag?access_key=' + goodKey, json=data, headers=headers)
assert r.status_code == 200, "Error adding tag: expected 200, got: %d." % r.status_code
new_tag_list = r.json()
assert len(ticket['tags']) + 1 == len(new_tag_list), 'List of tags should be increased by 1'

#
#
# Get list of events for a ticket
show_progress()
r = requests.get(apiUrl + 'tickets/%s' % ticket['id'] + '/events?access_key=' + goodKey, headers=headers)
assert r.status_code == 200, "Error getting list of events: expected 200, got: %d." % r.status_code
events = r.json()
assert len(events) > 0, 'List of events should not be empty'

#
#
# Remove tag from a ticket
show_progress()
data = {'tag_label': 'Test'}
r = requests.post(apiUrl + 'tickets/%s' % ticket['id'] + '/remove_tag?access_key=' + goodKey, json=data,
                  headers=headers)
assert r.status_code == 200, "Error removing tag: expected 200, got: %d." % r.status_code
new_tag_list = r.json()
assert len(ticket['tags']) == len(new_tag_list), 'List of tags should be decreased by 1'

# 
# 
# delete newly created ticket
show_progress()
url = apiUrl + 'tickets/%s' % ticket['id'] + '?access_key=' + goodKey
r = requests.delete(url, headers=headers)
assert r.status_code == 200, "Error deleting: expected 200, got: %d." % r.status_code

#
#
# search for recently closed tickets 
show_progress()
url = apiUrl + 'tickets/search?access_key=' + goodKey + '&query=status.id:60&sf=closed_on&r=1'
r = requests.get(url, headers=headers)
tickets = r.json()
assert r.status_code == 200, "Error getting recently closed tickets: expected 200, got: %d." % r.status_code
assert tickets[0]['status_id'] == 60, "Ticket status should be 60, but got %d" % tickets[0]['status_id']

#
#
# search for tickets rated with 3 stars (rating 60)
show_progress()
url = apiUrl + 'tickets/search?access_key=' + goodKey + '&query=rating:60&sf=closed_on&r=1'
r = requests.get(url, headers=headers)
assert r.status_code == 200, "Error getting recently closed tickets: expected 200, got: %d." % r.status_code
tickets = r.json()
assert tickets[0]['rating'] == 60, "Ticket rating should be 60, but got %d" % tickets[0]['rating']

#
# 
# get asset list
show_progress()
r = requests.get(apiUrl + 'assets?access_key=' + goodKey, headers=headers)
assert r.status_code == 200, "Error getting asset list. Expected 200, got: %d" % r.status_code
assets = r.json()

#
# 
# get asset status list
show_progress()
r = requests.get(apiUrl + 'asset_statuses?access_key=' + goodKey, headers=headers)
assert r.status_code == 200, "Error getting asset status list. Expected 200, got: %d" % r.status_code
asset_statuses = r.json()

#
# 
# get asset type list
show_progress()
r = requests.get(apiUrl + 'asset_types?access_key=' + goodKey, headers=headers)
assert r.status_code == 200, "Error getting asset type list. Expected 200, got: %d" % r.status_code
asset_types = r.json()

#
# 
# get department list
show_progress()
r = requests.get(apiUrl + 'departments?access_key=' + goodKey, headers=headers)
assert r.status_code == 200, "Error getting department list. Expected 200, got: %d" % r.status_code
departments = r.json()

#
# 
# get location list
show_progress()
r = requests.get(apiUrl + 'locations?access_key=' + goodKey, headers=headers)
assert r.status_code == 200, "Error getting location list. Expected 200, got: %d" % r.status_code
locations = r.json()

print("\n==================")
print("==== TESTS OK ====")
print("==================\n")
