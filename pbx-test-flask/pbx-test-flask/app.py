"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

values = [
    {
        'id': 1,
        'title': u'value1',
        'important': False
    },
    {
        'id': 2,
        'title': u'value2',
        'important': True
    }
]
# GET api/values 
@app.route('/api/values', methods=['GET'])
def get_values():
    return jsonify({'values': values})

# GET api/values/1
@app.route('/api/values/<int:value_id>', methods=['GET'])
def get_value(value_id):
    value = [value for value in values if value['id'] == value_id]
    if len(value) == 0:
        abort(404)
    return jsonify({'value': value[0]})

# POST api/values
@app.route('/api/values', methods=['POST'])
def create_value():
    if not request.json or not 'title' in request.json:
        abort(400)
    value = {
        'id': values[-1]['id'] + 1,
        'title': request.json['title'],
        'important': False
    }
    values.append(value)
    return jsonify({'value': value}), 201

# PUT api/values/1
@app.route('/api/values/<int:value_id>', methods=['PUT'])
def update_value(value_id):
    value = [value for value in values if value['id'] == value_id]
    if len(value) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'important' in request.json and type(request.json['important']) is not bool:
        abort(400)
    value[0]['title'] = request.json.get('title', value[0]['title'])
    value[0]['important'] = request.json.get('done', value[0]['done'])
    return jsonify({'value': value[0]})

# DELETE api/values/1
@app.route('/api/values/<int:value_id>', methods=['DELETE'])
def delete_value(value_id):
    value = [value for value in values if value['id'] == value_id]
    if len(value) == 0:
        abort(404)
    values.remove(value[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
