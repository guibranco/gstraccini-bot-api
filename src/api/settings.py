from flask import Blueprint, request, jsonify

settings_api = Blueprint('settings_api', __name__)

# Mock settings data
bot_settings = {
    'setting1': 'value1',
    'setting2': 'value2'
}

@settings_api.route('/api/settings', methods=['GET'])
def get_settings():
    return jsonify(bot_settings)

@settings_api.route('/api/settings', methods=['PUT'])
def update_settings():
    data = request.json
    bot_settings.update(data)
    return jsonify({'message': 'Settings updated successfully', 'settings': bot_settings})
