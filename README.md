# CheckDomainScope
Takes a list of domains and checks if they are within a provided list of in-scope IP addresses + CIDR ranges

positional arguments:
  scopefile       File containing all CIDR ranges in-scope

optional arguments:
  -h, --help      show this help message and exit
  -dL DOMAINLIST  A list of domains to resolve and check if they are in-scope
  -iL IPLIST      A list of IP addresses to check against the in-scope list

Example: 
`./CheckDomainScope scope.txt -dL domains.txt`

Where domains.txt:
```Example1.com
example2.com
example3.com
```

Where scope.txt:
```1.1.1.1/30
192.10.8.5/24
2.2.2.2
100.50.41.31/32
```

Outputs for each domain check in "domains.txt": 
`Hostname <hostname>, IP Address <resolved IP>, in scope: <True/False>`
