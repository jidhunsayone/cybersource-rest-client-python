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


class Ptsv2paymentsPaymentInformationFluidData(object):
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
        'key_serial_number': 'str',
        'descriptor': 'str',
        'value': 'str',
        'encoding': 'str'
    }

    attribute_map = {
        'key_serial_number': 'keySerialNumber',
        'descriptor': 'descriptor',
        'value': 'value',
        'encoding': 'encoding'
    }

    def __init__(self, key_serial_number=None, descriptor=None, value=None, encoding=None):
        """
        Ptsv2paymentsPaymentInformationFluidData - a model defined in Swagger
        """

        self._key_serial_number = None
        self._descriptor = None
        self._value = None
        self._encoding = None

        if key_serial_number is not None:
          self.key_serial_number = key_serial_number
        if descriptor is not None:
          self.descriptor = descriptor
        if value is not None:
          self.value = value
        if encoding is not None:
          self.encoding = encoding

    @property
    def key_serial_number(self):
        """
        Gets the key_serial_number of this Ptsv2paymentsPaymentInformationFluidData.
        The encoded or encrypted value that a payment solution returns for an authorization request. For details about the valid values for a key, see [Creating an Online Authorization](https://developer.cybersource.com/api/developer-guides/dita-payments/CreatingOnlineAuth.html) 

        :return: The key_serial_number of this Ptsv2paymentsPaymentInformationFluidData.
        :rtype: str
        """
        return self._key_serial_number

    @key_serial_number.setter
    def key_serial_number(self, key_serial_number):
        """
        Sets the key_serial_number of this Ptsv2paymentsPaymentInformationFluidData.
        The encoded or encrypted value that a payment solution returns for an authorization request. For details about the valid values for a key, see [Creating an Online Authorization](https://developer.cybersource.com/api/developer-guides/dita-payments/CreatingOnlineAuth.html) 

        :param key_serial_number: The key_serial_number of this Ptsv2paymentsPaymentInformationFluidData.
        :type: str
        """

        self._key_serial_number = key_serial_number

    @property
    def descriptor(self):
        """
        Gets the descriptor of this Ptsv2paymentsPaymentInformationFluidData.
        The identifier for a payment solution, which is sending the encrypted payment data for decryption. Valid values: Samsung Pay: RklEPUNPTU1PTi5TQU1TVU5HLklOQVBQLlBBWU1FTlQ= Note: For other payment solutions, the value may be specific to the terminal or device initiatinf the payment. For example, the descriptor for a Bluefin payment encryption would be a device-generated descriptor. Used by Authorization and Standalone Credits. Required for authorizations and standalone credits.  Card Present processing: Format of the encrypted payment data. The value for Bluefin PCI P2PE is `Ymx1ZWZpbg==`. paymentInformation.fluidData.encoding must be `Base64`. The value for Cybersource P2PE decryption depends on the encoding method used and identified in encoding field. If paymentInformation.fluidData.encoding is `Base64`, the value is: `RklEPUVNVi5QQVlNRU5ULkFQSQ==` If paymentInformation.fluidData.encoding is `HEX`, the value is: `4649443D454D562E5041594D454E542E41504` 

        :return: The descriptor of this Ptsv2paymentsPaymentInformationFluidData.
        :rtype: str
        """
        return self._descriptor

    @descriptor.setter
    def descriptor(self, descriptor):
        """
        Sets the descriptor of this Ptsv2paymentsPaymentInformationFluidData.
        The identifier for a payment solution, which is sending the encrypted payment data for decryption. Valid values: Samsung Pay: RklEPUNPTU1PTi5TQU1TVU5HLklOQVBQLlBBWU1FTlQ= Note: For other payment solutions, the value may be specific to the terminal or device initiatinf the payment. For example, the descriptor for a Bluefin payment encryption would be a device-generated descriptor. Used by Authorization and Standalone Credits. Required for authorizations and standalone credits.  Card Present processing: Format of the encrypted payment data. The value for Bluefin PCI P2PE is `Ymx1ZWZpbg==`. paymentInformation.fluidData.encoding must be `Base64`. The value for Cybersource P2PE decryption depends on the encoding method used and identified in encoding field. If paymentInformation.fluidData.encoding is `Base64`, the value is: `RklEPUVNVi5QQVlNRU5ULkFQSQ==` If paymentInformation.fluidData.encoding is `HEX`, the value is: `4649443D454D562E5041594D454E542E41504` 

        :param descriptor: The descriptor of this Ptsv2paymentsPaymentInformationFluidData.
        :type: str
        """

        self._descriptor = descriptor

    @property
    def value(self):
        """
        Gets the value of this Ptsv2paymentsPaymentInformationFluidData.
        Represents the encrypted payment data BLOB. The entry for this field is dependent on the payment solution used by the merchant. Used by Authorization and Standalone Credits. Required for authorizations and standalone credits that use a Cybersource suppored Point-to-Point encryption method. Card Present processing This field represents the encrypted payment data generated by the payment terminal/device. 

        :return: The value of this Ptsv2paymentsPaymentInformationFluidData.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Ptsv2paymentsPaymentInformationFluidData.
        Represents the encrypted payment data BLOB. The entry for this field is dependent on the payment solution used by the merchant. Used by Authorization and Standalone Credits. Required for authorizations and standalone credits that use a Cybersource suppored Point-to-Point encryption method. Card Present processing This field represents the encrypted payment data generated by the payment terminal/device. 

        :param value: The value of this Ptsv2paymentsPaymentInformationFluidData.
        :type: str
        """

        self._value = value

    @property
    def encoding(self):
        """
        Gets the encoding of this Ptsv2paymentsPaymentInformationFluidData.
        Encoding method used to encrypt the payment data. Valid values: `Base64`, `HEX` If no value is provided, `Base64` is taken as the default value. And the `Base64` descriptor is used for paymentInformation.fluidData.encoding 

        :return: The encoding of this Ptsv2paymentsPaymentInformationFluidData.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """
        Sets the encoding of this Ptsv2paymentsPaymentInformationFluidData.
        Encoding method used to encrypt the payment data. Valid values: `Base64`, `HEX` If no value is provided, `Base64` is taken as the default value. And the `Base64` descriptor is used for paymentInformation.fluidData.encoding 

        :param encoding: The encoding of this Ptsv2paymentsPaymentInformationFluidData.
        :type: str
        """

        self._encoding = encoding

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
        if not isinstance(other, Ptsv2paymentsPaymentInformationFluidData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
