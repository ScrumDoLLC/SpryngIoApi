import slumber
from colorama import init, Fore
from time import sleep

import local_settings as settings
# We're using slumber (http://slumber.in/), a python library that makes RESTfull calls amazingly easy to access the API


def main():
	init()
	base_url = "%s/openapi/" % settings.host
	api = slumber.API(base_url, auth=(settings.username, settings.password))
	read_collections(api)


def read_collections(api):
	# Get all of our collections
	try:
		collections_list = api.organizations(settings.organization_slug).initiatives(settings.initiative_slug).collections().get()
	except Exception as e:
		print(e)
		return

	api_count = check_throttle(1)

	for collection in collections_list:
		# Print out the name & slug of each collection (Fore.GREEN colors it...)
		print(Fore.GREEN + "%s\t%s" % (collection["name"], collection["slug"]))


# Since we're iterating over your entire account in this example, there could be a lot of API calls.
# This function is a dumb way to make sure we don't go over the throttle limit.
def check_throttle(requests):
	requests += 1
	if requests >= 149:
		sleep(5) # Add in a delay when we get close the our max # of requests per 5 seconds.
		return 0
	return requests

if __name__ == "__main__":
    main()
