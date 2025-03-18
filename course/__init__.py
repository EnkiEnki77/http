# http is the most popular protocol for exchanging data across the internet.

# A protocol is a set of rules agreed upon between computers across the world that then allow computers to
# communicate across the internet.

# A URL (uniform resource locator) is the address of another computer or resource on the internet. Part of the URL
# specifies how to reach the server, and part of it tells the server what resource we want.

# In order to utilize http to request data from a server we need to supply a URL that specifies the server, and
# what data we're wanting.


# The http:// is the scheme of the URL and specifies which communication protocol is utilized for the url.

# We need to specify the scheme, because http is not the only communication protocol that utilizes URL's


# A computer can act as both a server and a client, depending on whether its making a request or serving a
# response.
# Say we load up a youtube video on our phone. Our phone will act as a client and ask for the video plus its
# comments.
# On youtubes backend the request is received by the computer that stores youtubes videos, but say they store
# comments on a different computer, before the video computer serves the response back to our phone it will
# act as a client requesting comments from the comment computer. Then send the video and comments back to our
# phone



# Having to write the extensive logic for making an HTTP request from scratch every time would be a lot, so the
# browser provides an API to us through JS that abstracts away a lot of that logic, making things a lot more
# simple. It's called the fetch API

# Fetch takes the url youd like to make a request with and a settings object that defines the settings of the
# http request as inputs.

# in the settings object you can set things such as the http method, the mode, and the headers.

