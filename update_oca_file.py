#!/bin/python3

import requests
import urllib

FILES = [
    ".editorconfig",
    ".pre-commit-config.yaml.jinja",
    ".pylintrc-mandatory.jinja",
    ".pylintrc.jinja",
    "{% if odoo_version > 12 %}.eslintrc.yml{% endif %}",
    "{% if odoo_version > 12 %}.isort.cfg{% endif %}",
    "{% if odoo_version > 12 %}.prettierrc.yml{% endif %}",
    "{% if odoo_version >= 13 %}.flake8{% endif %}",
]

base_url = "https://raw.githubusercontent.com/OCA/oca-addons-repo-template/master/src/"


REPLACE_BLOCKS = {
    ".pre-commit-config.yaml.jinja": [
        (b"""  - repo: https://github.com/acsone/setuptools-odoo
    rev: {{ repo_rev.setuptools_odoo }}
    hooks:
      - id: setuptools-odoo-make-default
      {%- if generate_requirements_txt %}
      - id: setuptools-odoo-get-requirements
        args:
          - --output
          - requirements.txt
          - --header
          - "# generated from manifests external_dependencies"
      {%- endif %}""", b""),
        (b"""{#- Older versions that differ a lot have their own hardcoded templates for readability #}
{%- if odoo_version < 13 %}
  {%- include "version-specific/mqt-compat/.pre-commit-config.yaml.jinja" %}

{%- elif odoo_version < 14 %}
  {%- include "version-specific/%s/.pre-commit-config.yaml.jinja" % odoo_version %}

{#- Newer versions without hacks are rendered here directly #}
{%- else %}""", b""),
        (b"rcfile=.pylintrc-mandatory\n{%- endif %}", b"rcfile=.pylintrc-mandatory"),
    ],
    ".pylintrc-mandatory.jinja": [
        (b"    translation-required,\n", b""),
        (b"""{%- if odoo_version < 13 %}
  {%- include "version-specific/mqt-compat/.pylintrc-mandatory.jinja" %}
{%- else %}\n""", b""),
        (b"reports=no\n{%- endif %}", b"reports=no"),
    ],
    ".pylintrc.jinja": [
        (b"""{%- if odoo_version < 13 %}
  {%- include "version-specific/mqt-compat/.pylintrc.jinja" %}
{%- else %}\n""", b""),
        (b".pylintrc-mandatory.jinja",
            b"{% if odoo_version >= 14 %}.pylintrc-mandatory{% endif %}.jinja"),
        (b"{% endblock %}\n{%- endif %}", b"{% endblock %}"),
    ],
}

def update_content(filename, content):
    if filename in REPLACE_BLOCKS:
        for before, after in REPLACE_BLOCKS[filename]:
            if not before in content:
                raise Exception(
                    f"The following block is missing in {filename}:\n {before}"
                    )
            content = content.replace(before, after)
    return content

for filename in FILES:
    url = urllib.parse.urljoin(base_url, urllib.parse.quote(filename))
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception(f"Fail to get file {url} response: {res.content}")
    content = update_content(filename, res.content)
    if filename in [
            ".pre-commit-config.yaml.jinja",
            ".pylintrc.jinja",
            ".pylintrc-mandatory.jinja",
            ]:
        filename = "{% if odoo_version >= 14 %}" + filename[:-6] + "{% endif %}.jinja"

    open(f"src/{filename}", 'wb').write(content)
