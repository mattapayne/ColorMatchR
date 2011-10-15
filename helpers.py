import os
from google.appengine.ext.webapp import template

def render_template(request, template_name, template_directory='views', template_values={}):
	path = __get_template_path(template_name, template_directory)
	request.response.out.write(template.render(path, template_values))
	
def __get_template_path(template_name, template_directory='views'):
	return os.path.join(os.path.dirname(__file__), template_directory, template_name)