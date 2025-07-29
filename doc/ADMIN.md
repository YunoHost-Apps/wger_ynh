The default credentials are:
- username: admin
- password: adminadmin

But you can (understand: MUST!) change the password at your conveniance. 

After installation, if you wish to receive the data from the main instance (https://wger.de), you can run the following commands (official doc [here](https://wger.readthedocs.io/en/latest/administration/commands.html))

__INSTALL_DIR__/venv/bin/python manage.py sync-ingredients (this will take A LOT of time => several hours)
__INSTALL_DIR__/venv/bin/python manage.py sync-exercises
__INSTALL_DIR__/venv/bin/python manage.py download-exercise-images
__INSTALL_DIR__/venv/bin/python manage.py download-exercise-videos
__INSTALL_DIR__/venv/bin/python manage.py exercises-health-check

You can run all these commands or the one you choose.
But if you run all of them, it will take +-15GB of space in /home/yunohost.app/wger/media.

