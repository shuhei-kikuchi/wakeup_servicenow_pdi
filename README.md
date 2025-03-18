# Wakeup ServiceNow PDI(Personal Developer Instance)

## Overview

You may use ServiceNow PDI(Personal Developer Instance) for development or educational purposes. Unfortunately, ServiceNow  will delete your developer  instance after 10 days with no activity.To avoid deletion, this tool login to your ServiceNow Developer Account in a automated way and boot your instance.

## Content
    /
    ├── logs/                      # directory for video recordings and screenshots 
    ├── config.yaml.sample         
    ├── docker-compose.yaml
    ├── Dockerfile                 
    └── wakeup_snow_pdi.py         

    
## How to deploy
1. Install Docker and docker-compose.   Be sure to execute steps at https://docs.docker.com/engine/install/linux-postinstall/
2. Clone this repogitory by using  `git clone`
3. copy `config.yaml.sample` to `config.yaml` and edit values for email, password and instancename.
4. Execute: `docker compose pull`
5. Execute: `docker compose up`
   

