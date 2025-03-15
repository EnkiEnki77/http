# http/1 came out in 1996. It's built on top of the TCP protocol. When a client wants to make an HTTP
# request a TCP connection must be made with the server through a 3-way handshake, where the client sends
# a sync request, the server sends back acknowledgement and its own sync request, and the client sends
# back an acknowledgement of the servers sync request.

# As soon as the client acknowledges the servers sync request it can instantly send an HTTP request.
# As soon as the server sends a response the TCP connection is broken, and the client must initiate a new
# TCP connection to make another request.

# http is stateless, meaning requests are independent from each other.



# http/1.1 was released in 1997 and introduced keep alive mechanism that allowed the same TCP connection
# to be reused for multiple http requests.

# It also introduced pipelining which allows the client to send multiple requests before waiting for the
# servers response. The responses must be received in the same order requests were sent. Many proxies did
# not implement this properly and so the feature was not supported for many browsers

# Another issue you run into with pipelining is head of line blocking where when you have a queue of request
# waiting to be sent off, if one of them is abnormally large and takes up a lot of time to process this
# blocks all other message data from being processed, even if it could be processed rather quickly. This
# can in turn cause requests to time out, and other issues.

# To keep loading performance at an acceptable level browsers generally keep multiple TCP connections open
# to the same server at any given time, and send requests to it in parallel



# http/2 came out in 2015, and introduced http streams where multiple streams of requests could be sent
# to the server on a single tcp connection. Unlike pipelining, each stream is independent of each other,
# and so they dont need to be sent or received in order. This solves the head of line blocking issue
# at the application layer, because streams dont have to wait for each other to be resolved to start
# be being processed themselves. As soon as theyre ready to be processed, they are, regardless of whether
# the previous stream is taking awhile or not. But the issue still exists at the transport layer with TCP.

# it also introduced a push capability where servers can send updates to clients whenever new data is available.
# without requiring a client to pull.



# HTTP/3 was published in 2022. Instead of operating on TCP, Google has implemented a new protocol called
# QUIC that operates off of UDP. It introduces streams as the first class citizen at the transport layer.
# QUIC streams share the same quick connection, so no additional handshake is required. Streams are delivered
# independently, so packet loss effecting one stream doesnt effect others. This allows QUIC to eliminate
# HOL blocking at the transport layer.

# QUIC is designed for mobile heavy internet usage. People on their smart phones are constantly switching
# from one network to another. Using TCP, these connection handoffs are sluggish.

# QUIC implements connection ID, which allows the same connection across different networks.