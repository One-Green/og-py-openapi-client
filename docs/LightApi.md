# openapi_client.LightApi

All URIs are relative to *http://0.0.0.0:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**light_config_calendar_create**](LightApi.md#light_config_calendar_create) | **POST** /light/config-calendar/ | 
[**light_config_calendar_delete**](LightApi.md#light_config_calendar_delete) | **DELETE** /light/config-calendar/{id}/ | 
[**light_config_calendar_list**](LightApi.md#light_config_calendar_list) | **GET** /light/config-calendar/ | 
[**light_config_calendar_partial_update**](LightApi.md#light_config_calendar_partial_update) | **PATCH** /light/config-calendar/{id}/ | 
[**light_config_calendar_read**](LightApi.md#light_config_calendar_read) | **GET** /light/config-calendar/{id}/ | 
[**light_config_calendar_update**](LightApi.md#light_config_calendar_update) | **PUT** /light/config-calendar/{id}/ | 
[**light_config_create**](LightApi.md#light_config_create) | **POST** /light/config/ | 
[**light_config_daily_create**](LightApi.md#light_config_daily_create) | **POST** /light/config-daily/ | 
[**light_config_daily_delete**](LightApi.md#light_config_daily_delete) | **DELETE** /light/config-daily/{id}/ | 
[**light_config_daily_list**](LightApi.md#light_config_daily_list) | **GET** /light/config-daily/ | 
[**light_config_daily_partial_update**](LightApi.md#light_config_daily_partial_update) | **PATCH** /light/config-daily/{id}/ | 
[**light_config_daily_read**](LightApi.md#light_config_daily_read) | **GET** /light/config-daily/{id}/ | 
[**light_config_daily_update**](LightApi.md#light_config_daily_update) | **PUT** /light/config-daily/{id}/ | 
[**light_config_delete**](LightApi.md#light_config_delete) | **DELETE** /light/config/{id}/ | 
[**light_config_list**](LightApi.md#light_config_list) | **GET** /light/config/ | 
[**light_config_partial_update**](LightApi.md#light_config_partial_update) | **PATCH** /light/config/{id}/ | 
[**light_config_read**](LightApi.md#light_config_read) | **GET** /light/config/{id}/ | 
[**light_config_type_create**](LightApi.md#light_config_type_create) | **POST** /light/config-type/ | 
[**light_config_type_delete**](LightApi.md#light_config_type_delete) | **DELETE** /light/config-type/{id}/ | 
[**light_config_type_list**](LightApi.md#light_config_type_list) | **GET** /light/config-type/ | 
[**light_config_type_partial_update**](LightApi.md#light_config_type_partial_update) | **PATCH** /light/config-type/{id}/ | 
[**light_config_type_read**](LightApi.md#light_config_type_read) | **GET** /light/config-type/{id}/ | 
[**light_config_type_update**](LightApi.md#light_config_type_update) | **PUT** /light/config-type/{id}/ | 
[**light_config_update**](LightApi.md#light_config_update) | **PUT** /light/config/{id}/ | 
[**light_controller_force_create**](LightApi.md#light_controller_force_create) | **POST** /light/controller-force/ | 
[**light_controller_force_delete**](LightApi.md#light_controller_force_delete) | **DELETE** /light/controller-force/{id}/ | 
[**light_controller_force_list**](LightApi.md#light_controller_force_list) | **GET** /light/controller-force/ | 
[**light_controller_force_partial_update**](LightApi.md#light_controller_force_partial_update) | **PATCH** /light/controller-force/{id}/ | 
[**light_controller_force_read**](LightApi.md#light_controller_force_read) | **GET** /light/controller-force/{id}/ | 
[**light_controller_force_update**](LightApi.md#light_controller_force_update) | **PUT** /light/controller-force/{id}/ | 
[**light_controller_list**](LightApi.md#light_controller_list) | **GET** /light/controller/ | 
[**light_controller_read**](LightApi.md#light_controller_read) | **GET** /light/controller/{id}/ | 
[**light_device_create**](LightApi.md#light_device_create) | **POST** /light/device/ | 
[**light_device_delete**](LightApi.md#light_device_delete) | **DELETE** /light/device/{id}/ | 
[**light_device_list**](LightApi.md#light_device_list) | **GET** /light/device/ | 
[**light_device_partial_update**](LightApi.md#light_device_partial_update) | **PATCH** /light/device/{id}/ | 
[**light_device_read**](LightApi.md#light_device_read) | **GET** /light/device/{id}/ | 
[**light_device_update**](LightApi.md#light_device_update) | **PUT** /light/device/{id}/ | 
[**light_sensor_list**](LightApi.md#light_sensor_list) | **GET** /light/sensor/ | 
[**light_sensor_read**](LightApi.md#light_sensor_read) | **GET** /light/sensor/{id}/ | 


# **light_config_calendar_create**
> LightConfigurationCalendarRange light_config_calendar_create(data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_configuration_calendar_range import LightConfigurationCalendarRange
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
    api_instance = light_api.LightApi(api_client)
    data = LightConfigurationCalendarRange(
        name="name_example",
        start_date_at=dateutil_parser('1970-01-01').date(),
        end_date_at=dateutil_parser('1970-01-01').date(),
        on_time_at="on_time_at_example",
        off_time_at="off_time_at_example",
    ) # LightConfigurationCalendarRange | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_config_calendar_create(data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_calendar_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**LightConfigurationCalendarRange**](LightConfigurationCalendarRange.md)|  |

### Return type

[**LightConfigurationCalendarRange**](LightConfigurationCalendarRange.md)

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

# **light_config_calendar_delete**
> light_config_calendar_delete(id)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this calendar range.

    # example passing only required values which don't have defaults set
    try:
        api_instance.light_config_calendar_delete(id)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_calendar_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this calendar range. |

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

# **light_config_calendar_list**
> LightConfigCalendarList200Response light_config_calendar_list()



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_config_calendar_list200_response import LightConfigCalendarList200Response
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
    api_instance = light_api.LightApi(api_client)
    search = "search_example" # str | A search term. (optional)
    page = 1 # int | A page number within the paginated result set. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.light_config_calendar_list(search=search, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_calendar_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional]
 **page** | **int**| A page number within the paginated result set. | [optional]

### Return type

[**LightConfigCalendarList200Response**](LightConfigCalendarList200Response.md)

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

# **light_config_calendar_partial_update**
> LightConfigurationCalendarRange light_config_calendar_partial_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_configuration_calendar_range import LightConfigurationCalendarRange
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this calendar range.
    data = LightConfigurationCalendarRange(
        name="name_example",
        start_date_at=dateutil_parser('1970-01-01').date(),
        end_date_at=dateutil_parser('1970-01-01').date(),
        on_time_at="on_time_at_example",
        off_time_at="off_time_at_example",
    ) # LightConfigurationCalendarRange | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_config_calendar_partial_update(id, data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_calendar_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this calendar range. |
 **data** | [**LightConfigurationCalendarRange**](LightConfigurationCalendarRange.md)|  |

### Return type

[**LightConfigurationCalendarRange**](LightConfigurationCalendarRange.md)

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

# **light_config_calendar_read**
> LightConfigurationCalendarRange light_config_calendar_read(id)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_configuration_calendar_range import LightConfigurationCalendarRange
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this calendar range.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_config_calendar_read(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_calendar_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this calendar range. |

### Return type

[**LightConfigurationCalendarRange**](LightConfigurationCalendarRange.md)

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

# **light_config_calendar_update**
> LightConfigurationCalendarRange light_config_calendar_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_configuration_calendar_range import LightConfigurationCalendarRange
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this calendar range.
    data = LightConfigurationCalendarRange(
        name="name_example",
        start_date_at=dateutil_parser('1970-01-01').date(),
        end_date_at=dateutil_parser('1970-01-01').date(),
        on_time_at="on_time_at_example",
        off_time_at="off_time_at_example",
    ) # LightConfigurationCalendarRange | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_config_calendar_update(id, data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_calendar_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this calendar range. |
 **data** | [**LightConfigurationCalendarRange**](LightConfigurationCalendarRange.md)|  |

### Return type

[**LightConfigurationCalendarRange**](LightConfigurationCalendarRange.md)

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

# **light_config_create**
> LightConfiguration light_config_create(data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_configuration import LightConfiguration
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
    api_instance = light_api.LightApi(api_client)
    data = LightConfiguration(
        tag=1,
        config_type=1,
        daily_config=1,
        planner_configs=[
            1,
        ],
    ) # LightConfiguration | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_config_create(data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**LightConfiguration**](LightConfiguration.md)|  |

### Return type

[**LightConfiguration**](LightConfiguration.md)

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

# **light_config_daily_create**
> LightConfigurationDailyTimeRange light_config_daily_create(data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_configuration_daily_time_range import LightConfigurationDailyTimeRange
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
    api_instance = light_api.LightApi(api_client)
    data = LightConfigurationDailyTimeRange(
        name="name_example",
        on_at="on_at_example",
        off_at="off_at_example",
        on_monday=True,
        on_tuesday=True,
        on_wednesday=True,
        on_thursday=True,
        on_friday=True,
        on_saturday=True,
        on_sunday=True,
    ) # LightConfigurationDailyTimeRange | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_config_daily_create(data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_daily_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**LightConfigurationDailyTimeRange**](LightConfigurationDailyTimeRange.md)|  |

### Return type

[**LightConfigurationDailyTimeRange**](LightConfigurationDailyTimeRange.md)

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

# **light_config_daily_delete**
> light_config_daily_delete(id)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this daily time range.

    # example passing only required values which don't have defaults set
    try:
        api_instance.light_config_daily_delete(id)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_daily_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this daily time range. |

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

# **light_config_daily_list**
> LightConfigDailyList200Response light_config_daily_list()



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_config_daily_list200_response import LightConfigDailyList200Response
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
    api_instance = light_api.LightApi(api_client)
    search = "search_example" # str | A search term. (optional)
    page = 1 # int | A page number within the paginated result set. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.light_config_daily_list(search=search, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_daily_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional]
 **page** | **int**| A page number within the paginated result set. | [optional]

### Return type

[**LightConfigDailyList200Response**](LightConfigDailyList200Response.md)

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

# **light_config_daily_partial_update**
> LightConfigurationDailyTimeRange light_config_daily_partial_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_configuration_daily_time_range import LightConfigurationDailyTimeRange
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this daily time range.
    data = LightConfigurationDailyTimeRange(
        name="name_example",
        on_at="on_at_example",
        off_at="off_at_example",
        on_monday=True,
        on_tuesday=True,
        on_wednesday=True,
        on_thursday=True,
        on_friday=True,
        on_saturday=True,
        on_sunday=True,
    ) # LightConfigurationDailyTimeRange | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_config_daily_partial_update(id, data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_daily_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this daily time range. |
 **data** | [**LightConfigurationDailyTimeRange**](LightConfigurationDailyTimeRange.md)|  |

### Return type

[**LightConfigurationDailyTimeRange**](LightConfigurationDailyTimeRange.md)

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

# **light_config_daily_read**
> LightConfigurationDailyTimeRange light_config_daily_read(id)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_configuration_daily_time_range import LightConfigurationDailyTimeRange
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this daily time range.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_config_daily_read(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_daily_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this daily time range. |

### Return type

[**LightConfigurationDailyTimeRange**](LightConfigurationDailyTimeRange.md)

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

# **light_config_daily_update**
> LightConfigurationDailyTimeRange light_config_daily_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_configuration_daily_time_range import LightConfigurationDailyTimeRange
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this daily time range.
    data = LightConfigurationDailyTimeRange(
        name="name_example",
        on_at="on_at_example",
        off_at="off_at_example",
        on_monday=True,
        on_tuesday=True,
        on_wednesday=True,
        on_thursday=True,
        on_friday=True,
        on_saturday=True,
        on_sunday=True,
    ) # LightConfigurationDailyTimeRange | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_config_daily_update(id, data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_daily_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this daily time range. |
 **data** | [**LightConfigurationDailyTimeRange**](LightConfigurationDailyTimeRange.md)|  |

### Return type

[**LightConfigurationDailyTimeRange**](LightConfigurationDailyTimeRange.md)

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

# **light_config_delete**
> light_config_delete(id)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this config.

    # example passing only required values which don't have defaults set
    try:
        api_instance.light_config_delete(id)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_delete: %s\n" % e)
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

# **light_config_list**
> LightConfigList200Response light_config_list()



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_config_list200_response import LightConfigList200Response
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
    api_instance = light_api.LightApi(api_client)
    search = "search_example" # str | A search term. (optional)
    page = 1 # int | A page number within the paginated result set. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.light_config_list(search=search, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional]
 **page** | **int**| A page number within the paginated result set. | [optional]

### Return type

[**LightConfigList200Response**](LightConfigList200Response.md)

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

# **light_config_partial_update**
> LightConfiguration light_config_partial_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_configuration import LightConfiguration
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this config.
    data = LightConfiguration(
        tag=1,
        config_type=1,
        daily_config=1,
        planner_configs=[
            1,
        ],
    ) # LightConfiguration | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_config_partial_update(id, data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config. |
 **data** | [**LightConfiguration**](LightConfiguration.md)|  |

### Return type

[**LightConfiguration**](LightConfiguration.md)

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

# **light_config_read**
> LightConfiguration light_config_read(id)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_configuration import LightConfiguration
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this config.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_config_read(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config. |

### Return type

[**LightConfiguration**](LightConfiguration.md)

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

# **light_config_type_create**
> LightConfigurationType light_config_type_create(data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_configuration_type import LightConfigurationType
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
    api_instance = light_api.LightApi(api_client)
    data = LightConfigurationType(
        name="name_example",
    ) # LightConfigurationType | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_config_type_create(data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_type_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**LightConfigurationType**](LightConfigurationType.md)|  |

### Return type

[**LightConfigurationType**](LightConfigurationType.md)

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

# **light_config_type_delete**
> light_config_type_delete(id)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this config type.

    # example passing only required values which don't have defaults set
    try:
        api_instance.light_config_type_delete(id)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_type_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config type. |

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

# **light_config_type_list**
> LightConfigTypeList200Response light_config_type_list()



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_config_type_list200_response import LightConfigTypeList200Response
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
    api_instance = light_api.LightApi(api_client)
    search = "search_example" # str | A search term. (optional)
    page = 1 # int | A page number within the paginated result set. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.light_config_type_list(search=search, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_type_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional]
 **page** | **int**| A page number within the paginated result set. | [optional]

### Return type

[**LightConfigTypeList200Response**](LightConfigTypeList200Response.md)

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

# **light_config_type_partial_update**
> LightConfigurationType light_config_type_partial_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_configuration_type import LightConfigurationType
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this config type.
    data = LightConfigurationType(
        name="name_example",
    ) # LightConfigurationType | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_config_type_partial_update(id, data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_type_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config type. |
 **data** | [**LightConfigurationType**](LightConfigurationType.md)|  |

### Return type

[**LightConfigurationType**](LightConfigurationType.md)

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

# **light_config_type_read**
> LightConfigurationType light_config_type_read(id)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_configuration_type import LightConfigurationType
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this config type.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_config_type_read(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_type_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config type. |

### Return type

[**LightConfigurationType**](LightConfigurationType.md)

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

# **light_config_type_update**
> LightConfigurationType light_config_type_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_configuration_type import LightConfigurationType
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this config type.
    data = LightConfigurationType(
        name="name_example",
    ) # LightConfigurationType | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_config_type_update(id, data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_type_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config type. |
 **data** | [**LightConfigurationType**](LightConfigurationType.md)|  |

### Return type

[**LightConfigurationType**](LightConfigurationType.md)

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

# **light_config_update**
> LightConfiguration light_config_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_configuration import LightConfiguration
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this config.
    data = LightConfiguration(
        tag=1,
        config_type=1,
        daily_config=1,
        planner_configs=[
            1,
        ],
    ) # LightConfiguration | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_config_update(id, data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_config_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config. |
 **data** | [**LightConfiguration**](LightConfiguration.md)|  |

### Return type

[**LightConfiguration**](LightConfiguration.md)

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

# **light_controller_force_create**
> LightForceController light_controller_force_create(data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_force_controller import LightForceController
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
    api_instance = light_api.LightApi(api_client)
    data = LightForceController(
        force_light_signal=True,
        light_signal=True,
        tag=1,
    ) # LightForceController | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_controller_force_create(data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_controller_force_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**LightForceController**](LightForceController.md)|  |

### Return type

[**LightForceController**](LightForceController.md)

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

# **light_controller_force_delete**
> light_controller_force_delete(id)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this force controller.

    # example passing only required values which don't have defaults set
    try:
        api_instance.light_controller_force_delete(id)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_controller_force_delete: %s\n" % e)
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

# **light_controller_force_list**
> LightControllerForceList200Response light_controller_force_list()



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_controller_force_list200_response import LightControllerForceList200Response
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
    api_instance = light_api.LightApi(api_client)
    search = "search_example" # str | A search term. (optional)
    page = 1 # int | A page number within the paginated result set. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.light_controller_force_list(search=search, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_controller_force_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional]
 **page** | **int**| A page number within the paginated result set. | [optional]

### Return type

[**LightControllerForceList200Response**](LightControllerForceList200Response.md)

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

# **light_controller_force_partial_update**
> LightForceController light_controller_force_partial_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_force_controller import LightForceController
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this force controller.
    data = LightForceController(
        force_light_signal=True,
        light_signal=True,
        tag=1,
    ) # LightForceController | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_controller_force_partial_update(id, data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_controller_force_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this force controller. |
 **data** | [**LightForceController**](LightForceController.md)|  |

### Return type

[**LightForceController**](LightForceController.md)

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

# **light_controller_force_read**
> LightForceController light_controller_force_read(id)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_force_controller import LightForceController
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this force controller.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_controller_force_read(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_controller_force_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this force controller. |

### Return type

[**LightForceController**](LightForceController.md)

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

# **light_controller_force_update**
> LightForceController light_controller_force_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_force_controller import LightForceController
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this force controller.
    data = LightForceController(
        force_light_signal=True,
        light_signal=True,
        tag=1,
    ) # LightForceController | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_controller_force_update(id, data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_controller_force_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this force controller. |
 **data** | [**LightForceController**](LightForceController.md)|  |

### Return type

[**LightForceController**](LightForceController.md)

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

# **light_controller_list**
> LightControllerList200Response light_controller_list()



Iot tag based controller live action to take only get because always updated by Iot Controller

### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_controller_list200_response import LightControllerList200Response
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
    api_instance = light_api.LightApi(api_client)
    search = "search_example" # str | A search term. (optional)
    page = 1 # int | A page number within the paginated result set. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.light_controller_list(search=search, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_controller_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional]
 **page** | **int**| A page number within the paginated result set. | [optional]

### Return type

[**LightControllerList200Response**](LightControllerList200Response.md)

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

# **light_controller_read**
> LightController light_controller_read(id)



Iot tag based controller live action to take only get because always updated by Iot Controller

### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_controller import LightController
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this controller.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_controller_read(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_controller_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this controller. |

### Return type

[**LightController**](LightController.md)

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

# **light_device_create**
> LightDevice light_device_create(data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_device import LightDevice
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
    api_instance = light_api.LightApi(api_client)
    data = LightDevice(
        tag="tag_example",
    ) # LightDevice | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_device_create(data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_device_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**LightDevice**](LightDevice.md)|  |

### Return type

[**LightDevice**](LightDevice.md)

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

# **light_device_delete**
> light_device_delete(id)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this device.

    # example passing only required values which don't have defaults set
    try:
        api_instance.light_device_delete(id)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_device_delete: %s\n" % e)
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

# **light_device_list**
> LightDeviceList200Response light_device_list()



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_device_list200_response import LightDeviceList200Response
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
    api_instance = light_api.LightApi(api_client)
    search = "search_example" # str | A search term. (optional)
    page = 1 # int | A page number within the paginated result set. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.light_device_list(search=search, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_device_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional]
 **page** | **int**| A page number within the paginated result set. | [optional]

### Return type

[**LightDeviceList200Response**](LightDeviceList200Response.md)

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

# **light_device_partial_update**
> LightDevice light_device_partial_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_device import LightDevice
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this device.
    data = LightDevice(
        tag="tag_example",
    ) # LightDevice | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_device_partial_update(id, data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_device_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this device. |
 **data** | [**LightDevice**](LightDevice.md)|  |

### Return type

[**LightDevice**](LightDevice.md)

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

# **light_device_read**
> LightDevice light_device_read(id)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_device import LightDevice
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this device.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_device_read(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_device_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this device. |

### Return type

[**LightDevice**](LightDevice.md)

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

# **light_device_update**
> LightDevice light_device_update(id, data)



### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_device import LightDevice
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this device.
    data = LightDevice(
        tag="tag_example",
    ) # LightDevice | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_device_update(id, data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_device_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this device. |
 **data** | [**LightDevice**](LightDevice.md)|  |

### Return type

[**LightDevice**](LightDevice.md)

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

# **light_sensor_list**
> LightSensorList200Response light_sensor_list()



IoT tag based sensors live values only get because always updated by IoT

### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_sensor_list200_response import LightSensorList200Response
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
    api_instance = light_api.LightApi(api_client)
    search = "search_example" # str | A search term. (optional)
    page = 1 # int | A page number within the paginated result set. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.light_sensor_list(search=search, page=page)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_sensor_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| A search term. | [optional]
 **page** | **int**| A page number within the paginated result set. | [optional]

### Return type

[**LightSensorList200Response**](LightSensorList200Response.md)

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

# **light_sensor_read**
> LightSensor light_sensor_read(id)



IoT tag based sensors live values only get because always updated by IoT

### Example

* Basic Authentication (Basic):

```python
import time
import openapi_client
from openapi_client.api import light_api
from openapi_client.model.light_sensor import LightSensor
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
    api_instance = light_api.LightApi(api_client)
    id = 1 # int | A unique integer value identifying this sensor.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.light_sensor_read(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LightApi->light_sensor_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sensor. |

### Return type

[**LightSensor**](LightSensor.md)

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

