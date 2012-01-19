from django.core.handlers.wsgi import WSGIHandler

import environment


# setup the environment for Django
environment.setup_environ(__file__)

# set application for WSGI processing
application = WSGIHandler()