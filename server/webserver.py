from giveawayInfo import *
import json
import cherrypy
import os
import sys

class webserver(object):
    @cherrypy.expose
    def index(self):
        pass
    
    @cherrypy.expose
    def get_keys(self):
        giveaway_obj = GiveawayInfo()
        web_content = giveaway_obj.get_web_content()
        keys = giveaway_obj.get_keys(web_content)
        json_keys = json.dumps({"keys": keys})
        return json_keys

conf = {
    '/': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': os.path.join(os.path.realpath(sys.path[0]), 'public'),
        'tools.staticdir.index': 'index.html',
    },
}

cherrypy.quickstart(webserver(), '/', conf)