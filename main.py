from google.appengine.ext import webapp
from helpers import *
from models import *
import logging

class MainPage(webapp.RequestHandler):
    def get(self):
		param = self.request.get('r')
		template_values = {}
		if param and param == '1':
			template_values['message'] = "You've already signed up."
		elif param and param == '2':
			template_values['message'] = "Thanks for signing up for the beta program."
		render_template(self, 'index.html', template_values=template_values)
    def post(self):
		email = self.request.get('email')
		signup = db.GqlQuery("SELECT * FROM BetaSignup WHERE email = :1", email).get()
		if signup:
			self.redirect('/?r=1')
		else:
			signup = BetaSignup(email=email)
			signup.put()
			self.redirect('/?r=2')