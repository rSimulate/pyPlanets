# Python dependencies, Bottle, pyMongo, virtualenv
import json
import bottle
import virtualenv
import os
import logging

from bottle import route, run, request, abort
from pymongo import Connection

# URI Variables
mongoUri = os.getenv('MONGOLAB_URI', 'mongodb://localhost/pyPlanets')
portno = 5016

# mongo database info
#connection = Connection('localhost', 27017)
#db = connection.mydatabase

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

@route('/metasim', method='GET')
def getEndpoint():
    return json.dumps({
       'versions': [{
            'id': '1.0',
               'links': [{
                'rel': '/rel/entrypoint',
                'href': '/metasim/1.0',
                'method': 'GET'}]}]});

@route('/metasim/:version', method='GET')
def getVersion(version):
    if version == '1.0':
        return json.dumps({
            'links': {
                'rel': '/rel/simulations',
                'href': '/metasim/' + request.params.version+ '/simulations',
                'method': 'POST'}})
    else: abort(404, 'Version not found')


# Simulations Resource

@route('/metasim/:version/simulations', method='GET')
def getSimVer():
#     logging.info(json.dumps() ##I need help turning on logging##
    return json.dumps({
       'versions': [{
            'id': '1.0',
               'links': [{
                'rel': '/rel/entrypoint',
                'href': '/metasim/1.0',
                'method': 'GET'}]}]});

@route('/metasim/:version/simulations', method='GET')
def getSimulations(version):
    if version == '1.0':
        # Mongo calls need work
        db['simulations'].find_one({}).toArray(function(err, simulations)
        return json.dumps({
            'links': {
                'rel': '/rel/simulations',
                'href': '/metasim/' + request.params.version+ '/simulations',
                'method': 'POST'}})
    else: abort(404, 'Version not found')

# Create a new Simulation
@route('/metasim/:version/simulations', method='post')
def makeSimulation(version)):
    simulationUri = request.body.simulation_href
    # Console log here
    simulationID = simulationUri.split('/').slice(-1)
    # Create simulation object
    simulation =:
        simulation_href= request.body.simulation_href
    db.collection('simulations').insert(simulation)
    response.header('Location', url.format:
        protocol: 'http',
        hostname: request.host,
        port: port,
        pathname: request.originalUrl + '/' + simulationID + '/data'
    )
    response.send(201, bodies:
        radius: 1
        xyz_position: {x:5, y:0, z:0}
        xyz_velocity: {x:0, y:0, z:0}
    )


# Delete Simulations
@route('/metasim/:version/simulations', method='delete')
def deleteSimulation(version):
    version = request.params.version
    if version == '1.0':
        simulationID = request.params.id
        if db.collection('simulations').find_one(_id:simuilationID).count() > 0 :
            db.collection('simulations').remove(_id:simulationId)
            response.send(204, null)
        else:
            # Console dump
            response.send(404, 'version' + version + ' not found')

# Serve up Simulation data
@route('/metasim/:version/simulations/:id/data'):
def servSim():
    response.send({bodies:[{
        radius:1
        xyz_position: {x:5, y:0, z:0},
        xyz_velocity: {x:0, y:0, z:0}}]
        }
        )

# Port listener
app.listen(port, function() {
    # console.log
    }

run(host='localhost', port=portno)
