# ESP Shutdown Project

This project was born of a need to shut down a Linux server whenever Eskom decides we don't need power for a few hours.

### Requirements
This project makes use of the EskomSePush API. You will need a token to access the service: Subscribe [here](https://eskomsepush.gumroad.com/l/api).


### Suggested Usage
Set up a cron job as follows

`57 * * * * python3 /source_path/esp_shutdown.py #Check for loadshedding and shutdown`

You can either run the cron job as root, or (preferably) a user that has rights to call shutdown without needing to authenticate.
See [Run only specific sudo commands without password](https://linuxhandbook.com/sudo-without-password/#run-only-specific-sudo-commands-without-password) for details on how to set this up.

### Installation
Clone the repo and run `python3 esp_shutdown.py`

### Configuration
You will need to configure your API token as well as the area you are in. You can do this in `settings.ini`.
Your area code can be determined by using the EskomSePush API as follows:
`https://developer.sepush.co.za/business/2.0/areas_search/text=Sandton`

Take the resulting id for the area that fits you and put that under `Area` 

### To Do
- Add logging/reporting
- Refactor
- Add error handling
- Refactor..
- Wrap in service that can handle the cron management?
- Refactor....
