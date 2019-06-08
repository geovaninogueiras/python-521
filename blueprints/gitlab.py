
import flask
import requests

blueprint = flask.Blueprint('gitlab', __name__)

DOMAIN = 'https://gitlab.com/api/v4'
PROJECTS_URL = DOMAIN + '/projects?owned=true&private_token=1prFvNtqT6HhbXEz34QA'

@blueprint.route('/gitlab', methods=[ 'GET' ])
def get_gitlab():
    
    context = {
        'page': 'gitlab',
        'current_tab': flask.request.args.get('current_tab') or 'users',
        'route': {
            'is_public': False
        },
        'projetecs': requests.get(PROJECTS_URL).json()
    }

    return flask.render_template('gitlab.html', context=context)

@blueprint.route('/gitlab', methods=[ 'POST' ])
def post_gitlab():
    pass


@blueprint.route('/gitlab/<string:projectid>/commits', methods=[ 'GET' ])
def get_commits(projectid):
    
    COMMITS_URL =  DOMAIN + '/projects/'+projectid+'/repository/commits?private_token=1prFvNtqT6HhbXEz34QA'
    
    context = {
        'page': 'gitlab',
        'current_tab': flask.request.args.get('current_tab') or 'projects',
        'route': {
            'is_public': False
        },
        'commits': requests.get(COMMITS_URL).json()
    }

    return flask.render_template('gitlab.html', context=context)