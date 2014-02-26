example-github-oauth-flask
==========================

Example Flask web-app to use GitHub API with OAuth

Requriements
------------

- Python 3.3+
- [Foreman](https://github.com/ddollar/foreman)

Prepare
-------

### 1. Register your application

Go to https://github.com/settings/applications/new

Authorization callback URL should be `http://localhost:5000/callback/github` 

### 2. Clone the repo and install dependencies

```sh
$ git clone https://github.com/orangain/example-github-oauth-flask.git
$ cd example-github-oauth-flask
$ virtualenv --python=python3 venv  # if you use virtualenv
$ . venv/bin/activate  # if you use virtualenv
(venv)$ pip install -r requirements.txt
```

### 3. Put config file 

`example-github-oauth-flask/.env`

```
GITHUB_CLIENT_ID=(Your app's client ID)
GITHUB_CLIENT_SECRET=(Your apps' client secret)
SESSION_SECRET_KEY=(Random string)
```

Run server
----------

```sh
(venv)$ foreman run python github_oauth.py
```

Visit [http://localhost:5000/](http://localhost:5000/)
