from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from my_devices import nxos1, nxos2
from netmiko import ConnectHandler


env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

nxos1_var = {
    "interface": "Ethernet1/2",
    "ip_address": "172.31.255.1/30",
    "local_as": 22,
    "peer_ip": "172.31.255.2"
}

nxos2_var = {
    "interface": "Ethernet1/2",
    "ip_address": "172.31.255.2/30",
    "local_as": 22,
    "peer_ip": "172.31.255.1"
}

template_file = 'ex2c.j2'
template = env.get_template(template_file)
nxos1_output = (template.render(**nxos1_var)).splitlines()
nxos2_output = (template.render(**nxos2_var)).splitlines()

net_connect = ConnectHandler(**nxos1)
output = net_connect.send_config_set(nxos1_output)
print(output)
net_connect.disconnect()

net_connect = ConnectHandler(**nxos2)
output = net_connect.send_config_set(nxos2_output)
print(output)
output = net_connect.send_command("ping 172.31.255.1")
print(output)
output = net_connect.send_command("show bgp all neighbors 172.31.255.1")
print(output)
net_connect.disconnect()


