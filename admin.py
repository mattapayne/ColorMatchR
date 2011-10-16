from google.appengine.ext import webapp
from google.appengine.ext import db
from helpers import *
#This is a test
class AdminPage(webapp.RequestHandler):
    def get(self):
		signups = db.GqlQuery("SELECT * FROM BetaSignup")
		template_data = {'signups': signups}
		render_template(self, template_name='admin.html', template_values=template_data)