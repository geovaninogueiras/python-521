
import flask
import jenkins

blueprint = flask.Blueprint('jenkins', __name__)

connections = jenkins.Jenkins('http://localhost:8080', '4linux', '4linux123')

@blueprint.route('/jenkins', methods=[ 'GET' ])
def get_jenkins():
    
    context = {
        'page': 'jenkins',
        'route': {
            'is_public': False
        },
        'containers': connections.
    }

    return flask.render_template('jenkins.html', context=context)

@blueprint.route('/jenkins', methods=[ 'POST' ])
def post_jenkins():
    pass

@blueprint.route('/jenkins/update/<string:jobname>', methods=[ 'GET' ])
def get_jenkins_update(jobname):
    
    context = {
        'page': 'jenkins-update',
        'route': {
            'is_public': False
        },
        
    }

    return flask.render_template('jenkins_update.html', context=context)

@blueprint.route('/jenkins', methods=[ 'POST' ])
def post_jenkins_update():
    pass