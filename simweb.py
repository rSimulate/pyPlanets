# Python dependencies, Bottle, pyMongo, virtualenv
import json
import bottle
import vitualenv
from bottle import route, run, request, abort
from pymongo import Connection

# URI Variables
mongoUri = process.env.MONGOLAB_URI || 'mongodb://localhost/bodiesReferenceEngine'
portno = 5016

# mongo database info
connection = Connection('localhost', 27017)
db = connection.mydatabase

# example functions from before

@route('/documents', method='PUT')
def put_document():
    data = request.body.readline()
    if not data:
        abort(400, 'No data received')
    entity = json.loads(data)
    if not entity.has_key('_id'):
        abort(400, 'No _id specified')
    try:
        db['documents'].save(entity)
    except ValidationError as ve:
        abort(400, str(ve))

@route('/documents/:id', method='GET')
def get_document(id):
    entity = db['documents'].find_one({'_id':id})
    if not entity:
        abort(404, 'No document with id %s' % id)
    return entity

# Start my conversion here

def getLinkByRel(links, rel):
    for i in links:
        if links[i].rel == rel:
            return links[i]
        else:
            return undefined

# Endpoint Resource

@route('/metasim/:version', method='GET')
def getVersion(request, response):
    if request.params.version == '1.0':
        response.send:
            links:
                rel: '/rel/simulations'
                href: '/metasim/' + request.params.version+ '/simulations'
                method: 'POST'
    else: abort(404, 'Version not found')





@route('/metasim/:version/simulations', method='GET')




run(host='localhost', port=portno)