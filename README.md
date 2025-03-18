# Wakeup ServiceNow PDI(Personal Development Instance)

## Overview

You may use ServiceNow PDI(Personal Development Instance) for development or educational purposes. Unfortunately, ServiceNow PDI will delete the created instance after 10 days of no activity if you have not logged in to your ServiceNow Account. To avoid deletion, this tool login to your ServiceNow Developer Account in a way that allows scheduled execution and automates booting development instances.

## Content
    /
    ├── logs/                      # directory for video recordings and screenshots 
    ├── config.yaml.sample         
    ├── docker-compose.yml         
    ├── Dockerfile                 
    └── wakeup_snow_pdi.py         

    
## How to deploy
1. Install Docker and docker-compose.   Be sure to execute steps at https://docs.docker.com/engine/install/linux-postinstall/
2. Clone this repogitory by using  `git clone`
3. copy `config.yaml.sample` to `config.yaml` and edit values for email, password and instancename.
4. Execute: `docker compose pull`
5. Execute: `docker compose up`
   

