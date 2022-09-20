from urllib.request import ssl, socket
hostname = 'etsy.com'
port = '443'

context = ssl.create_default_context()

with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        certificate = ssock.getpeercert()
        print(certificate['notAfter'])
        print(certificate)
        
### Output
#Oct  1 17:09:27 2022 GMT
#{'subject': ((('commonName', '*.etsystatic.com'),),), 'issuer': ((('countryName', 'US'),), (('stateOrProvinceName', 'California'),), (('organizationName', 'Zscaler Inc.'),), (('organizationalUnitName', 'Zscaler Inc.'),), (('commonName', 'Zscaler Intermediate Root CA (zscalerthree.net) (t) '),)), 'version': 3, 'serialNumber': '67A7EB7DDC67A4EB59C8B95912934639', 'notBefore': 'Sep 17 17:09:27 2022 GMT', 'notAfter': 'Oct  1 17:09:27 2022 GMT', 'subjectAltName': (('DNS', '*.etsystatic.com'), ('DNS', 'api-origin.etsy.com'), ('DNS', 'api.etsy.com'), ('DNS', 'm.etsy.com'), ('DNS', 'openapi.etsy.com'), ('DNS', 'www.etsy.com'), ('DNS', 'etsy.com')), 'crlDistributionPoints': ('http://gateway.zscalerthree.net/zscaler-zscrl--4.crl',)}
