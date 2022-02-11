from email import header
import os
from unicodedata import name
from wsgiref import headers
import requests
netbox_ROOT = "https://178.74.59.186:4434"
Token = {'Authorization':'Token a6582fd99e88413997670f5c9c3e29c2d8115089'} 
Sites = "/api/dcim/sites/"

SITES = [
    {'name':'HMZ1',
    'slug':'hmz1'
    },
    {
    'name':'KRT1',
    'slug':'krt1'
    }
]

def add_site(name,slug):
    api_token = Token
    headers = {'Authorization': 'Token a6582fd99e88413997670f5c9c3e29c2d8115089',
    'Content-Type':'application/json',
    'Accept':'application/json' }
    data ={
    'name': name,
    'slug': slug
        }

    Re = requests.post(netbox_ROOT + Sites + "?",headers=headers, json=data ,verify=False)
    if Re.status_code== 201:
        print('Your Sites {name} has been created')
    else:
        print('Code NOT working')


def add_site():
    for site in SITES:
        add_site(**site)

def main():
    add_site()
if __name__ == '__main__':
    main()