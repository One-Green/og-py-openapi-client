# openapi_client.SprinklerApi

All URIs are relative to *http://0.0.0.0:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sprinkler_config_create**](SprinklerApi.md#sprinkler_config_create) | **POST** /sprinkler/config/ | 
[**sprinkler_config_delete**](SprinklerApi.md#sprinkler_config_delete) | **DELETE** /sprinkler/config/{id}/ | 
[**sprinkler_config_list**](SprinklerApi.md#sprinkler_config_list) | **GET** /sprinkler/config/ | 
[**sprinkler_config_partial_update**](SprinklerApi.md#sprinkler_config_partial_update) | **PATCH** /sprinkler/config/{id}/ | 
[**sprinkler_config_read**](SprinklerApi.md#sprinkler_config_read) | **GET** /sprinkler/config/{id}/ | 
[**sprinkler_config_update**](SprinklerApi.md#sprinkler_config_update) | **PUT** /sprinkler/config/{id}/ | 
[**sprinkler_controller_force_create**](SprinklerApi.md#sprinkler_controller_force_create) | **POST** /sprinkler/controller-force/ | 
[**sprinkler_controller_force_delete**](SprinklerApi.md#sprinkler_controller_force_delete) | **DELETE** /sprinkler/controller-force/{id}/ | 
[**sprinkler_controller_force_list**](SprinklerApi.md#sprinkler_controller_force_list) | **GET** /sprinkler/controller-force/ | 
[**sprinkler_controller_force_partial_update**](SprinklerApi.md#sprinkler_controller_force_partial_update) | **PATCH** /sprinkler/controller-force/{id}/ | 
[**sprinkler_controller_force_read**](SprinklerApi.md#sprinkler_controller_force_read) | **GET** /sprinkler/controller-force/{id}/ | 
[**sprinkler_controller_force_update**](SprinklerApi.md#sprinkler_controller_force_update) | **PUT** /sprinkler/controller-force/{id}/ | 
[**sprinkler_controller_list**](SprinklerApi.md#sprinkler_controller_list) | **GET** /sprinkler/controller/ | 
[**sprinkler_controller_read**](SprinklerApi.md#sprinkler_controller_read) | **GET** /sprinkler/controller/{id}/ | 
[**sprinkler_device_create**](SprinklerApi.md#sprinkler_device_create) | **POST** /sprinkler/device/ | 
[**sprinkler_device_delete**](SprinklerApi.md#sprinkler_device_delete) | **DELETE** /sprinkler/device/{id}/ | 
[**sprinkler_device_list**](SprinklerApi.md#sprinkler_device_list) | **GET** /sprinkler/device/ | 
[**sprinkler_device_partial_update**](SprinklerApi.md#sprinkler_device_partial_update) | **PATCH** /sprinkler/device/{id}/ | 
[**sprinkler_device_read**](SprinklerApi.md#sprinkler_device_read) | **GET** /sprinkler/device/{id}/ | 
[**sprinkler_device_update**](SprinklerApi.md#sprinkler_device_update) | **PUT** /sprinkler/device/{id}/ | 
[**sprinkler_sensor_list**](SprinklerApi.md#sprinkler_sensor_list) | **GET** /sprinkler/sensor/ | 
[**sprinkler_sensor_read**](SprinklerApi.md#sprinkler_sensor_read) | **GET** /sprinkler/sensor/{id}/ | 


# **sprinkler_config_create**
> SprinklerConfiguration sprinkler_config_create(data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import sprinkler_api
from openapi_client.model.sprinkler_configuration import SprinklerConfiguration
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sprinkler_api.SprinklerApi(api_client)
    data = SprinklerConfiguration(
        soil_moisture_min_level=3.14,
        soil_moisture_max_level=3.14,
        tag=1,
        water_tag_link=1,
    ) # SprinklerConfiguration | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.sprinkler_config_create(data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SprinklerApi->sprinkler_config_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SprinklerConfiguration**](SprinklerConfiguration.md)|  |

### Return type

[**SprinklerConfiguration**](SprinklerConfiguration.md)

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

# **sprinkler_config_delete**
> sprinkler_config_delete(id)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import sprinkler_api
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sprinkler_api.SprinklerApi(api_client)
    id = 1 # int | A unique integer value identifying this config.

    # example passing only required values which don't have defaults set
    try:
        api_instance.sprinkler_config_delete(id)
    except openapi_client.ApiException as e:
        print("Exception when calling SprinklerApi->sprinkler_config_delete: %s\n" % e)
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

# **sprinkler_config_list**
> SprinklerConfigList200Response sprinkler_config_list()



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import sprinkler_api
from openapi_client.model.sprinkler_config_list200_response import SprinklerConfigList200Response
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sprinkler_api.SprinklerApi(api_client)
    search = "search_example" # str | A search term. (optional)
    page = 1 # int | A page number within the paginated result set. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.sprinkler_config_list(search=search, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SprinklerApi->sprinkler_config_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional]
 **page** | **int**| A page number within the paginated result set. | [optional]

### Return type

[**SprinklerConfigList200Response**](SprinklerConfigList200Response.md)

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

# **sprinkler_config_partial_update**
> SprinklerConfiguration sprinkler_config_partial_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import sprinkler_api
from openapi_client.model.sprinkler_configuration import SprinklerConfiguration
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sprinkler_api.SprinklerApi(api_client)
    id = 1 # int | A unique integer value identifying this config.
    data = SprinklerConfiguration(
        soil_moisture_min_level=3.14,
        soil_moisture_max_level=3.14,
        tag=1,
        water_tag_link=1,
    ) # SprinklerConfiguration | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.sprinkler_config_partial_update(id, data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SprinklerApi->sprinkler_config_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config. |
 **data** | [**SprinklerConfiguration**](SprinklerConfiguration.md)|  |

### Return type

[**SprinklerConfiguration**](SprinklerConfiguration.md)

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

# **sprinkler_config_read**
> SprinklerConfiguration sprinkler_config_read(id)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import sprinkler_api
from openapi_client.model.sprinkler_configuration import SprinklerConfiguration
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sprinkler_api.SprinklerApi(api_client)
    id = 1 # int | A unique integer value identifying this config.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.sprinkler_config_read(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SprinklerApi->sprinkler_config_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config. |

### Return type

[**SprinklerConfiguration**](SprinklerConfiguration.md)

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

# **sprinkler_config_update**
> SprinklerConfiguration sprinkler_config_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import sprinkler_api
from openapi_client.model.sprinkler_configuration import SprinklerConfiguration
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sprinkler_api.SprinklerApi(api_client)
    id = 1 # int | A unique integer value identifying this config.
    data = SprinklerConfiguration(
        soil_moisture_min_level=3.14,
        soil_moisture_max_level=3.14,
        tag=1,
        water_tag_link=1,
    ) # SprinklerConfiguration | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.sprinkler_config_update(id, data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SprinklerApi->sprinkler_config_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config. |
 **data** | [**SprinklerConfiguration**](SprinklerConfiguration.md)|  |

### Return type

[**SprinklerConfiguration**](SprinklerConfiguration.md)

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

# **sprinkler_controller_force_create**
> SprinklerForceController sprinkler_controller_force_create(data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import sprinkler_api
from openapi_client.model.sprinkler_force_controller import SprinklerForceController
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sprinkler_api.SprinklerApi(api_client)
    data = SprinklerForceController(
        force_water_valve_signal=True,
        water_valve_signal=True,
        tag=1,
    ) # SprinklerForceController | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.sprinkler_controller_force_create(data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SprinklerApi->sprinkler_controller_force_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SprinklerForceController**](SprinklerForceController.md)|  |

### Return type

[**SprinklerForceController**](SprinklerForceController.md)

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

# **sprinkler_controller_force_delete**
> sprinkler_controller_force_delete(id)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import sprinkler_api
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sprinkler_api.SprinklerApi(api_client)
    id = 1 # int | A unique integer value identifying this force controller.

    # example passing only required values which don't have defaults set
    try:
        api_instance.sprinkler_controller_force_delete(id)
    except openapi_client.ApiException as e:
        print("Exception when calling SprinklerApi->sprinkler_controller_force_delete: %s\n" % e)
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

# **sprinkler_controller_force_list**
> SprinklerControllerForceList200Response sprinkler_controller_force_list()



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import sprinkler_api
from openapi_client.model.sprinkler_controller_force_list200_response import SprinklerControllerForceList200Response
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sprinkler_api.SprinklerApi(api_client)
    search = "search_example" # str | A search term. (optional)
    page = 1 # int | A page number within the paginated result set. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.sprinkler_controller_force_list(search=search, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SprinklerApi->sprinkler_controller_force_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional]
 **page** | **int**| A page number within the paginated result set. | [optional]

### Return type

[**SprinklerControllerForceList200Response**](SprinklerControllerForceList200Response.md)

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

# **sprinkler_controller_force_partial_update**
> SprinklerForceController sprinkler_controller_force_partial_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import sprinkler_api
from openapi_client.model.sprinkler_force_controller import SprinklerForceController
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sprinkler_api.SprinklerApi(api_client)
    id = 1 # int | A unique integer value identifying this force controller.
    data = SprinklerForceController(
        force_water_valve_signal=True,
        water_valve_signal=True,
        tag=1,
    ) # SprinklerForceController | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.sprinkler_controller_force_partial_update(id, data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SprinklerApi->sprinkler_controller_force_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this force controller. |
 **data** | [**SprinklerForceController**](SprinklerForceController.md)|  |

### Return type

[**SprinklerForceController**](SprinklerForceController.md)

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

# **sprinkler_controller_force_read**
> SprinklerForceController sprinkler_controller_force_read(id)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import sprinkler_api
from openapi_client.model.sprinkler_force_controller import SprinklerForceController
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sprinkler_api.SprinklerApi(api_client)
    id = 1 # int | A unique integer value identifying this force controller.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.sprinkler_controller_force_read(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SprinklerApi->sprinkler_controller_force_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this force controller. |

### Return type

[**SprinklerForceController**](SprinklerForceController.md)

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

# **sprinkler_controller_force_update**
> SprinklerForceController sprinkler_controller_force_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import sprinkler_api
from openapi_client.model.sprinkler_force_controller import SprinklerForceController
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sprinkler_api.SprinklerApi(api_client)
    id = 1 # int | A unique integer value identifying this force controller.
    data = SprinklerForceController(
        force_water_valve_signal=True,
        water_valve_signal=True,
        tag=1,
    ) # SprinklerForceController | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.sprinkler_controller_force_update(id, data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SprinklerApi->sprinkler_controller_force_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this force controller. |
 **data** | [**SprinklerForceController**](SprinklerForceController.md)|  |

### Return type

[**SprinklerForceController**](SprinklerForceController.md)

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

# **sprinkler_controller_list**
> SprinklerControllerList200Response sprinkler_controller_list()



Iot tag based controller live action to take only get because always updated by Iot Controller

### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import sprinkler_api
from openapi_client.model.sprinkler_controller_list200_response import SprinklerControllerList200Response
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sprinkler_api.SprinklerApi(api_client)
    search = "search_example" # str | A search term. (optional)
    page = 1 # int | A page number within the paginated result set. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.sprinkler_controller_list(search=search, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SprinklerApi->sprinkler_controller_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional]
 **page** | **int**| A page number within the paginated result set. | [optional]

### Return type

[**SprinklerControllerList200Response**](SprinklerControllerList200Response.md)

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

# **sprinkler_controller_read**
> SprinklerController sprinkler_controller_read(id)



Iot tag based controller live action to take only get because always updated by Iot Controller

### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import sprinkler_api
from openapi_client.model.sprinkler_controller import SprinklerController
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sprinkler_api.SprinklerApi(api_client)
    id = 1 # int | A unique integer value identifying this controller.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.sprinkler_controller_read(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SprinklerApi->sprinkler_controller_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this controller. |

### Return type

[**SprinklerController**](SprinklerController.md)

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

# **sprinkler_device_create**
> SprinklerDevice sprinkler_device_create(data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import sprinkler_api
from openapi_client.model.sprinkler_device import SprinklerDevice
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sprinkler_api.SprinklerApi(api_client)
    data = SprinklerDevice(
        tag="tag_example",
    ) # SprinklerDevice | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.sprinkler_device_create(data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SprinklerApi->sprinkler_device_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SprinklerDevice**](SprinklerDevice.md)|  |

### Return type

[**SprinklerDevice**](SprinklerDevice.md)

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

# **sprinkler_device_delete**
> sprinkler_device_delete(id)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import sprinkler_api
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sprinkler_api.SprinklerApi(api_client)
    id = 1 # int | A unique integer value identifying this device.

    # example passing only required values which don't have defaults set
    try:
        api_instance.sprinkler_device_delete(id)
    except openapi_client.ApiException as e:
        print("Exception when calling SprinklerApi->sprinkler_device_delete: %s\n" % e)
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

# **sprinkler_device_list**
> SprinklerDeviceList200Response sprinkler_device_list()



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import sprinkler_api
from openapi_client.model.sprinkler_device_list200_response import SprinklerDeviceList200Response
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sprinkler_api.SprinklerApi(api_client)
    search = "search_example" # str | A search term. (optional)
    page = 1 # int | A page number within the paginated result set. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.sprinkler_device_list(search=search, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SprinklerApi->sprinkler_device_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional]
 **page** | **int**| A page number within the paginated result set. | [optional]

### Return type

[**SprinklerDeviceList200Response**](SprinklerDeviceList200Response.md)

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

# **sprinkler_device_partial_update**
> SprinklerDevice sprinkler_device_partial_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import sprinkler_api
from openapi_client.model.sprinkler_device import SprinklerDevice
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sprinkler_api.SprinklerApi(api_client)
    id = 1 # int | A unique integer value identifying this device.
    data = SprinklerDevice(
        tag="tag_example",
    ) # SprinklerDevice | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.sprinkler_device_partial_update(id, data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SprinklerApi->sprinkler_device_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this device. |
 **data** | [**SprinklerDevice**](SprinklerDevice.md)|  |

### Return type

[**SprinklerDevice**](SprinklerDevice.md)

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

# **sprinkler_device_read**
> SprinklerDevice sprinkler_device_read(id)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import sprinkler_api
from openapi_client.model.sprinkler_device import SprinklerDevice
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sprinkler_api.SprinklerApi(api_client)
    id = 1 # int | A unique integer value identifying this device.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.sprinkler_device_read(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SprinklerApi->sprinkler_device_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this device. |

### Return type

[**SprinklerDevice**](SprinklerDevice.md)

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

# **sprinkler_device_update**
> SprinklerDevice sprinkler_device_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import sprinkler_api
from openapi_client.model.sprinkler_device import SprinklerDevice
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sprinkler_api.SprinklerApi(api_client)
    id = 1 # int | A unique integer value identifying this device.
    data = SprinklerDevice(
        tag="tag_example",
    ) # SprinklerDevice | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.sprinkler_device_update(id, data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SprinklerApi->sprinkler_device_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this device. |
 **data** | [**SprinklerDevice**](SprinklerDevice.md)|  |

### Return type

[**SprinklerDevice**](SprinklerDevice.md)

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

# **sprinkler_sensor_list**
> SprinklerSensorList200Response sprinkler_sensor_list()



IoT tag based sensors live values only get because always updated by IoT

### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import sprinkler_api
from openapi_client.model.sprinkler_sensor_list200_response import SprinklerSensorList200Response
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sprinkler_api.SprinklerApi(api_client)
    search = "search_example" # str | A search term. (optional)
    page = 1 # int | A page number within the paginated result set. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.sprinkler_sensor_list(search=search, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SprinklerApi->sprinkler_sensor_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional]
 **page** | **int**| A page number within the paginated result set. | [optional]

### Return type

[**SprinklerSensorList200Response**](SprinklerSensorList200Response.md)

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

# **sprinkler_sensor_read**
> SprinklerSensor sprinkler_sensor_read(id)



IoT tag based sensors live values only get because always updated by IoT

### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import sprinkler_api
from openapi_client.model.sprinkler_sensor import SprinklerSensor
from pprint import pprint
# Defining the host is optional and defaults to http://0.0.0.0:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://0.0.0.0:8001"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sprinkler_api.SprinklerApi(api_client)
    id = 1 # int | A unique integer value identifying this sensor.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.sprinkler_sensor_read(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SprinklerApi->sprinkler_sensor_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sensor. |

### Return type

[**SprinklerSensor**](SprinklerSensor.md)

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

