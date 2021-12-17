import requests
import json
import yaml
import os
from django.conf import settings
from django.views.generic import TemplateView

OrgID = "520943"
OrgKey = "5f0ea09fe6b80f40dc328785aa4fbabd75396658"

class homeview(TemplateView):
    template_name = 'demo/status.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        
        if self.request.path == '/demo/getData':
            print('>>> getAPI() called')
            data, pconfig, sconfig = getVPNStatus()
            context['data'] = data
            context['pconfig'] = pconfig
            context['sconfig'] = sconfig            

        elif self.request.path.startswith('/demo/ConfigVPN'):            
            print('>>>We hit ConfigVPN!')
            
            ip=self.kwargs['ip']
            configVPN(ip)
            data, pconfig, sconfig = getVPNStatus()
            context['data'] = data
            context['pconfig'] = pconfig
            context['sconfig'] = sconfig  
            
        return context
       
def getVPNStatus():
    
    url = "https://api.meraki.com/api/v1/organizations/" + OrgID + "/appliance/vpn/statuses"
    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-KEY": OrgKey
    }

    response = requests.request('GET', url, headers=headers, data=payload)
    
    data = response.text[1:-1]
    data = json.loads(data)

    ### VPN Configurations
    primary_config = os.path.join(settings.BASE_DIR, 'primaryconfig.yml')
    secondary_config = os.path.join(settings.BASE_DIR, 'secondaryconfig.yml')
                
    with open(primary_config) as f:    
        pconfig = yaml.load(f, Loader=yaml.FullLoader)
    with open(secondary_config) as f:    
        sconfig = yaml.load(f, Loader=yaml.FullLoader)
        
    return data, pconfig, sconfig

def configVPN(ip):
    primary_config = os.path.join(settings.BASE_DIR, 'primaryconfig.yml')
    secondary_config = os.path.join(settings.BASE_DIR, 'secondaryconfig.yml')

    with open(primary_config) as pconfig:
        pvar = yaml.safe_load(pconfig)
    with open(secondary_config) as sconfig:
        svar = yaml.safe_load(sconfig)
        
    primaryip = pvar['peers'][0]['publicIp']
    secondaryip = svar['peers'][0]['publicIp']

    ### Example of API call to update VPN
    url = "https://api.meraki.com/api/v1/organizations/" + OrgID + "/appliance/vpn/thirdPartyVPNPeers"
    
    if ip == primaryip:
        payload = json.dumps(svar, indent=2)
    elif ip == secondaryip:
        payload = json.dumps(pvar, indent=2)
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": OrgKey
    }
    
    #########################################################
    # yaml file created manually FAIL
    # the reason is enter key
    # only yaml file created automatically by dicttoyaml.py
    #########################################################
    response = requests.request('PUT', url, headers=headers, data = payload)
    print(response.text.encode('utf8'))