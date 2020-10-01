from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment


env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

vrf_var = {
    "VRF_NAME": "blue",
    "RD": "100:1",
    "IPv4_ENABLED": True,
    "IPv6_ENABLED": True
}


template_file = 'ex3.j2'
template = env.get_template(template_file)
output = template.render(**vrf_var)

print(output)


