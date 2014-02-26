# coding: utf-8

import os
import binascii

from flask import Flask, request, session, abort, redirect
from rauth import OAuth2Service

GITHUB_CLIENT_ID = os.environ['GITHUB_CLIENT_ID']
GITHUB_CLIENT_SECRET = os.environ['GITHUB_CLIENT_SECRET']

app = Flask(__name__)
app.secret_key = os.environ['SESSION_SECRET_KEY']

github = OAuth2Service(
    client_id=GITHUB_CLIENT_ID,
    client_secret=GITHUB_CLIENT_SECRET,
    name='github',
    authorize_url='https://github.com/login/oauth/authorize',
    access_token_url='https://github.com/login/oauth/access_token',
    base_url='https://api.github.com/')


@app.route('/')
def top():
    if 'username' in session:
        return 'Welcome @{0}! <a href="/repos">Repos</a> <a href="/logout">Logout</a>'.format(
            session['username'])

    if 'oauth_state' not in session:
        session['oauth_state'] = binascii.hexlify(os.urandom(24))

    authorize_url = github.get_authorize_url(scope='', state=session['oauth_state'])
    return '<a href="{0}">Sign in with GitHub</a>'.format(authorize_url)


@app.route('/callback/github')
def callback():
    code = request.args['code']
    state = request.args['state'].encode('utf-8')
    if state != session['oauth_state']:
        abort(400)

    auth_session = github.get_auth_session(data={'code': code})
    session['access_token'] = auth_session.access_token

    r = auth_session.get('/user')
    session['username'] = r.json()['login']

    return redirect('/')


@app.route('/logout')
def logout():
    session.pop('username')
    session.pop('access_token')

    return redirect('/')


@app.route('/repos')
def repos():
    auth_session = github.get_session(session['access_token'])
    r = auth_session.get('/user/repos')
    repos = r.json()

    return '<ul>{0}</ul>'.format(
        '\n'.join('<li>{0}</li>'.format(repo['full_name']) for repo in repos))

if __name__ == '__main__':
    app.run(debug=True)
