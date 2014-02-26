example-github-oauth-flask
==========================

Example Flask web-app to use GitHub API with OAuth

Requriements
------------

- Python 3.3+
- [Foreman](https://github.com/ddollar/foreman)

Prepare
-------

1. Register your application at https://github.com/settings/applications/new

   Authorization callback URL should be `http://localhost:5000/callback/github` 

2. Clone and install dependencies

```
$ git clone https://github.com/orangain/example-github-oauth-flask.git
$ cd example-github-oauth-flask
$ virtualenv --python=python3 venv  # if you use virtualenv
$ . venv/bin/activate  # if you use virtualenv
(venv)$ pip install -r requirements.txt
```

3. Create `.env` file 

```
GITHUB_CLIENT_ID=(Your Client ID)
GITHUB_CLIENT_SECRET=(Your Client Secret)
SESSION_SECRET_KEY=(Random string)
```

Run server
----------

```
(venv)$ foreman run python github_oauth.py
```
