# IP2Location.io Maltego local transform


This is a Maltego local transform that used IP2Location.io API to query and return the geolocation data for an IP address, such as country, region, city, latitude & longitude, ZIP code, time zone and ASN.

This module requires API key to function. You may sign up for a free API key at [https://www.ip2location.io/pricing](https://www.ip2location.io/pricing).  

## Installation

 1. Download and extract the release from [https://github.com/ip2location/ip2location-io-maltego/releases](https://github.com/ip2location/ip2location-io-maltego/releases).
 2. Navigate to the extracted folder, and open *transforms/credentials.py*. Add your IP2Location.io API Key into this variable: `API_KEY=''`.
 3. Open your Maltego client, click on the "Transforms" tab in the ribbon bar and clicking "New Local Transform".
 4. A new wizard will be open to guide you through the process of adding a new local Transform. On the first page, you will required to fill in the "Display Name" and "Input Entity Type". For the "Display Name" field, fill in "IP2Location Geolocation" if you want to lookup geolocation information or "IP2WHOIS Hosted Domain" if you want to lookup for hosted domain infomation, and choose IPv4 address or IPv6 address according to your use case. Click *Next >* button when done.
 
> Only one type of IP address can be chosen at the same time. To use this local transform for both types, you may need to perform multiple imports for this local transform.

 5. In the next page, you will be required to fill in "Command", "Parameters" and "Working Directory". For the "Command", fill in the absolute path of the Python interpreter in your machine. For "Parameters", fill in the following value according to the "Display Name" field in previous step: `project.py local ip2locationgeolocation` or `project.py local ip2locationhosteddomain`. For "Working Directory", set the value to the absolute path of the extracted folder in step 2. Click "Finish" to save the settings.


## Usage

 1. Create a new graph, and search for IPv4 address or IPv6 address in the Entity Palette depends on what you choose in step4 in the installation section. Drag the entity into the graph.
 2. By default the entity will contains an IP address. You can continue using it or change the value depends on your use case.
 3. Right click on the IP address entity on the graph, click Local Transform, and click on the transform that we just imported. The transform will query the API to get the geolocation result.
 4. For IP geolocation, you shall see a Location entity is created at below of the IP address entity with the API result in Property View.

![Output of using IP2Location.io local transform for IP Geolocation](https://cdn.ip2location.io/assets/img/integrations/maltego-output.png)
5. For hosted domain, you shall see a Phrase entity that indicates the total number of hosted domain found is created at below of the IP address entity, along with the first 5 domains.

![Output of using IP2Location.io local transform for Hosted Domain](https://cdn.ip2whois.com/assets/img/maltego-output-hosteddomain.png)

## License

See the LICENSE file.