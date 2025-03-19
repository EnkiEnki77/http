// # web clients find other computers over the internet using Internet Protocol (IP) addresses.
//
// # each device connected to the internet has a unique IP address.
//
// # when we browse the internet through a web browser such as google we type a domain name into the search bar, which
// # is then converted into an IP address by the DNS. We then can take this IP address and know what server to make
// # an http request to over the internet in order to request the data for a given webpage.

async function fetchIPAddress(domain){
    const response = await fetch(
        `https://1.1.1.1/dns-query?name=${domain}&type=A`,
        {
            headers:{
                accept: "application/dns-json"
            }
        }
    )
    const responseObj = await response.json()

    // console.log(`IP address: ${responseObj.Answer[0].data}`)

    return responseObj.Answer[0].data
}

fetchIPAddress("example.com")



// The domain name/host name is only a part of the URL. It is the part of the URL that allows us to derive the IP
// of the server we want to communicate with.

function getDomainNameFromURL(url){
    const urlObj = new URL(url).hostname
    return urlObj
}

// The URL api is an api built into js that allows us to turn URL's into an object, with each of it's pieces being
// a property. To access the domain you would use the hostname property.

// Its a class so it has to be instantiated with the new keyword.

console.log(getDomainNameFromURL('https://homestarrunner.com/toons'))




// DNS (domain name system) is the phone book of the internet. Humans type easy to read domain names into their web
// web browser. DNS resolves these domains into an IP address the client can use to locate and make an http request
// to a server.

// DNS is managed by a non-profit company called ICANN. Whenever your computer attempts to resolve a domain name it
// contacts one of ICANN's root nameservers whose address is included in your computers networking config.

// If DNS is a phone book ICANN is the company that keeps it up to date and available.



// Sub domains prefix a domain and allow a domain to network traffic to multiple different servers and resources.

// Say we have the domain boot.dev. A sub domain would be blog.boot.dev, and it may exist at a different IP.

// So we can break up our site/resources onto multiple IP addresses without having to buy additional domains.
// You own all sub domains of a given domain.


// The part of the domain such as .dev, .com, .org, etc. Is called the top level domain