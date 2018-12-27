# coding: utf-8

"""
    JCDecaux API

    JCDecaux API for retrieving dynamic data about bike stations and contracts  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: alesanchezmedina@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ..api_client import ApiClient


class StationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def stations_get(self, **kwargs):  # noqa: E501
        """Gets the list of stations  # noqa: E501

        Allows the user to get the full list of JCDecaux stations. Also allows  the user to retrieve the stations list of a specific contract.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_=True
        >>> thread = api.stations_get(async_=True)
        >>> result = thread.get()

        :param async_ bool
        :param str contract: Name of the contract from which retrieve the list of stations
        :return: list[Station]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_'):
            return self.stations_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.stations_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def stations_get_with_http_info(self, **kwargs):  # noqa: E501
        """Gets the list of stations  # noqa: E501

        Allows the user to get the full list of JCDecaux stations. Also allows  the user to retrieve the stations list of a specific contract.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_=True
        >>> thread = api.stations_get_with_http_info(async_=True)
        >>> result = thread.get()

        :param async_ bool
        :param str contract: Name of the contract from which retrieve the list of stations
        :return: list[Station]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['contract']  # noqa: E501
        all_params.append('async_')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stations_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'contract' in params:
            query_params.append(('contract', params['contract']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Station]',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async_'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stations_station_number_get(self, station_number, contract, **kwargs):  # noqa: E501
        """Gets a specific station  # noqa: E501

        Allows the user to retrieve static and dynamic data from a specific station whithin a contract   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_=True
        >>> thread = api.stations_station_number_get(station_number, contract, async_=True)
        >>> result = thread.get()

        :param async_ bool
        :param str station_number: The station number you want to retrieve (required)
        :param str contract: The contract to which the station belongs (required)
        :return: list[Station]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_'):
            return self.stations_station_number_get_with_http_info(station_number, contract, **kwargs)  # noqa: E501
        else:
            (data) = self.stations_station_number_get_with_http_info(station_number, contract, **kwargs)  # noqa: E501
            return data

    def stations_station_number_get_with_http_info(self, station_number, contract, **kwargs):  # noqa: E501
        """Gets a specific station  # noqa: E501

        Allows the user to retrieve static and dynamic data from a specific station whithin a contract   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_=True
        >>> thread = api.stations_station_number_get_with_http_info(station_number, contract, async_=True)
        >>> result = thread.get()

        :param async_ bool
        :param str station_number: The station number you want to retrieve (required)
        :param str contract: The contract to which the station belongs (required)
        :return: list[Station]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['station_number', 'contract']  # noqa: E501
        all_params.append('async_')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stations_station_number_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'station_number' is set
        if ('station_number' not in params or
                params['station_number'] is None):
            raise ValueError("Missing the required parameter `station_number` when calling `stations_station_number_get`")  # noqa: E501
        # verify the required parameter 'contract' is set
        if ('contract' not in params or
                params['contract'] is None):
            raise ValueError("Missing the required parameter `contract` when calling `stations_station_number_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'station_number' in params:
            path_params['station_number'] = params['station_number']  # noqa: E501

        query_params = []
        if 'contract' in params:
            query_params.append(('contract', params['contract']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stations/{station_number}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Station',  # noqa: E501
            auth_settings=auth_settings,
            async_=params.get('async_'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
