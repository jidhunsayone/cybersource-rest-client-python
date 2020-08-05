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


class Tmsv2customersMerchantDefinedInformation(object):
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
        'name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, name=None, value=None):
        """
        Tmsv2customersMerchantDefinedInformation - a model defined in Swagger
        """

        self._name = None
        self._value = None

        if name is not None:
          self.name = name
        if value is not None:
          self.value = value

    @property
    def name(self):
        """
        Gets the name of this Tmsv2customersMerchantDefinedInformation.
        The number you assign as the name for your merchant-defined data or secure field. Valid values are data1 to data4 and sensitive1 to sensitive4  For example, to set the name for merchant-defined data 2 field, you would reference merchantDefinedInformation[x].name as data2 Valid values: - data1 - data2 - data3 - data4 - sensitive1 - sensitive2 - sensitive3 - sensitive4 

        :return: The name of this Tmsv2customersMerchantDefinedInformation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Tmsv2customersMerchantDefinedInformation.
        The number you assign as the name for your merchant-defined data or secure field. Valid values are data1 to data4 and sensitive1 to sensitive4  For example, to set the name for merchant-defined data 2 field, you would reference merchantDefinedInformation[x].name as data2 Valid values: - data1 - data2 - data3 - data4 - sensitive1 - sensitive2 - sensitive3 - sensitive4 

        :param name: The name of this Tmsv2customersMerchantDefinedInformation.
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """
        Gets the value of this Tmsv2customersMerchantDefinedInformation.
        The value you assign for your merchant-defined data field.  **Warning** Merchant-defined data fields are not intended to and must not be used to capture personally identifying information. Accordingly, merchants are prohibited from capturing, obtaining, and/or transmitting any personally identifying information in or via the merchant-defined data fields. Personally identifying information includes, but is not limited to, address, credit card number, social security number, driver's license number, state-issued identification number, passport number, and card verification numbers (CVV, CVC2, CVV2, CID, CVN). In the event CyberSource discovers that a merchant is capturing and/or transmitting personally identifying information via the merchant-defined data fields, whether or not intentionally, CyberSource will immediately suspend the merchant's account, which will result in a rejection of any and all transaction requests submitted by the merchant after the point of suspension. 

        :return: The value of this Tmsv2customersMerchantDefinedInformation.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Tmsv2customersMerchantDefinedInformation.
        The value you assign for your merchant-defined data field.  **Warning** Merchant-defined data fields are not intended to and must not be used to capture personally identifying information. Accordingly, merchants are prohibited from capturing, obtaining, and/or transmitting any personally identifying information in or via the merchant-defined data fields. Personally identifying information includes, but is not limited to, address, credit card number, social security number, driver's license number, state-issued identification number, passport number, and card verification numbers (CVV, CVC2, CVV2, CID, CVN). In the event CyberSource discovers that a merchant is capturing and/or transmitting personally identifying information via the merchant-defined data fields, whether or not intentionally, CyberSource will immediately suspend the merchant's account, which will result in a rejection of any and all transaction requests submitted by the merchant after the point of suspension. 

        :param value: The value of this Tmsv2customersMerchantDefinedInformation.
        :type: str
        """
        if value is not None and len(value) > 100:
            raise ValueError("Invalid value for `value`, length must be less than or equal to `100`")

        self._value = value

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
        if not isinstance(other, Tmsv2customersMerchantDefinedInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
