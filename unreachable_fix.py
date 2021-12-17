import requests

url = "https://api.meraki.com/api/v1/organizations/520943/appliance/vpn/thirdPartyVPNPeers"

payload = '''{
    "peers": [
        {
            "name": "AWS-VPN",
            "publicIp": "52.72.0.237",
            "privateSubnets": [ "10.0.1.0/24" ],
            "secret": "uAow6xu6Wtuiszlru4T8Y0toU9NVn7zz",
            "remoteId": "52.72.0.237",
            "ikeVersion": "1",
            "ipsecPolicies": {
                "ikeCipherAlgo": [ "aes128" ],
                "ikeAuthAlgo": [ "sha1" ],
                "ikeDiffieHellmanGroup": [ "group2" ],
                "ikeLifetime": 28800,
                "childCipherAlgo": [ "aes128" ],
                "childAuthAlgo": [ "sha1" ],
                "childPfsGroup": [ "group2" ],
                "childLifetime": 3600
            },
            "networkTags": [ "all" ]
        }
    ]
}'''
print(type(payload))
print(payload)
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "5f0ea09fe6b80f40dc328785aa4fbabd75396658"
}

response = requests.request('PUT', url, headers=headers, data = payload)

print(response.text.encode('utf8'))