# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VasV2TaxVoid200Response(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'submit_time_utc': 'str',
        'status': 'str',
        'client_reference_information': 'PtsV2IncrementalAuthorizationPatch201ResponseClientReferenceInformation',
        'void_amount_details': 'VasV2TaxVoid200ResponseVoidAmountDetails'
    }

    attribute_map = {
        'id': 'id',
        'submit_time_utc': 'submitTimeUtc',
        'status': 'status',
        'client_reference_information': 'clientReferenceInformation',
        'void_amount_details': 'voidAmountDetails'
    }

    def __init__(self, id=None, submit_time_utc=None, status=None, client_reference_information=None, void_amount_details=None):
        """
        VasV2TaxVoid200Response - a model defined in Swagger
        """

        self._id = None
        self._submit_time_utc = None
        self._status = None
        self._client_reference_information = None
        self._void_amount_details = None

        if id is not None:
          self.id = id
        if submit_time_utc is not None:
          self.submit_time_utc = submit_time_utc
        if status is not None:
          self.status = status
        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if void_amount_details is not None:
          self.void_amount_details = void_amount_details

    @property
    def id(self):
        """
        Gets the id of this VasV2TaxVoid200Response.
        An unique identification number generated by Cybersource to identify the submitted request. Returned by all services. It is also appended to the endpoint of the resource. On incremental authorizations, this value with be the same as the identification number returned in the original authorization response. 

        :return: The id of this VasV2TaxVoid200Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VasV2TaxVoid200Response.
        An unique identification number generated by Cybersource to identify the submitted request. Returned by all services. It is also appended to the endpoint of the resource. On incremental authorizations, this value with be the same as the identification number returned in the original authorization response. 

        :param id: The id of this VasV2TaxVoid200Response.
        :type: str
        """

        self._id = id

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this VasV2TaxVoid200Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` **Example** `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC.  Returned by Cybersource for all services. 

        :return: The submit_time_utc of this VasV2TaxVoid200Response.
        :rtype: str
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this VasV2TaxVoid200Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` **Example** `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC.  Returned by Cybersource for all services. 

        :param submit_time_utc: The submit_time_utc of this VasV2TaxVoid200Response.
        :type: str
        """

        self._submit_time_utc = submit_time_utc

    @property
    def status(self):
        """
        Gets the status of this VasV2TaxVoid200Response.
        The status of the submitted transaction.  Possible values:  - VOIDED 

        :return: The status of this VasV2TaxVoid200Response.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this VasV2TaxVoid200Response.
        The status of the submitted transaction.  Possible values:  - VOIDED 

        :param status: The status of this VasV2TaxVoid200Response.
        :type: str
        """

        self._status = status

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this VasV2TaxVoid200Response.

        :return: The client_reference_information of this VasV2TaxVoid200Response.
        :rtype: PtsV2IncrementalAuthorizationPatch201ResponseClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this VasV2TaxVoid200Response.

        :param client_reference_information: The client_reference_information of this VasV2TaxVoid200Response.
        :type: PtsV2IncrementalAuthorizationPatch201ResponseClientReferenceInformation
        """

        self._client_reference_information = client_reference_information

    @property
    def void_amount_details(self):
        """
        Gets the void_amount_details of this VasV2TaxVoid200Response.

        :return: The void_amount_details of this VasV2TaxVoid200Response.
        :rtype: VasV2TaxVoid200ResponseVoidAmountDetails
        """
        return self._void_amount_details

    @void_amount_details.setter
    def void_amount_details(self, void_amount_details):
        """
        Sets the void_amount_details of this VasV2TaxVoid200Response.

        :param void_amount_details: The void_amount_details of this VasV2TaxVoid200Response.
        :type: VasV2TaxVoid200ResponseVoidAmountDetails
        """

        self._void_amount_details = void_amount_details

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, VasV2TaxVoid200Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
