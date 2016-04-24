Spilled it
==========

### Development

Set up a remote to dokku
```
git remote add dokku dokku@dokku.me:spilledit
```
Replace dokku.me with the dokku server you want to deploy to.

Get gunicorn with pip
```
pip install gunicorn
```

Now start the server:
```
gunicorn server:app --reload
```

It will listen for requests at http://localhost:8000. When you make changes to the files, it will automatically reload the application.

To deploy your changes, commit, then
```
git push dokku master
```
