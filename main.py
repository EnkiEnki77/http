# HTTP stands for Hypertext Transfer Protocol
# It is the foundation of the web, and is used to load webpages through hypertext links.

# HTTP is an application layer protocol designed to transfer data between devices across a network.
# It runs on top of other layers of the network protocol stack.

# A typical flow over HTTP involves a client device making a request for data to a server
# and the server sending back a response.

# An HTTP request is the way internet communication platforms such as browsers request the data they
# need to load a website.


# An HTTP request carries encoded data across a network, this will be of 5 different types.
# 1. The http version being utilized
# 2. A URL
# 3. An HTTP method
# 4. HTTP request headers
# 5. An optional body carrying data meant for the server.



# HTTP method indicates the action the request expects from the queried server. The main methods are:
# GET: requests a representation of a specific resource from the server, such as the html document of a
#      a website. It shouldnt have a request body
# HEAD: asks for a response similarly to GET, but without a response body.
# POST: submits data of some sort to the server, often changing the state and/or causing side effects
#       on the server.
# PUT: replaces a specified resource on the server with the request body.
# DELETE: deletes the specified resource.
# CONNECT: establishes a tunnel to the server, identified by the target resource.
# OPTIONS: describes the communication options for the resource.
# TRACE: performs a message loop-back test along the path to the target resource
# PATCH: updates a specified resource on the server with the request body.



# Request headers contain meta data about the request and are sent as key:value pairs
# They convey core information such as what browser is being used, and what data is being
# requested.


# The request body contains any info submitted in a form that should be sent to the server.



# HTTP response is what the server sends back in response to the request from the client
# it contains:
# Status code, response headers, and a response body.

# Status codes are 3 digit codes that give information about the status of the request. There are 5 blocks
# 100 status codes are informational
# 200 denote a successful request
# 300 denote redirection is necessary
# 400 are an error on the client side
# 500 an error on the server side.


