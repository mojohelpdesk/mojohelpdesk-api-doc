#!/usr/bin/env python

###
#
# This Python script showcases and tests Mojo Helpdesk (https://mojohelpdesk.com) REST API.
#
# Usage - see help: ./mojo-helpdesk-api-tests.py
#
# Public domain.    
#
##
import requests # pip install requests
import sys

dn = 'https://app.mojohelpdesk.com'

#
#
# Print a "." w/o a carriage return
def showProgress():
    sys.stdout.write(".") # write w/o \n
    sys.stdout.flush()

if len(sys.argv) < 2: 
    sys.exit("Usage: %s <access-key> [server domain name (e.g.: http://localhost:3000), default: https://app.mojohelpdesk.com]" % sys.argv[0])

goodKey = sys.argv[1] # get access key
badKey = "bad"

if len(sys.argv) >= 3: 
    dn = sys.argv[2] # get hostname

print("Using DN: %s" % dn)


#
# Ticket list endpoint / URL
# 
apiUrl = dn + '/api/v2/'

headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}


#
# 
# get ticket list w/ good key
showProgress()
r = requests.get(apiUrl + 'tickets?access_key=' + goodKey, headers=headers)
assert r.status_code == 200, "Error getting ticket list. Expected 200, got: %d" % r.status_code

#
# 
# get w/ bad key => error 401
showProgress()
r = requests.get(apiUrl + 'tickets?access_key=' + badKey, headers=headers)
assert r.status_code == 401, "Should get 'not authorized' error, got: %d" % r.status_code

#
# 
# get ticket queue list
showProgress()
r = requests.get(apiUrl + 'ticket_queues?access_key=' + goodKey, headers=headers)
assert r.status_code == 200, "Error getting ticket queue list. Expected 200, got: %d" % r.status_code
ticket_queues = r.json()

#
# 
# get ticket form list
showProgress()
r = requests.get(apiUrl + 'ticket_forms?access_key=' + goodKey, headers=headers)
assert r.status_code == 200, "Error getting ticket form list. Expected 200, got: %d" % r.status_code
ticket_forms = r.json()

#
# 
# create ticket OK
showProgress()
data = {'title':'Test ticket','description':'Testing API for ticket creation','priority_id':30,'ticket_queue_id':ticket_queues[0]['id']}
r = requests.post(apiUrl + 'tickets?access_key=' + goodKey, json=data, headers=headers)
assert r.status_code == 201, "Error creating: expected 201, got: %d." % r.status_code
ticket = r.json()

#
#
# create ticket without email notification OK
showProgress()
data = {'suppress_user_notification': 'true', 'title':'Test ticket','description':'Testing API for ticket creation','priority_id':30,'ticket_queue_id':ticket_queues[0]['id']}
r = requests.post(apiUrl + 'tickets?access_key=' + goodKey, json=data, headers=headers)
assert r.status_code == 201, "Error creating: expected 201, got: %d." % r.status_code
ticket = r.json()

#
#
# create ticket with attachments
showProgress()
data = {
  'title':'Test ticket',
  'description':'Testing API for ticket creation',
  'priority_id':30,
  'ticket_queue_id':ticket_queues[0]['id']
}
files = {
  'attachment[0][content]': open('test.txt', 'rb'),
  'attachment[1][content]': open('test.pdf', 'rb')
}
r = requests.post(apiUrl + 'tickets?access_key=' + goodKey, files=files, data=data)
assert r.status_code == 201, "Error creating: expected 201, got: %d." % r.status_code
ticket = r.json()

#
# 
# show ticket OK
showProgress()
r = requests.get(apiUrl + 'tickets/%s' % ticket['id'] + '?access_key=' + goodKey, headers=headers)
assert r.status_code == 200, "Error showing: expected 200, got: %d." % r.status_code
ticket = r.json()

#
# 
# update ticket OK
showProgress()
data = {'title':'Test ticket API'}
r = requests.put(apiUrl + 'tickets/%s' % ticket['id'] + '?access_key=' + goodKey, json=data, headers=headers)
assert r.status_code == 200, "Error updating: expected 200, got: %d." % r.status_code

