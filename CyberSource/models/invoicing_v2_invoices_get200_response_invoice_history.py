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


class InvoicingV2InvoicesGet200ResponseInvoiceHistory(object):
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
        'event': 'str',
        'date': 'datetime',
        'transaction_details': 'InvoicingV2InvoicesGet200ResponseTransactionDetails'
    }

    attribute_map = {
        'event': 'event',
        'date': 'date',
        'transaction_details': 'transactionDetails'
    }

    def __init__(self, event=None, date=None, transaction_details=None):
        """
        InvoicingV2InvoicesGet200ResponseInvoiceHistory - a model defined in Swagger
        """

        self._event = None
        self._date = None
        self._transaction_details = None

        if event is not None:
          self.event = event
        if date is not None:
          self.date = date
        if transaction_details is not None:
          self.transaction_details = transaction_details

    @property
    def event(self):
        """
        Gets the event of this InvoicingV2InvoicesGet200ResponseInvoiceHistory.
        The event triggered for the invoice.  Possible values:  - `CREATE`  - `UPDATE`  - `SEND`  - `RESEND`  - `REMINDER`  - `PAYMENT`  - `CANCEL` 

        :return: The event of this InvoicingV2InvoicesGet200ResponseInvoiceHistory.
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """
        Sets the event of this InvoicingV2InvoicesGet200ResponseInvoiceHistory.
        The event triggered for the invoice.  Possible values:  - `CREATE`  - `UPDATE`  - `SEND`  - `RESEND`  - `REMINDER`  - `PAYMENT`  - `CANCEL` 

        :param event: The event of this InvoicingV2InvoicesGet200ResponseInvoiceHistory.
        :type: str
        """

        self._event = event

    @property
    def date(self):
        """
        Gets the date of this InvoicingV2InvoicesGet200ResponseInvoiceHistory.
        The date and time when the invoice event was triggered in ISO 8601 format. Format: YYYY-MM-DDThh:mm:ssZ 

        :return: The date of this InvoicingV2InvoicesGet200ResponseInvoiceHistory.
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this InvoicingV2InvoicesGet200ResponseInvoiceHistory.
        The date and time when the invoice event was triggered in ISO 8601 format. Format: YYYY-MM-DDThh:mm:ssZ 

        :param date: The date of this InvoicingV2InvoicesGet200ResponseInvoiceHistory.
        :type: datetime
        """

        self._date = date

    @property
    def transaction_details(self):
        """
        Gets the transaction_details of this InvoicingV2InvoicesGet200ResponseInvoiceHistory.

        :return: The transaction_details of this InvoicingV2InvoicesGet200ResponseInvoiceHistory.
        :rtype: InvoicingV2InvoicesGet200ResponseTransactionDetails
        """
        return self._transaction_details

    @transaction_details.setter
    def transaction_details(self, transaction_details):
        """
        Sets the transaction_details of this InvoicingV2InvoicesGet200ResponseInvoiceHistory.

        :param transaction_details: The transaction_details of this InvoicingV2InvoicesGet200ResponseInvoiceHistory.
        :type: InvoicingV2InvoicesGet200ResponseTransactionDetails
        """

        self._transaction_details = transaction_details

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
        if not isinstance(other, InvoicingV2InvoicesGet200ResponseInvoiceHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
