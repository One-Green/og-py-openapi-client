
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from openapi_client.api.global_api import GlobalApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from openapi_client.api.global_api import GlobalApi
from openapi_client.api.light_api import LightApi
from openapi_client.api.sprinkler_api import SprinklerApi
from openapi_client.api.water_api import WaterApi
