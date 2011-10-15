from google.appengine.ext import db

class BetaSignup(db.Model):
	email = db.StringProperty()
	signup_date = db.DateTimeProperty(auto_now_add=True)