#
# 
# get agents details OK
showProgress()
r = requests.get(apiUrl + 'users/techs?access_key=' + goodKey, headers=headers)
assert r.status_code == 200, "Error getting list of agents: expected 200, got: %d." % r.status_code
agents = r.json()

#
# 
# get access rights for restricted agents
showProgress()
r = requests.get(apiUrl + 'access_rights/restricted_agents?access_key=' + goodKey, headers=headers)
assert r.status_code == 200, "Error getting access rights for restricted agents. Expected 200, got: %d" % r.status_code
restricted_agents = r.json()

#
# 
# get access rights for groups
showProgress()
r = requests.get(apiUrl + 'access_rights/groups?access_key=' + goodKey, headers=headers)
assert r.status_code == 200, "Error getting access rights for restricted agents. Expected 200, got: %d" % r.status_code
groups = r.json()

#
# 
# assign ticket OK
showProgress()
data = {'assignee_id':agents[0]['id']}
r = requests.put(apiUrl + 'tickets/%s' % ticket['id'] + '?access_key=' + goodKey, json=data, headers=headers)
assert r.status_code == 200, "Error assigning: expected 200, got: %d." % r.status_code

#
#
# Add tag to a ticket
showProgress()
data = {'tag_label':'Test'}
r = requests.post(apiUrl + 'tickets/%s' % ticket['id'] + '/add_tag?access_key=' + goodKey, json=data, headers=headers)
assert r.status_code == 200, "Error adding tag: expected 200, got: %d." % r.status_code
new_tag_list = r.json()
assert len(ticket['tags']) + 1 == len(new_tag_list), 'List of tags should be increased by 1'

#
#
# Get list of events for a ticket
showProgress()
r = requests.get(apiUrl + 'tickets/%s' % ticket['id'] + '/events?access_key=' + goodKey, headers=headers)
assert r.status_code == 200, "Error getting list of events: expected 200, got: %d." % r.status_code
events = r.json()
assert len(events) > 0, 'List of events should not be empty'
assert events[0]['action_name'] == 'update', 'Latest event should be an update'

#
#
# Remove tag from a ticket
showProgress()
data = {'tag_label':'Test'}
r = requests.post(apiUrl + 'tickets/%s' % ticket['id'] + '/remove_tag?access_key=' + goodKey, json=data, headers=headers)
assert r.status_code == 200, "Error removing tag: expected 200, got: %d." % r.status_code
new_tag_list = r.json()
assert len(ticket['tags']) == len(new_tag_list), 'List of tags should be decreased by 1'

# 
# 
# delete newly created ticket
showProgress()
url = apiUrl + 'tickets/%s' % ticket['id'] + '?access_key=' + goodKey
r = requests.delete(url, headers=headers)
assert r.status_code == 200, "Error deleting: expected 200, got: %d." % r.status_code

#
#
# search for recently closed tickets 
showProgress()
url = apiUrl + 'tickets/search?access_key=' + goodKey + '&query=status.id:60&sf=closed_on&r=1'
r = requests.get(url, headers=headers)
tickets = r.json()
assert r.status_code == 200, "Error getting recently closed tickets: expected 200, got: %d." % r.status_code
assert tickets[0]['status_id'] == 60, "Ticket status should be 60, but got %d" % tickets[0]['status_id']

#
#
# search for tickets rated with 3 stars (rating 60)
showProgress()
url = apiUrl + 'tickets/search?access_key=' + goodKey + '&query=rating:60&sf=closed_on&r=1'
r = requests.get(url, headers=headers)
assert r.status_code == 200, "Error getting recently closed tickets: expected 200, got: %d." % r.status_code
tickets = r.json()
assert tickets[0]['rating'] == 60, "Ticket rating should be 60, but got %d" % tickets[0]['rating']


print("\n==================")
print("==== TESTS OK ====")
print("==================\n")
