from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment


env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')

ntp_servers = []
ntp_servers.append("130.126.24.24")
ntp_servers.append("152.2.21.1")

clock_settings = {
    "timezone": "PST",
    "timezone_offset": "-8 0",
    "timezone_dst": "PDT"
}

template_var = {
    "ntp_servers": ntp_servers,
    "clock_settings": clock_settings
}

template_file = 'cisco3.j2'
template = env.get_template(template_file)
output = template.render(**template_var)

print(output)

