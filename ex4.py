from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment


env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

vrf_list = []

vrf_blue = {
    "VRF_NAME": "blue",
    "RD": "100:1",
    "IPv4_ENABLED": True,
    "IPv6_ENABLED": True
}


vrf_red = {
    "VRF_NAME": "red",
    "RD": "200:2",
    "IPv4_ENABLED": True,
    "IPv6_ENABLED": True
}


vrf_green = {
    "VRF_NAME": "green",
    "RD": "300:3",
    "IPv4_ENABLED": True,
    "IPv6_ENABLED": True
}

vrf_yellow = {
    "VRF_NAME": "yellow",
    "RD": "400:4",
    "IPv4_ENABLED": True,
    "IPv6_ENABLED": True
}

vrf_white = {
    "VRF_NAME": "white",
    "RD": "500:5",
    "IPv4_ENABLED": True,
    "IPv6_ENABLED": True
}

vrf_list.append(vrf_blue)
vrf_list.append(vrf_red)
vrf_list.append(vrf_green)
vrf_list.append(vrf_yellow)
vrf_list.append(vrf_white)

var = {
    "vrf_list": vrf_list
}

template_file = 'ex4.j2'
template = env.get_template(template_file)
output = template.render(**var)

print(output)

