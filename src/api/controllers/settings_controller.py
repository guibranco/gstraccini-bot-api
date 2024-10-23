from flask import jsonify

# Mock function to get current settings
def fetch_current_settings():
    # This function should interact with the actual configuration source
    return [
        {
            "name": "owner",
            "value": "guibranco",
            "category": "github",
            "last_updated": "2024-09-12T14:25:00Z"
        },
        {
            "name": "botname",
            "value": "gstraccini",
            "category": "system",
            "last_updated": "2024-09-10T09:15:00Z"
        }
    ]

def get_actual_settings():
    settings = fetch_current_settings()
    return jsonify({"settings": settings})