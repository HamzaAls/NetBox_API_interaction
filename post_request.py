from email import header
import os
from unicodedata import name
from wsgiref import headers
import requests
netbox_ROOT = "https://IP:PORTnumber"
Token = {'Authorization':'Token '} 
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
    headers = {'Authorization': 'Token ',
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
