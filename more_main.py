# http is an application layer protocol that is sent over a TCP connection, or in the
# case of HTTPS a TLS encrypted TCP connection.
# It enables a client and server to exchange data over a network through http requests and responses.

# requests are made by a client user-agent, such as a web browser (Or a proxy on behalf of it).

# between the client and server there are numerous entities, collectively referred to as proxies which act
# as gateways or caches and perform various different operations.


# The client or user-agent is generally the web browser, but can be any other tool that acts on behalf of
# the user to make requests to a server across the network.


# To display a web page the browser makes an initial request for the HTML document of the page, it then parses
# it and makes additional requests for any executable scripts, CSS files, images, or videos indicated within
# the HTML.


# The web server appears as one server virtually, but may actually be multiple sharing the load. Load balancing


# Between the client and server, numerous other computers and machines relay the http messages. Most reside
# on the transport, network, or physical layer. Some reside at the application layer, these are known as
# proxies. These can be transparent, forwarding on the message without altering it. Or non-transparent,
# in which case they alter the message in some way before forwarding it.


# Proxies can perform functions such as:
# caching, which can be public or private
# filtering, like an antivirus scan or parental controls.
# load balancing, to allow multiple servers to serve different requests.
# logging, to allow the storage of historical info.
# or authentication


