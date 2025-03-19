// URI (Uniform Resource Identifier) is a unique character sequence that identifies a resource that is
// accessed via the internet.

// URI's have syntax rules, to ensure uniformity. Allowing websites to interpret them in the same way.

// URI's come in two types: URL's (uniform resource locator), and URN's (uniform resource name)


// There are 8 pieces to a URL, some are required, some not.

// 1. The protocol aka. the scheme, such as http://, required
// Defines the rules behind how the data communicated is displayed, encoded or formatted.
// examples are: http, https, ftp, mailto, etc.
// All schemes require :, but only schemes with an authority component such as http require the //

// 2. Username, not required
// 3. Password, not required
// 4. Domain, required. May include a sub domain and top level domain.
// 5. Port, not required. Defaults to 80 or 443 depending on protocol
// The port is a virtual point where network connections are made. They are handled by the operating system
// and are numbered from 0 to 65,535, though some ports are reserved, such as 0 for the OS API.
// Whenever you connect to another computer over a network you are connecting to a specific port on that computer
// Which is listened to by a specific program on that computer.
// A port can only be used by one program at a time.
// The port component of a URL is often not visible when browsing normal sites on the internet, because the default
// http or https port is being used. 80 or 443 respectively. Whenever the port used is not default it must be specified
// in the URL.

// 6. Path, /board for example, not required. Defaults to /
// 7. Query, ?sort=createdAt for example, not required.
// 8. Fragment, #id for example, not required.

// Only the protocol and domain are required for a valid URL.
