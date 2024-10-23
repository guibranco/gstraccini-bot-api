from controllers.settings_controller import get_actual_settings

router.add_route('/actual-settings', get_actual_settings)