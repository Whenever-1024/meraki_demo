import yaml
payload = {
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
}
f = open("sample.yaml", "w")
yaml.dump(payload, f)
f.close()
