from flask import Flask, jsonify, request, abort, send_from_directory, render_template

app = Flask(__name__, static_folder='../static')

# Mock database
items = [
    {"id": "1", "name": "Item One", "description": "This is item one"},
    {"id": "2", "name": "Item Two", "description": "This is item two"}
]

@app.route('/docs')
def swagger_ui():
    return render_template('swagger.html')

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/api/items', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json or not 'description' in request.json:
        abort(400)
    item = {
        'id': str(len(items) + 1),
        'name': request.json['name'],
        'description': request.json['description']
    }
    items.append(item)
    return jsonify(item), 201

@app.route('/api/items/<string:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        abort(404)
    return jsonify(item)

@app.route('/api/items/<string:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        abort(404)
    if not request.json:
        abort(400)
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

@app.route('/api/items/<string:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        abort(404)
    items = [item for item in items if item['id'] != item_id]
    return jsonify({}), 204

if __name__ == '__main__':
    app.run(debug=True)
