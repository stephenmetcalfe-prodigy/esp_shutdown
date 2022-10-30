## ESP Shutdown Project

This project was born of a need to shut down a Linux server whenever Eskom decides we don't need power for a few hours.

### Suggested Usage
Set up a cron job as follows

`57 * * * * python3 /source_path/esp_shutdown.py #Check for loadshedding and shutdown`

You can either run the cron job as root, or (preferably) a user that has rights to call shutdown without needing to authenticate.
See [How to run sudo command without a password on a Linux or Unix](https://www.cyberciti.biz/faq/linux-unix-running-sudo-command-without-a-password/) for details on how to set this up.