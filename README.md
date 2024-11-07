<!-- Copyright (c) 2024, AgriTheory and contributors
For license information, please see license.txt-->

## Gleap

Gleap Integration for ERPNext

## Install Instructions

Set up a new bench, substitute a path to the python version to use, which should 3.10 latest

```
# for linux development
bench init --frappe-branch version-14 {{ bench name }} --python ~/.pyenv/versions/3.10.10/bin/python3
```
Create a new site in that bench
```
cd {{ bench name }}
bench new-site {{ site name }} --force --db-name {{ site name }}
bench use {{ site name }}
```
Download the ERPNext app
```
bench get-app erpnext --branch version-15
```
Download this application and install all apps
```
bench get-app gleap git@github.com:WashmoreHoldings/gleap.git
```
Set developer mode in `site_config.json`
```
cd {{ site name }}
nano site_config.json

 "developer_mode": 1,
```

Update and get the site ready
```
bench start
```
In a new terminal window
```
bench update
bench migrate
bench build
```

To run mypy
```shell
source env/bin/activate
mypy ./apps/washmoreerp/washmoreerp --ignore-missing-imports
```

To run pytest
```shell
source env/bin/activate
pytest ~/frappe-bench/apps/washmoreerp/washmoreerp/tests -s
```
