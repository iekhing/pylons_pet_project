import logging

from helloworld.lib.base import *




log = logging.getLogger(__name__)

class LoginController(BaseController):

    def index(self):
        # Return a rendered template
        #   return render('/some/template.mako')
        # or, Return a response
        log.debug('start the index controller')
	log.debug('login userid %s', c.userId)
	return render('/login.mako')
   
    def verify(self):
	if  request.params.get('userId') == request.params.get('password'):
		log.info('login successful')
		c.loginStatus =True
		c.userId =request.params.get('userId')
		c.password = request.params.get('password') 
	else :
		log.info ('failed to login')
		c.loginStatus =False
		c.welcomeMessage = 'Login Failed'
	return render('/welcome.mako')
