#!/bin/python3

import requests
import urllib

FILES = [
    ".pre-commit-config.yaml.jinja",
    ".pylintrc-mandatory.jinja",
    ".pylintrc.jinja",
    "{% if odoo_version > 12 %}.eslintrc.yml{% endif %}",
    "{% if odoo_version > 12 %}.isort.cfg{% endif %}",
    "{% if odoo_version > 12 %}.prettierrc.yml{% endif %}",
    "{% if odoo_version >= 13 %}.flake8{% endif %}",
]

base_url = "https://raw.githubusercontent.com/OCA/oca-addons-repo-template/master/src/"

for filename in FILES:
    url = urllib.parse.urljoin(base_url, urllib.parse.quote(filename))
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception(f"Fail to get file {url} response: {res.content}")
    open(f"src/{filename}", 'wb').write(res.content)
