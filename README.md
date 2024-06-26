# PiHoleClient
![alt text](images/image.png)

This Python module provides a class PiHoleClient that allows you to interact with a Pi-hole server via SSH. It uses the paramiko library to establish the SSH connection.

## Features
- Create DNS records
- Push DNS records to the Pi-hole server
- Delete DNS records from the Pi-hole server
- Read the custom list of DNS records from the Pi-hole server
- Close the SSH connection

## Usage
First, you need to create an instance of PiHoleClient with the SSH details of your Pi-hole server:
```python
from piholesdk import PiHoleClient

pihole_node =  {"ssh_ip_address":"192.168.178.100",
               "ssh_username":"root",
               "ssh_password":"password"}

client = PiHoleClient(**pihole_node)
```

You can then use the methods provided by the PiHoleClient class to interact with your Pi-hole server.
```python
client.read_custom_list()
{'status': True,
 'message': 'Retrieved A record list.',
 'data': {'netbox.domain.com': '192.168.178.102',
  'guacamole.domain.com': '192.168.178.102',
  'pfsense.domain.com': '192.168.178.1',
  'pihole.domain.com': '192.168.178.100',
  'vault.domain.com': '192.168.178.102',
  'jenkins.domain.com': '192.168.178.102',
  'grafana.domain.com': '192.168.178.102',
  'rabbitmq.domain.com': '192.168.178.102',
  'portainer.domain.com': '192.168.178.102',
  'proxmox03.domain.com': '192.168.178.32',
  'proxmox01.domain.com': '192.168.178.30',
  'proxmox02.domain.com': '192.168.178.31',
  'yangsuite.domain.com': '192.168.178.102',
  'homeassistant.domain.com': '192.168.178.161',
  'prometheus.domain.com': '192.168.178.103',
  'ubuntu.domain.com': '192.168.178.97'}}
```
Creating a DNS Record
```python
record = PiHoleClient.create_dns_record(hostname="jur", ip_address="6.6.6.9", domain="domain.com")
```

Pushing a DNS A Record to PiHole Server
```python
client.push_dns_record(record)
Out[8]: {'status': True, 'message': 'A record added successfully.'}
```

Deleting a DNS Record
```python
client.delete_dns_record(record)
{'status': True, 'message': 'A Record deleted successfully.'}
```


## Dependencies

Only Paramiko library

## Note
Please ensure that the user you are connecting with has the necessary permissions to perform the operations on the Pi-hole server.

