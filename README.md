# Ak recipe for basic odoo project


Download this project or can Git clone and remove .git
```sh
$ git clone https://github.com/akretion/docky-odoo-template  odoo_project
odoo_project $ cd odoo_project
odoo_project $ rm -rf .git
```

Create a .env
```sh
odoo_project $ docky init
```

The .env is a docker-compose file where you can put environment variables.

Ensure docker-compose is well configured
```sh
odoo_project $ docker-compose config
```

Install and run ak: 
```sh
odoo_project $ cd odoo
odoo_project/odoo $ ak build
```

Run docky
```sh
odoo_project $ docky run
```

See ak and docky documentation for more help.
