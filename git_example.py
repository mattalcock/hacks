#!/usr/bin/env python

from github2.client import Github

api_token = 'mattalcock'
api_user = '43de91f8870bf58cda7945304baf4faa'

#Currently 2,259,699 repos. I think we can pre populate for top 100 repos (500)
#Refresh the cache that sorts them periodically.

big_projects = ['bootstrap']

#Build a class object of the repo and cache that.

github = Github()

query_string = "bootstrap"
limit = 10

results = github.repos.search(query_string)
matches = [ (r.name, r.owner) for r in results[:limit]]

for name, owner in matches:
	combo_name = "%s/%s" % (owner, name)
	print combo_name
	watchers =  len(github.repos.watchers(combo_name))
	open_issues = github.issues.list(combo_name, state="open")
	closed_issues = github.issues.list(combo_name, state="closed")
	print "%s has %s watchers." % (combo_name, watchers)
	print "%s has %s open issues." % (combo_name, len(open_issues))
	print "%s has %s closed issues." % (combo_name, len(closed_issues))
