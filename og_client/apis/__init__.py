
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from og_client.api.global_api import GlobalApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from og_client.api.global_api import GlobalApi
from og_client.api.light_api import LightApi
from og_client.api.sprinkler_api import SprinklerApi
from og_client.api.water_api import WaterApi
