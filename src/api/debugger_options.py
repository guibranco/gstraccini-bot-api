from flask import Blueprint, request, jsonify

debugger_options_bp = Blueprint('debugger_options', __name__)

# Mock configuration store
debugger_settings = {
    "all": True,
    "repositories": False,
    "issues": False,
    "pushes": False
}

@debugger_options_bp.route('/debugger-options', methods=['GET'])
def get_debugger_options():
    """Retrieve current debugger settings."""
    return jsonify(debugger_settings)

@debugger_options_bp.route('/debugger-options', methods=['PUT'])
def update_debugger_options():
    """Update debugger settings dynamically."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    # Validate input
    for key in data:
        if key not in debugger_settings:
            return jsonify({"error": "Invalid debugger option"}), 400
        if not isinstance(data[key], bool):
            return jsonify({"error": "Invalid data type for option"}), 400

    # Update settings
    debugger_settings.update(data)
    return jsonify({
        "status": "success",
        "message": "Debugger options updated successfully"
    })

# Add more routes or logic as needed for additional functionality
