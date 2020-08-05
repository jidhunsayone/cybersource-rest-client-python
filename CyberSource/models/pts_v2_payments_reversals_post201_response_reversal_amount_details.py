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


class PtsV2PaymentsReversalsPost201ResponseReversalAmountDetails(object):
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
        'reversed_amount': 'str',
        'original_transaction_amount': 'str',
        'currency': 'str'
    }

    attribute_map = {
        'reversed_amount': 'reversedAmount',
        'original_transaction_amount': 'originalTransactionAmount',
        'currency': 'currency'
    }

    def __init__(self, reversed_amount=None, original_transaction_amount=None, currency=None):
        """
        PtsV2PaymentsReversalsPost201ResponseReversalAmountDetails - a model defined in Swagger
        """

        self._reversed_amount = None
        self._original_transaction_amount = None
        self._currency = None

        if reversed_amount is not None:
          self.reversed_amount = reversed_amount
        if original_transaction_amount is not None:
          self.original_transaction_amount = original_transaction_amount
        if currency is not None:
          self.currency = currency

    @property
    def reversed_amount(self):
        """
        Gets the reversed_amount of this PtsV2PaymentsReversalsPost201ResponseReversalAmountDetails.
        Total reversed amount.  Returned by authorization reversal. 

        :return: The reversed_amount of this PtsV2PaymentsReversalsPost201ResponseReversalAmountDetails.
        :rtype: str
        """
        return self._reversed_amount

    @reversed_amount.setter
    def reversed_amount(self, reversed_amount):
        """
        Sets the reversed_amount of this PtsV2PaymentsReversalsPost201ResponseReversalAmountDetails.
        Total reversed amount.  Returned by authorization reversal. 

        :param reversed_amount: The reversed_amount of this PtsV2PaymentsReversalsPost201ResponseReversalAmountDetails.
        :type: str
        """
        if reversed_amount is not None and len(reversed_amount) > 15:
            raise ValueError("Invalid value for `reversed_amount`, length must be less than or equal to `15`")

        self._reversed_amount = reversed_amount

    @property
    def original_transaction_amount(self):
        """
        Gets the original_transaction_amount of this PtsV2PaymentsReversalsPost201ResponseReversalAmountDetails.
        Amount of the original transaction.  Returned by authorization reversal and void. 

        :return: The original_transaction_amount of this PtsV2PaymentsReversalsPost201ResponseReversalAmountDetails.
        :rtype: str
        """
        return self._original_transaction_amount

    @original_transaction_amount.setter
    def original_transaction_amount(self, original_transaction_amount):
        """
        Sets the original_transaction_amount of this PtsV2PaymentsReversalsPost201ResponseReversalAmountDetails.
        Amount of the original transaction.  Returned by authorization reversal and void. 

        :param original_transaction_amount: The original_transaction_amount of this PtsV2PaymentsReversalsPost201ResponseReversalAmountDetails.
        :type: str
        """
        if original_transaction_amount is not None and len(original_transaction_amount) > 15:
            raise ValueError("Invalid value for `original_transaction_amount`, length must be less than or equal to `15`")

        self._original_transaction_amount = original_transaction_amount

    @property
    def currency(self):
        """
        Gets the currency of this PtsV2PaymentsReversalsPost201ResponseReversalAmountDetails.
        Currency used for the order. Use the three-character [ISO Standard Currency Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf)  #### Used by **Authorization** Required field.  **Authorization Reversal** For an authorization reversal (`reversalInformation`) or a capture (`processingOptions.capture` is set to `true`), you must use the same currency that you used in your payment authorization request.  #### PIN Debit Currency for the amount you requested for the PIN debit purchase. This value is returned for partial authorizations. The issuing bank can approve a partial amount if the balance on the debit card is less than the requested transaction amount. For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf). Returned by PIN debit purchase.  For PIN debit reversal requests, you must use the same currency that was used for the PIN debit purchase or PIN debit credit that you are reversing. For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf).  Required field for PIN Debit purchase and PIN Debit credit requests. Optional field for PIN Debit reversal requests.  #### GPX This field is optional for reversing an authorization or credit.  #### DCC for First Data Your local currency. For details, see the `currency` field description in [Dynamic Currency Conversion For First Data Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/DCC_FirstData_SCMP/DCC_FirstData_SCMP_API.pdf).  #### Tax Calculation Required for international tax and value added tax only. Optional for U.S. and Canadian taxes. Your local currency. 

        :return: The currency of this PtsV2PaymentsReversalsPost201ResponseReversalAmountDetails.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this PtsV2PaymentsReversalsPost201ResponseReversalAmountDetails.
        Currency used for the order. Use the three-character [ISO Standard Currency Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf)  #### Used by **Authorization** Required field.  **Authorization Reversal** For an authorization reversal (`reversalInformation`) or a capture (`processingOptions.capture` is set to `true`), you must use the same currency that you used in your payment authorization request.  #### PIN Debit Currency for the amount you requested for the PIN debit purchase. This value is returned for partial authorizations. The issuing bank can approve a partial amount if the balance on the debit card is less than the requested transaction amount. For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf). Returned by PIN debit purchase.  For PIN debit reversal requests, you must use the same currency that was used for the PIN debit purchase or PIN debit credit that you are reversing. For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf).  Required field for PIN Debit purchase and PIN Debit credit requests. Optional field for PIN Debit reversal requests.  #### GPX This field is optional for reversing an authorization or credit.  #### DCC for First Data Your local currency. For details, see the `currency` field description in [Dynamic Currency Conversion For First Data Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/DCC_FirstData_SCMP/DCC_FirstData_SCMP_API.pdf).  #### Tax Calculation Required for international tax and value added tax only. Optional for U.S. and Canadian taxes. Your local currency. 

        :param currency: The currency of this PtsV2PaymentsReversalsPost201ResponseReversalAmountDetails.
        :type: str
        """
        if currency is not None and len(currency) > 3:
            raise ValueError("Invalid value for `currency`, length must be less than or equal to `3`")

        self._currency = currency

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
        if not isinstance(other, PtsV2PaymentsReversalsPost201ResponseReversalAmountDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
