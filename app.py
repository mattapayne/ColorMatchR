from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from main import *
from admin import *

application = webapp.WSGIApplication(
                                     [('/', MainPage), ('/beta_signup', MainPage), ('/admin', AdminPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()