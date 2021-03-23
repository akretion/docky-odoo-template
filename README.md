# Ak recipe for basic odoo project


Download this project files:
```sh
$ wget -qO - https://api.github.com/repos/akretion/docky-odoo-template/tarball/14.0 | tar xvz
$ mv akretion-docky-odoo-template-* odoo_project
```

Create a .env
```sh
$ cd odoo_project
odoo_project $ docky init
```

The .env is a docker-compose file where you can put environment variables.

Ensure docker-compose is well configured
```sh
odoo_project $ docker-compose config
```

Install and run ak in odoo folder:
```sh
odoo_project $ cd odoo
odoo_project/odoo $ ak build
```

Run docky
```sh
odoo_project $ docky run
```

See ak and docky documentation for more help.
