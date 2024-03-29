# Basic Odoo project template used by [docky](https://github.com/akretion/docky)

This repo contains all the basic files needed to create an Odoo project from scratch using the [docky](https://github.com/akretion/docky) and [ak](https://github.com/akretion/ak) command-line tools developed by [Akretion](https://akretion.com).

To start a new Odoo project, you don't need to download this repo anymore:

1. First install [docky](https://github.com/akretion/docky) (version > 8.0.0), [copier](https://github.com/copier-org/copier) and [ak](https://github.com/akretion/ak)

For that we strongly recommend you to install them with [pipx](https://github.com/pypa/pipx)

```
pipx install docky
pipx install copier
pipx install git+https://github.com/akretion/ak.git@master
```

2. Create the project directory from a template with `copier copy`. For instance:

```
copier copy https://github.com/akretion/docky-odoo-template my-odoo-project
```

(you will then be asked to choose an Odoo version by copier).

3. Create the ".env" file

You can copy the ".env-sample" to ".env" and update enviroment variable if needed


4. Download the Odoo source code and other external modules specified in the [spec.yaml](odoo/spec.yaml) and [odoo-spec.yaml](odoo/odoo-spec.yaml) file using `ak build` from the spec.yaml's folder


```
cd odoo
ak build -c odoo-spec.yaml
ak build
```

> [ak](https://github.com/akretion/ak) use the [git-aggregator](https://github.com/acsone/git-aggregator) tool by [Acsone](https://www.acsone.eu/).
> More information on the [git-aggregator](https://github.com/acsone/git-aggregator) repo to understand how to fill the [spec.yaml](odoo/spec.yaml) file.


5. Once all the code is downloaded, go back to your project's root folder and launch `docky run`
```
cd ..
docky run
```

On the first `docky run`, docky will download the Odoo image referenced in the [DockerFile](odoo/Dockerfile) and run your different docker-compose files (basically docker-compose.yml, dev.docker-compose.yml or prod.docker-compose.yml) following the environment's variables registered in your **.env** file.

To reload the Odoo docker image or to update your docky after changing you environment variables, run `docky build`.

More information on : [docky](https://github.com/akretion/docky).


# Bump and Migration

When creating migration script (pre, post...) you can name the directory "0.0.0"
Indeed Odoo will always run migration script with the version "0.0.0" so you can use this as
the "current" migration script for your PR.
Then whenever you will run the cmd "./bump" it will set the right version number.


# Spec Tips (TODO move in ak doc ?)

```
social:
    modules:
        - mail_debrand
    src: https://github.com/OCA/social 14.0

server-auth:
  modules:
    - auth_oidc
  src: https://github.com/OCA/server-auth 14.0

# Recommended way: prefer short syntax without merges
# all stable modules from main branch
server-tools:
  modules:
    - base_technical_user
  src: https://github.com/OCA/server-tools 14.0

# and an dedicated entry (dir) for each
# pending branch in order to avoid merges.
server-tools-sentry:
  modules:
    - sentry
  src: https://github.com/akretion/server-tools 14.0-mig-sentry-sdk

# Alternative syntax
# not recommanded
# can also be used with multiple patch on the same module
server-brand:
    modules:
      - disable_odoo_online
      - remove_odoo_enterprise
    remotes:
        oca: https://github.com/OCA/server-brand
    #   ak: https://github.com/akretion/server-brand
    merges:
        - oca 14.0
        - oca refs/pull/39/head # PR for 'remove_odoo_enterprise'
        # - ak somebranch
```


# Tips for the template maintenance

## pre-commit

Precommit file are extracted from the OCA project https://github.com/OCA/oca-addons-repo-template

For updating the files you need to execute the file **update_oca_file.py**.
Then commit the updated files.
If files were added in the OCA, please update the script before.
