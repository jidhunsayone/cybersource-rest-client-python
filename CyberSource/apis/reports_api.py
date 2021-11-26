# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient
import CyberSource.logging.log_factory as LogFactory


class ReportsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """
	
    def __init__(self, merchant_config, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client
        self.api_client.set_configuration(merchant_config)
        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.api_client.mconfig.log_config)



    def create_report(self, create_adhoc_report_request, **kwargs):
        """
        Create Adhoc Report
        Create a one-time report. You must specify the type of report in reportDefinitionName. For a list of values for reportDefinitionName, see the [Reporting Developer Guide](https://www.cybersource.com/developers/documentation/reporting_and_reconciliation) 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_report(create_adhoc_report_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateAdhocReportRequest create_adhoc_report_request: Report subscription request payload (required)
        :param str organization_id: Valid Organization Id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `create_report` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_report_with_http_info(create_adhoc_report_request, **kwargs)
        else:
            (data) = self.create_report_with_http_info(create_adhoc_report_request, **kwargs)
            return data

    def create_report_with_http_info(self, create_adhoc_report_request, **kwargs):
        """
        Create Adhoc Report
        Create a one-time report. You must specify the type of report in reportDefinitionName. For a list of values for reportDefinitionName, see the [Reporting Developer Guide](https://www.cybersource.com/developers/documentation/reporting_and_reconciliation) 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_report_with_http_info(create_adhoc_report_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateAdhocReportRequest create_adhoc_report_request: Report subscription request payload (required)
        :param str organization_id: Valid Organization Id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_adhoc_report_request', 'organization_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_report" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_adhoc_report_request' is set
        if ('create_adhoc_report_request' not in params) or (params['create_adhoc_report_request'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `create_adhoc_report_request` when calling `create_report`")
            raise ValueError("Missing the required parameter `create_adhoc_report_request` when calling `create_report`")

        if 'organization_id' in params and len(params['organization_id']) > 32:
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `organization_id` when calling `create_report`, length must be less than or equal to `32`")
            raise ValueError("Invalid value for parameter `organization_id` when calling `create_report`, length must be less than or equal to `32`")
        if 'organization_id' in params and len(params['organization_id']) < 1:
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `organization_id` when calling `create_report`, length must be greater than or equal to `1`")
            raise ValueError("Invalid value for parameter `organization_id` when calling `create_report`, length must be greater than or equal to `1`")
        if 'organization_id' in params and not re.search('[a-zA-Z0-9-_]+', params['organization_id']):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `organization_id` when calling `create_report`, must conform to the pattern `/[a-zA-Z0-9-_]+/`")
            raise ValueError("Invalid value for parameter `organization_id` when calling `create_report`, must conform to the pattern `/[a-zA-Z0-9-_]+/`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'organization_id' in params:
            query_params.append(('organizationId', params['organization_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_adhoc_report_request' in params:
            body_params = params['create_adhoc_report_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/hal+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/reporting/v3/reports', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_report_by_report_id(self, report_id, **kwargs):
        """
        Get Report Based on Report Id
        Download a report using the reportId value. If you don’t already know this value, you can obtain it using the Retrieve available reports call. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_report_by_report_id(report_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str report_id: Valid Report Id (required)
        :param str organization_id: Valid Organization Id
        :return: ReportingV3ReportsIdGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `get_report_by_report_id` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_report_by_report_id_with_http_info(report_id, **kwargs)
        else:
            (data) = self.get_report_by_report_id_with_http_info(report_id, **kwargs)
            return data

    def get_report_by_report_id_with_http_info(self, report_id, **kwargs):
        """
        Get Report Based on Report Id
        Download a report using the reportId value. If you don’t already know this value, you can obtain it using the Retrieve available reports call. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_report_by_report_id_with_http_info(report_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str report_id: Valid Report Id (required)
        :param str organization_id: Valid Organization Id
        :return: ReportingV3ReportsIdGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['report_id', 'organization_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_report_by_report_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'report_id' is set
        if ('report_id' not in params) or (params['report_id'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `report_id` when calling `get_report_by_report_id`")
            raise ValueError("Missing the required parameter `report_id` when calling `get_report_by_report_id`")

        if 'organization_id' in params and len(params['organization_id']) > 32:
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `organization_id` when calling `get_report_by_report_id`, length must be less than or equal to `32`")
            raise ValueError("Invalid value for parameter `organization_id` when calling `get_report_by_report_id`, length must be less than or equal to `32`")
        if 'organization_id' in params and len(params['organization_id']) < 1:
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `organization_id` when calling `get_report_by_report_id`, length must be greater than or equal to `1`")
            raise ValueError("Invalid value for parameter `organization_id` when calling `get_report_by_report_id`, length must be greater than or equal to `1`")
        if 'organization_id' in params and not re.search('[a-zA-Z0-9-_]+', params['organization_id']):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `organization_id` when calling `get_report_by_report_id`, must conform to the pattern `/[a-zA-Z0-9-_]+/`")
            raise ValueError("Invalid value for parameter `organization_id` when calling `get_report_by_report_id`, must conform to the pattern `/[a-zA-Z0-9-_]+/`")

        collection_formats = {}

        path_params = {}
        if 'report_id' in params:
            path_params['reportId'] = params['report_id']

        query_params = []
        if 'organization_id' in params:
            query_params.append(('organizationId', params['organization_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/hal+json', 'application/xml'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/reporting/v3/reports/{}'.format(report_id), 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ReportingV3ReportsIdGet200Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def search_reports(self, start_time, end_time, time_query_type, **kwargs):
        """
        Retrieve Available Reports
        Retrieve a list of the available reports to which you are subscribed. This will also give you the reportId value, which you can also use to download a report. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.search_reports(start_time, end_time, time_query_type, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param datetime start_time: Valid report Start Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd'T'HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z)  (required)
        :param datetime end_time: Valid report End Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd'T'HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z)  (required)
        :param str time_query_type: Specify time you would like to search  Valid values: - reportTimeFrame - executedTime  (required)
        :param str organization_id: Valid Organization Id
        :param str report_mime_type: Valid Report Format  Valid values: - application/xml - text/csv 
        :param str report_frequency: Valid Report Frequency  Valid values: - DAILY - WEEKLY - MONTHLY - USER_DEFINED - ADHOC 
        :param str report_name: Valid Report Name
        :param int report_definition_id: Valid Report Definition Id
        :param str report_status: Valid Report Status  Valid values: - COMPLETED - PENDING - QUEUED - RUNNING - ERROR - NO_DATA 
        :return: ReportingV3ReportsGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `search_reports` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.search_reports_with_http_info(start_time, end_time, time_query_type, **kwargs)
        else:
            (data) = self.search_reports_with_http_info(start_time, end_time, time_query_type, **kwargs)
            return data

    def search_reports_with_http_info(self, start_time, end_time, time_query_type, **kwargs):
        """
        Retrieve Available Reports
        Retrieve a list of the available reports to which you are subscribed. This will also give you the reportId value, which you can also use to download a report. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.search_reports_with_http_info(start_time, end_time, time_query_type, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param datetime start_time: Valid report Start Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd'T'HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z)  (required)
        :param datetime end_time: Valid report End Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**   - yyyy-MM-dd'T'HH:mm:ss.SSSZ (e.g. 2018-01-01T00:00:00.000Z)  (required)
        :param str time_query_type: Specify time you would like to search  Valid values: - reportTimeFrame - executedTime  (required)
        :param str organization_id: Valid Organization Id
        :param str report_mime_type: Valid Report Format  Valid values: - application/xml - text/csv 
        :param str report_frequency: Valid Report Frequency  Valid values: - DAILY - WEEKLY - MONTHLY - USER_DEFINED - ADHOC 
        :param str report_name: Valid Report Name
        :param int report_definition_id: Valid Report Definition Id
        :param str report_status: Valid Report Status  Valid values: - COMPLETED - PENDING - QUEUED - RUNNING - ERROR - NO_DATA 
        :return: ReportingV3ReportsGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_time', 'end_time', 'time_query_type', 'organization_id', 'report_mime_type', 'report_frequency', 'report_name', 'report_definition_id', 'report_status']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_reports" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'start_time' is set
        if ('start_time' not in params) or (params['start_time'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `start_time` when calling `search_reports`")
            raise ValueError("Missing the required parameter `start_time` when calling `search_reports`")
        # verify the required parameter 'end_time' is set
        if ('end_time' not in params) or (params['end_time'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `end_time` when calling `search_reports`")
            raise ValueError("Missing the required parameter `end_time` when calling `search_reports`")
        # verify the required parameter 'time_query_type' is set
        if ('time_query_type' not in params) or (params['time_query_type'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `time_query_type` when calling `search_reports`")
            raise ValueError("Missing the required parameter `time_query_type` when calling `search_reports`")

        if 'organization_id' in params and len(params['organization_id']) > 32:
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `organization_id` when calling `search_reports`, length must be less than or equal to `32`")
            raise ValueError("Invalid value for parameter `organization_id` when calling `search_reports`, length must be less than or equal to `32`")
        if 'organization_id' in params and len(params['organization_id']) < 1:
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `organization_id` when calling `search_reports`, length must be greater than or equal to `1`")
            raise ValueError("Invalid value for parameter `organization_id` when calling `search_reports`, length must be greater than or equal to `1`")
        if 'organization_id' in params and not re.search('[a-zA-Z0-9-_]+', params['organization_id']):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `organization_id` when calling `search_reports`, must conform to the pattern `/[a-zA-Z0-9-_]+/`")
            raise ValueError("Invalid value for parameter `organization_id` when calling `search_reports`, must conform to the pattern `/[a-zA-Z0-9-_]+/`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'organization_id' in params:
            query_params.append(('organizationId', params['organization_id']))
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))
        if 'time_query_type' in params:
            query_params.append(('timeQueryType', params['time_query_type']))
        if 'report_mime_type' in params:
            query_params.append(('reportMimeType', params['report_mime_type']))
        if 'report_frequency' in params:
            query_params.append(('reportFrequency', params['report_frequency']))
        if 'report_name' in params:
            query_params.append(('reportName', params['report_name']))
        if 'report_definition_id' in params:
            query_params.append(('reportDefinitionId', params['report_definition_id']))
        if 'report_status' in params:
            query_params.append(('reportStatus', params['report_status']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/hal+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/reporting/v3/reports', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ReportingV3ReportsGet200Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
