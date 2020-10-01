from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

nxos1 = {
    "interface": "Ethernet1/1",
    "ip_address": "10.1.100.1/24",
    "local_as": 22,
    "peer_ip": "10.1.100.2"
}

nxos2 = {
    "interface": "Ethernet1/1",
    "ip_address": "10.1.100.2/24",
    "local_as": 22,
    "peer_ip": "10.1.100.1"
}

template_file = 'ex2b.j2'
template = env.get_template(template_file)
nxos1_output = template.render(**nxos1)
nxos2_output = template.render(**nxos2)

print(nxos1_output)
print(nxos2_output)


