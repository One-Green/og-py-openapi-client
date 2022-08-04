# openapi_client.GlobalApi

All URIs are relative to *http://0.0.0.0:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**global_config_create**](GlobalApi.md#global_config_create) | **POST** /global/config/ | 
[**global_config_delete**](GlobalApi.md#global_config_delete) | **DELETE** /global/config/{id}/ | 
[**global_config_list**](GlobalApi.md#global_config_list) | **GET** /global/config/ | 
[**global_config_partial_update**](GlobalApi.md#global_config_partial_update) | **PATCH** /global/config/{id}/ | 
[**global_config_read**](GlobalApi.md#global_config_read) | **GET** /global/config/{id}/ | 
[**global_config_update**](GlobalApi.md#global_config_update) | **PUT** /global/config/{id}/ | 


# **global_config_create**
> GlobalConfig global_config_create(data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import global_api
from openapi_client.model.global_config import GlobalConfig
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
    api_instance = global_api.GlobalApi(api_client)
    data = GlobalConfig(
        site_tag="site_tag_example",
        address="address_example",
        timezone="timezone_example",
    ) # GlobalConfig | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.global_config_create(data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GlobalApi->global_config_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**GlobalConfig**](GlobalConfig.md)|  |

### Return type

[**GlobalConfig**](GlobalConfig.md)

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

# **global_config_delete**
> global_config_delete(id)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import global_api
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
    api_instance = global_api.GlobalApi(api_client)
    id = 1 # int | A unique integer value identifying this config.

    # example passing only required values which don't have defaults set
    try:
        api_instance.global_config_delete(id)
    except openapi_client.ApiException as e:
        print("Exception when calling GlobalApi->global_config_delete: %s\n" % e)
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

# **global_config_list**
> GlobalConfigList200Response global_config_list()



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import global_api
from openapi_client.model.global_config_list200_response import GlobalConfigList200Response
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
    api_instance = global_api.GlobalApi(api_client)
    search = "search_example" # str | A search term. (optional)
    page = 1 # int | A page number within the paginated result set. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.global_config_list(search=search, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GlobalApi->global_config_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional]
 **page** | **int**| A page number within the paginated result set. | [optional]

### Return type

[**GlobalConfigList200Response**](GlobalConfigList200Response.md)

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

# **global_config_partial_update**
> GlobalConfig global_config_partial_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import global_api
from openapi_client.model.global_config import GlobalConfig
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
    api_instance = global_api.GlobalApi(api_client)
    id = 1 # int | A unique integer value identifying this config.
    data = GlobalConfig(
        site_tag="site_tag_example",
        address="address_example",
        timezone="timezone_example",
    ) # GlobalConfig | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.global_config_partial_update(id, data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GlobalApi->global_config_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config. |
 **data** | [**GlobalConfig**](GlobalConfig.md)|  |

### Return type

[**GlobalConfig**](GlobalConfig.md)

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

# **global_config_read**
> GlobalConfig global_config_read(id)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import global_api
from openapi_client.model.global_config import GlobalConfig
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
    api_instance = global_api.GlobalApi(api_client)
    id = 1 # int | A unique integer value identifying this config.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.global_config_read(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GlobalApi->global_config_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config. |

### Return type

[**GlobalConfig**](GlobalConfig.md)

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

# **global_config_update**
> GlobalConfig global_config_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import global_api
from openapi_client.model.global_config import GlobalConfig
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
    api_instance = global_api.GlobalApi(api_client)
    id = 1 # int | A unique integer value identifying this config.
    data = GlobalConfig(
        site_tag="site_tag_example",
        address="address_example",
        timezone="timezone_example",
    ) # GlobalConfig | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.global_config_update(id, data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GlobalApi->global_config_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config. |
 **data** | [**GlobalConfig**](GlobalConfig.md)|  |

### Return type

[**GlobalConfig**](GlobalConfig.md)

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

