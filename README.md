# OpenUpgrade from Odoo 8.0 to Odoo 9.0 Docky template

## Install Docker, then docky and ak
```
sudo pip install git+https://github.com/akretion/docky.git@master --upgrade
sudo pip install git+https://github.com/akretion/ak.git@master --upgrade
```

## Clone the project and build it

Clone the repo and then use ak to fetch teh required dependencies:
```
git clone https://github.com/akretion/docky-odoo-template.git -b 9.0-OpenUpgrade openupgrade9
cd openupgrade9/odoo
ak build
```

## Load your dump and migrate it

Copy your dump in ```odoo/backup/prod.dump```

Copy your filestore in ```./data/filestore/openupgrade9```

Start docky with ```docky run```

Now, inside the container, load your dump as a new database that we will keep for reference
and create a copy of it on which we will run the migration:
```
createdb prod-8.0
time psql prod-8.0 < /odoo/backup/prod.dump
createdb openupgrade9 -O odoo -T 8-prod
time odoo -d openupgrade-to-9 -u all --stop-after-init

```
