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

