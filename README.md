# IP2Location.io Maltego Transforms

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Enrich IP address entities in **Maltego** with IP geolocation, network information, and hosted-domain results using the [IP2Location.io API](https://www.ip2location.io/). This project provides **local Python transforms** for IPv4 and IPv6 investigations.

## Features

- **IP geolocation:** Look up country, region, city, coordinates, ZIP code, time zone, and ASN information where available.
- **Hosted domains:** Find domains associated with an IP address and display a result count and up to five domains in the graph.
- **Graph-based investigation:** Run lookups from IP address entities without leaving Maltego.
- **IPv4 and IPv6:** Configure separate local transforms for each entity type.

Results depend on the API response and your subscription plan.

## Available Transforms

| Transform | Maltego input | Graph output | Command parameters |
|---|---|---|---|
| IP2Location Geolocation | IPv4 Address or IPv6 Address | Location entity with details in the Property View | `project.py local ip2locationgeolocation` |
| IP2WHOIS Hosted Domain | IPv4 Address or IPv6 Address | Phrase entity with a domain count and up to five hosted domains | `project.py local ip2locationhosteddomain` |

> Maltego requires an input entity type when creating a local transform. Register a transform separately for IPv4 and IPv6 if you need both.

## Requirements

- Maltego desktop client with support for local transforms.
- Python and `pip` installed on your computer.
- An [IP2Location.io API key](https://www.ip2location.io/pricing).
- Internet access for API requests.

## Installation and Setup

### 1. Download and install dependencies

Clone the repository (or download and extract it from GitHub):

```bash
git clone https://github.com/ip2location/ip2location-io-maltego.git
cd ip2location-io-maltego
python -m pip install -r requirements.txt
```

The project uses the `maltego-trx` Python package. If `python` is not recognized on your system, use your installed Python executable (for example, `py` on Windows or `python3` on some systems).

### 2. Configure your API key

Open `transforms/credentials.py` and set your key:

```python
API_KEY = 'YOUR_IP2LOCATION_IO_API_KEY'
FORMAT = 'json'
```

**Security:** Do not commit your configured API key to a public repository or share the modified credentials file. The current project reads the key from this Python file.

### 3. Register a local transform in Maltego

In Maltego, open **Transforms → New Local Transform** and complete the wizard. Use the following values:

| Setting | Value |
|---|---|
| Display Name | `IP2Location Geolocation` or `IP2WHOIS Hosted Domain` |
| Input Entity Type | IPv4 Address **or** IPv6 Address |
| Command | Absolute path to your Python interpreter |
| Parameters | `project.py local ip2locationgeolocation` **or** `project.py local ip2locationhosteddomain` |
| Working Directory | Absolute path to the repository's root directory (containing `project.py`) |

Choose the **Parameters** value that matches the transform you are registering, then click **Finish**. Repeat the registration for other transform and IP address types as needed.

> **Example Windows command:** `C:\\Python313\\python.exe` (replace with the actual path on your machine). The working directory should be a folder path, not a file path.

## Using the Transforms

### IP Geolocation Lookup

1. Create or open a Maltego graph.
2. Drag an **IPv4 Address** or **IPv6 Address** entity from the Entity Palette onto the graph.
3. Enter the IP address you want to investigate.
4. Right-click the entity and select **Local Transforms → IP2Location Geolocation**.
5. Review the resulting **Location** entity and its details in the **Property View**.

![IP2Location.io geolocation transform output in Maltego](https://cdn.ip2location.io/assets/img/integrations/maltego-output.png)

### Hosted Domain Lookup

1. Add an IPv4 or IPv6 entity to your graph.
2. Right-click the entity and select **Local Transforms → IP2WHOIS Hosted Domain**.
3. Review the **Phrase** entity showing the number of domains found, along with the first five domain results.

![Hosted domain transform output in Maltego](https://cdn.ip2whois.com/assets/img/maltego-output-hosteddomain.png)

> Hosted-domain results identify associations returned by the API; shared hosting and infrastructure changes mean these associations should not be treated as proof of common ownership.

## Understanding ASN Lookup

An **Autonomous System Number (ASN)** identifies an autonomous system involved in Internet routing. ASN information can help investigators understand which network operator is associated with an IP address and support traffic attribution, infrastructure research, and incident triage.

The geolocation transform can return ASN information when provided by the API. To review it, run the geolocation transform and inspect the output entity's properties. **ASN data does not, by itself, identify an individual user or device.**

For offline ASN research, see [IP2Location ASN LITE](https://www.ip2location.com/database/lite).

## Troubleshooting

| Problem | What to check |
|---|---|
| Transform is not visible | Confirm that you registered the correct IPv4 or IPv6 input entity and selected the local transform. |
| Python does not start | Use the absolute Python executable path and verify the working directory contains `project.py`. |
| `ModuleNotFoundError: maltego_trx` | Run `python -m pip install -r requirements.txt` with the same Python interpreter configured in Maltego. |
| Lookup returns no useful result | Check the API key, network connectivity, input IP address, and subscription entitlements. |
| Geolocation fields are missing | Available fields vary by API plan and IP address. |
| Hosted domains are not shown | Check API access and whether the queried IP has results; the transform displays only the first five domains. |

For additional help, [open a GitHub issue](https://github.com/ip2location/ip2location-io-maltego/issues).

## Accuracy and Responsible Use

IP geolocation is **not GPS**. Locations are approximate and may represent a network, service provider, or connection point rather than a device's physical position. VPNs, proxies, mobile networks, and shared hosting can affect interpretation. Combine IP intelligence with other evidence when conducting investigations.

## Related IP2Location Products

| Product | Purpose |
|---|---|
| [IP2Location.io](https://www.ip2location.io/) | Hosted IP geolocation, ASN, and network intelligence APIs. |
| [IP2Location LITE](https://www.ip2location.com/database/lite) | Free downloadable IP geolocation and ASN databases for offline use. |
| [IP2Location Database](https://www.ip2location.com/database/ip2location) | Commercial offline IP geolocation databases. |
| [IP2Proxy](https://www.ip2location.com/database/proxy) | IP proxy, VPN, TOR and anonymizer intelligence. |
| [IP2WHOIS](https://www.ip2whois.com/) | Domain WHOIS lookup services. |

> These database products are separate from the Maltego integration. The transforms use online API lookups rather than local database files.

## Support

- **API access and plans:** [IP2Location.io Pricing](https://www.ip2location.io/pricing)
- **Bugs and feature requests:** [GitHub Issues](https://github.com/ip2location/ip2location-io-maltego/issues)

## License

Licensed under the **MIT License**. See [LICENSE](https://github.com/ip2location/ip2location-io-maltego/blob/main/LICENSE).
