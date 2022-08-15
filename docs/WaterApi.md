# og_client.WaterApi

All URIs are relative to *http://0.0.0.0:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**water_config_create**](WaterApi.md#water_config_create) | **POST** /water/config/ | 
[**water_config_delete**](WaterApi.md#water_config_delete) | **DELETE** /water/config/{id}/ | 
[**water_config_list**](WaterApi.md#water_config_list) | **GET** /water/config/ | 
[**water_config_partial_update**](WaterApi.md#water_config_partial_update) | **PATCH** /water/config/{id}/ | 
[**water_config_read**](WaterApi.md#water_config_read) | **GET** /water/config/{id}/ | 
[**water_config_update**](WaterApi.md#water_config_update) | **PUT** /water/config/{id}/ | 
[**water_controller_force_create**](WaterApi.md#water_controller_force_create) | **POST** /water/controller-force/ | 
[**water_controller_force_delete**](WaterApi.md#water_controller_force_delete) | **DELETE** /water/controller-force/{id}/ | 
[**water_controller_force_list**](WaterApi.md#water_controller_force_list) | **GET** /water/controller-force/ | 
[**water_controller_force_partial_update**](WaterApi.md#water_controller_force_partial_update) | **PATCH** /water/controller-force/{id}/ | 
[**water_controller_force_read**](WaterApi.md#water_controller_force_read) | **GET** /water/controller-force/{id}/ | 
[**water_controller_force_update**](WaterApi.md#water_controller_force_update) | **PUT** /water/controller-force/{id}/ | 
[**water_controller_list**](WaterApi.md#water_controller_list) | **GET** /water/controller/ | 
[**water_controller_read**](WaterApi.md#water_controller_read) | **GET** /water/controller/{id}/ | 
[**water_device_create**](WaterApi.md#water_device_create) | **POST** /water/device/ | 
[**water_device_delete**](WaterApi.md#water_device_delete) | **DELETE** /water/device/{id}/ | 
[**water_device_list**](WaterApi.md#water_device_list) | **GET** /water/device/ | 
[**water_device_partial_update**](WaterApi.md#water_device_partial_update) | **PATCH** /water/device/{id}/ | 
[**water_device_read**](WaterApi.md#water_device_read) | **GET** /water/device/{id}/ | 
[**water_device_update**](WaterApi.md#water_device_update) | **PUT** /water/device/{id}/ | 
[**water_sensor_list**](WaterApi.md#water_sensor_list) | **GET** /water/sensor/ | 
[**water_sensor_read**](WaterApi.md#water_sensor_read) | **GET** /water/sensor/{id}/ | 


# **water_config_create**
> WaterConfiguration water_config_create(data)



### Example

* Basic Authentication (Basic):

```python
import time
import og_client
from og_client.api import water_api
from og_client.model.water_configuration import WaterConfiguration
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = og_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = og_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with og_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    data = WaterConfiguration(
        ph_min_level=3.14,
        ph_max_level=3.14,
        tds_min_level=3.14,
        tds_max_level=3.14,
        water_tank_height=3.14,
        nutrient_tank_height=3.14,
        ph_downer_tank_height=3.14,
        tag=1,
    ) # WaterConfiguration | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.water_config_create(data)
        pprint(api_response)
    except og_client.ApiException as e:
        print("Exception when calling WaterApi->water_config_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WaterConfiguration**](WaterConfiguration.md)|  |

### Return type

[**WaterConfiguration**](WaterConfiguration.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **water_config_delete**
> water_config_delete(id)



### Example

* Basic Authentication (Basic):

```python
import time
import og_client
from og_client.api import water_api
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = og_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = og_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with og_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    id = 1 # int | A unique integer value identifying this config.

    # example passing only required values which don't have defaults set
    try:
        api_instance.water_config_delete(id)
    except og_client.ApiException as e:
        print("Exception when calling WaterApi->water_config_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config. |

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **water_config_list**
> WaterConfigList200Response water_config_list()



### Example

* Basic Authentication (Basic):

```python
import time
import og_client
from og_client.api import water_api
from og_client.model.water_config_list200_response import WaterConfigList200Response
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = og_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = og_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with og_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    search = "search_example" # str | A search term. (optional)
    page = 1 # int | A page number within the paginated result set. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.water_config_list(search=search, page=page)
        pprint(api_response)
    except og_client.ApiException as e:
        print("Exception when calling WaterApi->water_config_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional]
 **page** | **int**| A page number within the paginated result set. | [optional]

### Return type

[**WaterConfigList200Response**](WaterConfigList200Response.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **water_config_partial_update**
> WaterConfiguration water_config_partial_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import og_client
from og_client.api import water_api
from og_client.model.water_configuration import WaterConfiguration
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = og_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = og_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with og_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    id = 1 # int | A unique integer value identifying this config.
    data = WaterConfiguration(
        ph_min_level=3.14,
        ph_max_level=3.14,
        tds_min_level=3.14,
        tds_max_level=3.14,
        water_tank_height=3.14,
        nutrient_tank_height=3.14,
        ph_downer_tank_height=3.14,
        tag=1,
    ) # WaterConfiguration | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.water_config_partial_update(id, data)
        pprint(api_response)
    except og_client.ApiException as e:
        print("Exception when calling WaterApi->water_config_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config. |
 **data** | [**WaterConfiguration**](WaterConfiguration.md)|  |

### Return type

[**WaterConfiguration**](WaterConfiguration.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **water_config_read**
> WaterConfiguration water_config_read(id)



### Example

* Basic Authentication (Basic):

```python
import time
import og_client
from og_client.api import water_api
from og_client.model.water_configuration import WaterConfiguration
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = og_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = og_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with og_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    id = 1 # int | A unique integer value identifying this config.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.water_config_read(id)
        pprint(api_response)
    except og_client.ApiException as e:
        print("Exception when calling WaterApi->water_config_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config. |

### Return type

[**WaterConfiguration**](WaterConfiguration.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **water_config_update**
> WaterConfiguration water_config_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import og_client
from og_client.api import water_api
from og_client.model.water_configuration import WaterConfiguration
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = og_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = og_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with og_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    id = 1 # int | A unique integer value identifying this config.
    data = WaterConfiguration(
        ph_min_level=3.14,
        ph_max_level=3.14,
        tds_min_level=3.14,
        tds_max_level=3.14,
        water_tank_height=3.14,
        nutrient_tank_height=3.14,
        ph_downer_tank_height=3.14,
        tag=1,
    ) # WaterConfiguration | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.water_config_update(id, data)
        pprint(api_response)
    except og_client.ApiException as e:
        print("Exception when calling WaterApi->water_config_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config. |
 **data** | [**WaterConfiguration**](WaterConfiguration.md)|  |

### Return type

[**WaterConfiguration**](WaterConfiguration.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **water_controller_force_create**
> WaterForceController water_controller_force_create(data)



### Example

* Basic Authentication (Basic):

```python
import time
import og_client
from og_client.api import water_api
from og_client.model.water_force_controller import WaterForceController
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = og_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = og_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with og_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    data = WaterForceController(
        force_water_pump_signal=True,
        force_nutrient_pump_signal=True,
        force_ph_downer_pump_signal=True,
        force_mixer_pump_signal=True,
        water_pump_signal=True,
        nutrient_pump_signal=True,
        ph_downer_pump_signal=True,
        mixer_pump_signal=True,
        tag=1,
    ) # WaterForceController | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.water_controller_force_create(data)
        pprint(api_response)
    except og_client.ApiException as e:
        print("Exception when calling WaterApi->water_controller_force_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WaterForceController**](WaterForceController.md)|  |

### Return type

[**WaterForceController**](WaterForceController.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **water_controller_force_delete**
> water_controller_force_delete(id)



### Example

* Basic Authentication (Basic):

```python
import time
import og_client
from og_client.api import water_api
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = og_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = og_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with og_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    id = 1 # int | A unique integer value identifying this force controller.

    # example passing only required values which don't have defaults set
    try:
        api_instance.water_controller_force_delete(id)
    except og_client.ApiException as e:
        print("Exception when calling WaterApi->water_controller_force_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this force controller. |

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **water_controller_force_list**
> WaterControllerForceList200Response water_controller_force_list()



### Example

* Basic Authentication (Basic):

```python
import time
import og_client
from og_client.api import water_api
from og_client.model.water_controller_force_list200_response import WaterControllerForceList200Response
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = og_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = og_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with og_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    search = "search_example" # str | A search term. (optional)
    page = 1 # int | A page number within the paginated result set. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.water_controller_force_list(search=search, page=page)
        pprint(api_response)
    except og_client.ApiException as e:
        print("Exception when calling WaterApi->water_controller_force_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional]
 **page** | **int**| A page number within the paginated result set. | [optional]

### Return type

[**WaterControllerForceList200Response**](WaterControllerForceList200Response.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **water_controller_force_partial_update**
> WaterForceController water_controller_force_partial_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import og_client
from og_client.api import water_api
from og_client.model.water_force_controller import WaterForceController
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = og_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = og_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with og_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    id = 1 # int | A unique integer value identifying this force controller.
    data = WaterForceController(
        force_water_pump_signal=True,
        force_nutrient_pump_signal=True,
        force_ph_downer_pump_signal=True,
        force_mixer_pump_signal=True,
        water_pump_signal=True,
        nutrient_pump_signal=True,
        ph_downer_pump_signal=True,
        mixer_pump_signal=True,
        tag=1,
    ) # WaterForceController | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.water_controller_force_partial_update(id, data)
        pprint(api_response)
    except og_client.ApiException as e:
        print("Exception when calling WaterApi->water_controller_force_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this force controller. |
 **data** | [**WaterForceController**](WaterForceController.md)|  |

### Return type

[**WaterForceController**](WaterForceController.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **water_controller_force_read**
> WaterForceController water_controller_force_read(id)



### Example

* Basic Authentication (Basic):

```python
import time
import og_client
from og_client.api import water_api
from og_client.model.water_force_controller import WaterForceController
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = og_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = og_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with og_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    id = 1 # int | A unique integer value identifying this force controller.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.water_controller_force_read(id)
        pprint(api_response)
    except og_client.ApiException as e:
        print("Exception when calling WaterApi->water_controller_force_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this force controller. |

### Return type

[**WaterForceController**](WaterForceController.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **water_controller_force_update**
> WaterForceController water_controller_force_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import og_client
from og_client.api import water_api
from og_client.model.water_force_controller import WaterForceController
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = og_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = og_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with og_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    id = 1 # int | A unique integer value identifying this force controller.
    data = WaterForceController(
        force_water_pump_signal=True,
        force_nutrient_pump_signal=True,
        force_ph_downer_pump_signal=True,
        force_mixer_pump_signal=True,
        water_pump_signal=True,
        nutrient_pump_signal=True,
        ph_downer_pump_signal=True,
        mixer_pump_signal=True,
        tag=1,
    ) # WaterForceController | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.water_controller_force_update(id, data)
        pprint(api_response)
    except og_client.ApiException as e:
        print("Exception when calling WaterApi->water_controller_force_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this force controller. |
 **data** | [**WaterForceController**](WaterForceController.md)|  |

### Return type

[**WaterForceController**](WaterForceController.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **water_controller_list**
> WaterControllerList200Response water_controller_list()



Iot tag based controller live action to take only get because always updated by Iot Controller

### Example

* Basic Authentication (Basic):

```python
import time
import og_client
from og_client.api import water_api
from og_client.model.water_controller_list200_response import WaterControllerList200Response
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = og_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = og_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with og_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    search = "search_example" # str | A search term. (optional)
    page = 1 # int | A page number within the paginated result set. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.water_controller_list(search=search, page=page)
        pprint(api_response)
    except og_client.ApiException as e:
        print("Exception when calling WaterApi->water_controller_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional]
 **page** | **int**| A page number within the paginated result set. | [optional]

### Return type

[**WaterControllerList200Response**](WaterControllerList200Response.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **water_controller_read**
> WaterController water_controller_read(id)



Iot tag based controller live action to take only get because always updated by Iot Controller

### Example

* Basic Authentication (Basic):

```python
import time
import og_client
from og_client.api import water_api
from og_client.model.water_controller import WaterController
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = og_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = og_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with og_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    id = 1 # int | A unique integer value identifying this controller.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.water_controller_read(id)
        pprint(api_response)
    except og_client.ApiException as e:
        print("Exception when calling WaterApi->water_controller_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this controller. |

### Return type

[**WaterController**](WaterController.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **water_device_create**
> WaterDevice water_device_create(data)



### Example

* Basic Authentication (Basic):

```python
import time
import og_client
from og_client.api import water_api
from og_client.model.water_device import WaterDevice
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = og_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = og_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with og_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    data = WaterDevice(
        tag="tag_example",
    ) # WaterDevice | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.water_device_create(data)
        pprint(api_response)
    except og_client.ApiException as e:
        print("Exception when calling WaterApi->water_device_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WaterDevice**](WaterDevice.md)|  |

### Return type

[**WaterDevice**](WaterDevice.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **water_device_delete**
> water_device_delete(id)



### Example

* Basic Authentication (Basic):

```python
import time
import og_client
from og_client.api import water_api
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = og_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = og_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with og_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    id = 1 # int | A unique integer value identifying this device.

    # example passing only required values which don't have defaults set
    try:
        api_instance.water_device_delete(id)
    except og_client.ApiException as e:
        print("Exception when calling WaterApi->water_device_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this device. |

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **water_device_list**
> WaterDeviceList200Response water_device_list()



### Example

* Basic Authentication (Basic):

```python
import time
import og_client
from og_client.api import water_api
from og_client.model.water_device_list200_response import WaterDeviceList200Response
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = og_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = og_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with og_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    search = "search_example" # str | A search term. (optional)
    page = 1 # int | A page number within the paginated result set. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.water_device_list(search=search, page=page)
        pprint(api_response)
    except og_client.ApiException as e:
        print("Exception when calling WaterApi->water_device_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional]
 **page** | **int**| A page number within the paginated result set. | [optional]

### Return type

[**WaterDeviceList200Response**](WaterDeviceList200Response.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **water_device_partial_update**
> WaterDevice water_device_partial_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import og_client
from og_client.api import water_api
from og_client.model.water_device import WaterDevice
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = og_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = og_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with og_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    id = 1 # int | A unique integer value identifying this device.
    data = WaterDevice(
        tag="tag_example",
    ) # WaterDevice | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.water_device_partial_update(id, data)
        pprint(api_response)
    except og_client.ApiException as e:
        print("Exception when calling WaterApi->water_device_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this device. |
 **data** | [**WaterDevice**](WaterDevice.md)|  |

### Return type

[**WaterDevice**](WaterDevice.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **water_device_read**
> WaterDevice water_device_read(id)



### Example

* Basic Authentication (Basic):

```python
import time
import og_client
from og_client.api import water_api
from og_client.model.water_device import WaterDevice
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = og_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = og_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with og_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    id = 1 # int | A unique integer value identifying this device.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.water_device_read(id)
        pprint(api_response)
    except og_client.ApiException as e:
        print("Exception when calling WaterApi->water_device_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this device. |

### Return type

[**WaterDevice**](WaterDevice.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **water_device_update**
> WaterDevice water_device_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import og_client
from og_client.api import water_api
from og_client.model.water_device import WaterDevice
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = og_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = og_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with og_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    id = 1 # int | A unique integer value identifying this device.
    data = WaterDevice(
        tag="tag_example",
    ) # WaterDevice | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.water_device_update(id, data)
        pprint(api_response)
    except og_client.ApiException as e:
        print("Exception when calling WaterApi->water_device_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this device. |
 **data** | [**WaterDevice**](WaterDevice.md)|  |

### Return type

[**WaterDevice**](WaterDevice.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **water_sensor_list**
> WaterSensorList200Response water_sensor_list()



IoT tag based sensors live values only get because always updated by IoT

### Example

* Basic Authentication (Basic):

```python
import time
import og_client
from og_client.api import water_api
from og_client.model.water_sensor_list200_response import WaterSensorList200Response
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = og_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = og_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with og_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    search = "search_example" # str | A search term. (optional)
    page = 1 # int | A page number within the paginated result set. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.water_sensor_list(search=search, page=page)
        pprint(api_response)
    except og_client.ApiException as e:
        print("Exception when calling WaterApi->water_sensor_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional]
 **page** | **int**| A page number within the paginated result set. | [optional]

### Return type

[**WaterSensorList200Response**](WaterSensorList200Response.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **water_sensor_read**
> WaterSensor water_sensor_read(id)



IoT tag based sensors live values only get because always updated by IoT

### Example

* Basic Authentication (Basic):

```python
import time
import og_client
from og_client.api import water_api
from og_client.model.water_sensor import WaterSensor
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = og_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = og_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with og_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = water_api.WaterApi(api_client)
    id = 1 # int | A unique integer value identifying this sensor.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.water_sensor_read(id)
        pprint(api_response)
    except og_client.ApiException as e:
        print("Exception when calling WaterApi->water_sensor_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sensor. |

### Return type

[**WaterSensor**](WaterSensor.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

