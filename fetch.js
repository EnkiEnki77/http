const url = getURL()
const settings = getSettings()

// because we're requesting data over the internet, which may take time we need to tell the program to pause
// and await the response.
const response = await fetch(url, settings)
// We also want to await the pending promise to be resolved, because we want to convert the response data to
// json, not the pending promise.
// The response our request gives back is in plain json text, json() converts it to an actual object we can work
// with.
const responseData = await response.json()

logIssues(responseData)

function getSettings(){
    const apiKey = generateKey()
    return {
        method: "GET",
        mode: "cors",
        headers: {
            "X-API-Key": apiKey,
            "Content-Type": "application/json"
        }
    }
}


function getURL(){
    return "https://api.boot.dev/v1/courses_rest_api/learn-http/issues"
}


function  generateKey() {
    const characters = "ABCDEF0123456789"
    let result = ''
    for(let i = 0; i < characters.length; i++){
        result += characters.charAt(Math.floor(Math.random() * characters.length))
    }
    return result
}


function logIssues(issues){
    for(const issue of issues){
        console.log(issue.title)
    }
}


// The frontend of a website or web app is the device the user interacts with the backend is simply a server
// that houses the data of the application in a centralized location

// A server is the name of a computer that takes on the role of serving data across a network connection. Any
// computer could be used as a server, even a smartphone. However, a good server should be running and listening
// for requests 24/7, so its best to use a computer specifically designed to be a server.



