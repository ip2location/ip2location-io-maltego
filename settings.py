from maltego_trx.decorator_registry import TransformSetting

ip2locationio_api_key_setting = TransformSetting(name='ip2locationioapikey',
                                   display_name='IP2Location.io API Key',
                                   setting_type='string',
                                   # global_setting=True,
                                   optional=False,
                                   popup=True)
