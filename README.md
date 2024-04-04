# piholesdk

## Usage

```python
In [2]: from piholesdk import PiHoleClient

pihole_node =  {"ssh_ip_address":"192.168.178.100",
               "ssh_username":"root",
               "ssh_password":"password"}

client = PiHoleClient(**pihole_node)

client.read_custom_list()

{'status': True,
 'message': 'Retrieved A record list.',
 'data': {'netbox.mteke.com': '192.168.178.102',
  'guacamole.mteke.com': '192.168.178.102',
  'pfsense.mteke.com': '192.168.178.1',
  'pihole.mteke.com': '192.168.178.100',
  'vault.mteke.com': '192.168.178.102',
  'jenkins.mteke.com': '192.168.178.102',
  'grafana.mteke.com': '192.168.178.102',
  'rabbitmq.mteke.com': '192.168.178.102',
  'portainer.mteke.com': '192.168.178.102',
  'proxmox03.mteke.com': '192.168.178.32',
  'proxmox01.mteke.com': '192.168.178.30',
  'proxmox02.mteke.com': '192.168.178.31',
  'yangsuite.mteke.com': '192.168.178.102',
  'homeassistant.mteke.com': '192.168.178.161',
  'prometheus.mteke.com': '192.168.178.103',
  'ubuntu.mteke.com': '192.168.178.97'}}

record = PiHoleClient.create_dns_record(hostname="jur", ip_address="6.6.6.9", domain="mteke.com")


client.push_dns_record(record)
Out[8]: {'status': True, 'message': 'A record added successfully.'}

In [9]: client.read_custom_list()
Out[9]: 
{'status': True,
 'message': 'Retrieved A record list.',
 'data': {'netbox.mteke.com': '192.168.178.102',
  'guacamole.mteke.com': '192.168.178.102',
  'pfsense.mteke.com': '192.168.178.1',
  'pihole.mteke.com': '192.168.178.100',
  'vault.mteke.com': '192.168.178.102',
  'jenkins.mteke.com': '192.168.178.102',
  'grafana.mteke.com': '192.168.178.102',
  'rabbitmq.mteke.com': '192.168.178.102',
  'portainer.mteke.com': '192.168.178.102',
  'proxmox03.mteke.com': '192.168.178.32',
  'proxmox01.mteke.com': '192.168.178.30',
  'proxmox02.mteke.com': '192.168.178.31',
  'yangsuite.mteke.com': '192.168.178.102',
  'homeassistant.mteke.com': '192.168.178.161',
  'prometheus.mteke.com': '192.168.178.103',
  'ubuntu.mteke.com': '192.168.178.97',
  'jur.mteke.com': '6.6.6.9'}}

client.delete_dns_record(record)
Out[10]: {'status': True, 'message': 'A Record deleted successfully.'}

In [11]: client.read_custom_list()
Out[11]: 
{'status': True,
 'message': 'Retrieved A record list.',
 'data': {'netbox.mteke.com': '192.168.178.102',
  'guacamole.mteke.com': '192.168.178.102',
  'pfsense.mteke.com': '192.168.178.1',
  'pihole.mteke.com': '192.168.178.100',
  'vault.mteke.com': '192.168.178.102',
  'jenkins.mteke.com': '192.168.178.102',
  'grafana.mteke.com': '192.168.178.102',
  'rabbitmq.mteke.com': '192.168.178.102',
  'portainer.mteke.com': '192.168.178.102',
  'proxmox03.mteke.com': '192.168.178.32',
  'proxmox01.mteke.com': '192.168.178.30',
  'proxmox02.mteke.com': '192.168.178.31',
  'yangsuite.mteke.com': '192.168.178.102',
  'homeassistant.mteke.com': '192.168.178.161',
  'prometheus.mteke.com': '192.168.178.103',
  'ubuntu.mteke.com': '192.168.178.97'}}

```
