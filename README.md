
Spryng.io API
=====================

This document describes the API for Spryng.io that can be accessed from https://app.spryng.io.

Authentication
--------------

### In Browser

For debugging purposes, if you make requests from your browser and are logged in,
your session info will be carried over.  Example:
https://app.spryng.io/openapi/v1/organizations/

We do not respond with CORS headers, and we do expect a CSRF token on PUT, POST or DELETE
so this is not a good way to authenticate for any real use.

### OAuth 1.0
In order for the client to access resources, it first has to obtain
permission.  This permission is expressed in
the form of a token and matching shared-secret. Unlike the resource owner credentials,
tokens can be issued with a limited lifetime and revoked independently.

You can get an API token from your account settings.

REST
----

Our calls generally follow RESTfull principles.

POST - Creates new items
PUT - Updates existing items
GET - Retrieves data
DELETE - Removes an item

JSON
----

All of our calls return results in JSON by default.  When expecting data
(POST or PUT), you should JSON encode your data in the body of the request.

What's a SLUG?
--------------

Initiatives and organizations are identified by a slug, a short string consisting of
alpha-numeric characters or dashes.  Most other objects are identified by a numeric id.
You can find out the slug of an organization by calling the getOrganizations call:
https://app.spryng.io/openapi/docs#!/organizations


API Browser
-----------

You can browse all the available API calls in our interactive API Browser:
https://app.spryng.io/openapi/docs

If you are logged into Spryng.io, you will be able to actually execute API calls
against your account via that page (ie. It's for real, be careful.) to see the inputs,
URL's and outputs of each command.  Click the "Try it out" button under each call.

Some properties are read-only via the API.  When posting or putting data, please
consult the body parameter of the API browser.  It lists all valid fields and gives
examples for the format of the data expected.

![API Browser](https://raw.github.com/ScrumDoLLC/SpryngIoApi/main/images/browser.png "API Browser")


Rate Throttling
---------------

GET requests - We allow up to 50 requests per 5 seconds.

POST or PUT requests - We allow up to 10 requests per 5 seconds.


Paged Results
-------------

In general, in order to make working with our API as easy as possible, we try to return
all relevant data in a single call.  However, there are a few calls that may generate way
too much information.  Those results will be paged.  The API Browser lists which calls will
be paged in this way.


Subscription
------------

API access requires a premium level subscription.


Support
-------

All calls have at least a minimal amount of documentation in the API browser.  If anything is
unclear, please send a message in our support email.  support@spryng.io


Contributions
-------------

Have an example in another language, find an error in this documentation?  We'd
love to include it, feel free to send a pull request via GitHub our way.
