from flask import Blueprint, jsonify, request

label_settings_bp = Blueprint('label_settings', __name__)

# Mock data for label settings
label_settings = [
    {
        'name': 'bug',
        'color': '#d73a4a',
        'description': 'Indicates an unexpected problem or unintended behavior',
        'default': True,
        'category': 'issues'
    },
    {
        'name': 'feature',
        'color': '#a2eeef',
        'description': 'New feature or request',
        'default': False,
        'category': 'enhancements'
    }
]

@label_settings_bp.route('/v1/label-settings', methods=['GET'])
def get_label_settings():
    # Pagination
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    start = (page - 1) * per_page
    end = start + per_page

    # Filtering
    default = request.args.get('default')
    category = request.args.get('category')

    filtered_labels = label_settings
    if default is not None:
        filtered_labels = [label for label in filtered_labels if label['default'] == (default.lower() == 'true')]
    if category is not None:
        filtered_labels = [label for label in filtered_labels if label['category'] == category]

    # Paginate the filtered results
    paginated_labels = filtered_labels[start:end]

    return jsonify({
        'labels': paginated_labels,
        'total': len(filtered_labels),
        'page': page,
        'per_page': per_page
    })
