import requests
from time import sleep
from colorama import init, Fore
import local_settings as settings


def main():
    init()
    base_url = "%s/openapi/" % settings.host
    read_collections(base_url)


def read_collections(base_url):
	# Get all of our collections
    collections_api = f'{base_url}organizations/{settings.organization_slug}/initiatives/{settings.initiative_slug}/collections'
    api_request = requests.get(collections_api, headers={'Authorization': f'Key {settings.access_token}'})
    api_count = check_throttle(1)

    if api_request.status_code != 200:
        # sonething wrong??
        print(api_request.json())
        return

    for collection in api_request.json():
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
