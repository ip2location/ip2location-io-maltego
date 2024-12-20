from maltego_trx.decorator_registry import TransformRegistry

registry = TransformRegistry(
        owner="IP2Location",
        author="IP2Location <support@ip2location.io>",
        # host_url="https://www.ip2location.io/",
        host_url="http://127.0.0.1:8080/run/ip2locationgeolocation/",
        seed_ids=["F9J53V7uvjlmjpU0gmXMAL8O"]
)

# The rest of these attributes are optional

# metadata
registry.version = "0.1"

# global settings
# from settings import ip2locationio_api_key_setting
# registry.global_settings = [ip2locationio_api_key_setting]

# transform suffix to indicate datasource
# registry.display_name_suffix = " [ACME]"

# reference OAuth settings
# registry.oauth_settings_id = ['github-oauth']
