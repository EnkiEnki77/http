# Our computer is connected to the internet, a network of millions of other computers also connected to the
# internet.
# When we want to communicate with one of the other computers over the network we specify the computer through
# its IP address aka web address.
# Each computer has it's own unique IP address, that allows other computers to directly communicate with it.

# The anatomy of an IP address is four numbers between 0 and 255, separated by dots. For example 17.244.27.199.
# This format of IP is called IPv4

# There's also IPv6 which has 8 numbers separated by colons :. There are way more possible IPv6 addresses.

# TO communicate any other computer across the internet you need their IP address, itd be very difficult and inconvenient
# to have to remember and type in the IP address for every site you  may want to visit.

# This is where DNS comes into play, it's main role is to map human readable names (domain names) to an IP address, so
# that these sites are more easily accessible.

# DNS (domain name system) is responsible for looking up the IP address associated with any domain name you type into
# your browser, and giving it back so the proper http request can be made.


# There are two steps when a client wants to send an http request to a server based on a given domain name
# 1. resolve the domain name to an IP address through DNS
# 2. use the IP address to make the http request.

