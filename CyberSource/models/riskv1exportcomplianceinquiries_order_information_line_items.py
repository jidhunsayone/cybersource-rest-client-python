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


class Riskv1exportcomplianceinquiriesOrderInformationLineItems(object):
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
        'unit_price': 'str',
        'allowed_export_countries': 'list[str]',
        'restricted_export_countries': 'list[str]',
        'quantity': 'int',
        'product_sku': 'str',
        'product_risk': 'str',
        'product_name': 'str',
        'product_code': 'str'
    }

    attribute_map = {
        'unit_price': 'unitPrice',
        'allowed_export_countries': 'allowedExportCountries',
        'restricted_export_countries': 'restrictedExportCountries',
        'quantity': 'quantity',
        'product_sku': 'productSKU',
        'product_risk': 'productRisk',
        'product_name': 'productName',
        'product_code': 'productCode'
    }

    def __init__(self, unit_price=None, allowed_export_countries=None, restricted_export_countries=None, quantity=None, product_sku=None, product_risk=None, product_name=None, product_code=None):
        """
        Riskv1exportcomplianceinquiriesOrderInformationLineItems - a model defined in Swagger
        """

        self._unit_price = None
        self._allowed_export_countries = None
        self._restricted_export_countries = None
        self._quantity = None
        self._product_sku = None
        self._product_risk = None
        self._product_name = None
        self._product_code = None

        self.unit_price = unit_price
        if allowed_export_countries is not None:
          self.allowed_export_countries = allowed_export_countries
        if restricted_export_countries is not None:
          self.restricted_export_countries = restricted_export_countries
        if quantity is not None:
          self.quantity = quantity
        if product_sku is not None:
          self.product_sku = product_sku
        if product_risk is not None:
          self.product_risk = product_risk
        if product_name is not None:
          self.product_name = product_name
        if product_code is not None:
          self.product_code = product_code

    @property
    def unit_price(self):
        """
        Gets the unit_price of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        Per-item price of the product. This value for this field cannot be negative.  You must include either this field or the request-level field `orderInformation.amountDetails.totalAmount` in your request.  You can include a decimal point (.), but you cannot include any other special characters. The value is truncated to the correct number of decimal places.  #### DCC with a Third-Party Provider Set this field to the converted amount that was returned by the DCC provider. You must include either the 1st line item in the order and this field, or the request-level field `orderInformation.amountDetails.totalAmount` in your request.  #### FDMS South If you accept IDR or CLP currencies, see the entry for FDMS South in the [Merchant Descriptors Using the SCMP API Guide.] (https://apps.cybersource.com/library/documentation/dev_guides/Merchant_Descriptors_SCMP_API/html/)  #### Tax Calculation Required field for U.S., Canadian, international and value added taxes.  #### Zero Amount Authorizations If your processor supports zero amount authorizations, you can set this field to 0 for the authorization to check if the card is lost or stolen.  #### Maximum Field Lengths For GPN and JCN Gateway: Decimal (10) All other processors: Decimal (15) 

        :return: The unit_price of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        :rtype: str
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """
        Sets the unit_price of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        Per-item price of the product. This value for this field cannot be negative.  You must include either this field or the request-level field `orderInformation.amountDetails.totalAmount` in your request.  You can include a decimal point (.), but you cannot include any other special characters. The value is truncated to the correct number of decimal places.  #### DCC with a Third-Party Provider Set this field to the converted amount that was returned by the DCC provider. You must include either the 1st line item in the order and this field, or the request-level field `orderInformation.amountDetails.totalAmount` in your request.  #### FDMS South If you accept IDR or CLP currencies, see the entry for FDMS South in the [Merchant Descriptors Using the SCMP API Guide.] (https://apps.cybersource.com/library/documentation/dev_guides/Merchant_Descriptors_SCMP_API/html/)  #### Tax Calculation Required field for U.S., Canadian, international and value added taxes.  #### Zero Amount Authorizations If your processor supports zero amount authorizations, you can set this field to 0 for the authorization to check if the card is lost or stolen.  #### Maximum Field Lengths For GPN and JCN Gateway: Decimal (10) All other processors: Decimal (15) 

        :param unit_price: The unit_price of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        :type: str
        """
        if unit_price is None:
            raise ValueError("Invalid value for `unit_price`, must not be `None`")
        if unit_price is not None and len(unit_price) > 15:
            raise ValueError("Invalid value for `unit_price`, length must be less than or equal to `15`")

        self._unit_price = unit_price

    @property
    def allowed_export_countries(self):
        """
        Gets the allowed_export_countries of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.

        :return: The allowed_export_countries of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        :rtype: list[str]
        """
        return self._allowed_export_countries

    @allowed_export_countries.setter
    def allowed_export_countries(self, allowed_export_countries):
        """
        Sets the allowed_export_countries of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.

        :param allowed_export_countries: The allowed_export_countries of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        :type: list[str]
        """

        self._allowed_export_countries = allowed_export_countries

    @property
    def restricted_export_countries(self):
        """
        Gets the restricted_export_countries of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.

        :return: The restricted_export_countries of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        :rtype: list[str]
        """
        return self._restricted_export_countries

    @restricted_export_countries.setter
    def restricted_export_countries(self, restricted_export_countries):
        """
        Sets the restricted_export_countries of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.

        :param restricted_export_countries: The restricted_export_countries of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        :type: list[str]
        """

        self._restricted_export_countries = restricted_export_countries

    @property
    def quantity(self):
        """
        Gets the quantity of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        Number of units for this order. Must be a non-negative integer.  The default is `1`. For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not `default` or one of the other values related to shipping and/or handling.  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes. 

        :return: The quantity of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        Number of units for this order. Must be a non-negative integer.  The default is `1`. For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not `default` or one of the other values related to shipping and/or handling.  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes. 

        :param quantity: The quantity of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        :type: int
        """
        if quantity is not None and quantity > 999999999:
            raise ValueError("Invalid value for `quantity`, must be a value less than or equal to `999999999`")
        if quantity is not None and quantity < 1:
            raise ValueError("Invalid value for `quantity`, must be a value greater than or equal to `1`")

        self._quantity = quantity

    @property
    def product_sku(self):
        """
        Gets the product_sku of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        Product identifier code. Also known as the Stock Keeping Unit (SKU) code for the product.  For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not set to **default** or one of the other values that are related to shipping and/or handling.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not `default` or one of the values related to shipping and/or handling. 

        :return: The product_sku of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        :rtype: str
        """
        return self._product_sku

    @product_sku.setter
    def product_sku(self, product_sku):
        """
        Sets the product_sku of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        Product identifier code. Also known as the Stock Keeping Unit (SKU) code for the product.  For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not set to **default** or one of the other values that are related to shipping and/or handling.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not `default` or one of the values related to shipping and/or handling. 

        :param product_sku: The product_sku of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        :type: str
        """
        if product_sku is not None and len(product_sku) > 255:
            raise ValueError("Invalid value for `product_sku`, length must be less than or equal to `255`")

        self._product_sku = product_sku

    @property
    def product_risk(self):
        """
        Gets the product_risk of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        Indicates the level of risk for the product. This field can contain one of the following values: - `low`: The product is associated with few chargebacks. - `normal`: The product is associated with a normal number of chargebacks. - `high`: The product is associated with many chargebacks. 

        :return: The product_risk of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        :rtype: str
        """
        return self._product_risk

    @product_risk.setter
    def product_risk(self, product_risk):
        """
        Sets the product_risk of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        Indicates the level of risk for the product. This field can contain one of the following values: - `low`: The product is associated with few chargebacks. - `normal`: The product is associated with a normal number of chargebacks. - `high`: The product is associated with many chargebacks. 

        :param product_risk: The product_risk of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        :type: str
        """
        if product_risk is not None and len(product_risk) > 6:
            raise ValueError("Invalid value for `product_risk`, length must be less than or equal to `6`")

        self._product_risk = product_risk

    @property
    def product_name(self):
        """
        Gets the product_name of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        For an authorization or capture transaction (`processingOptions.capture` is `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not `default` or one of the other values that are related to shipping and/or handling.  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes. 

        :return: The product_name of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """
        Sets the product_name of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        For an authorization or capture transaction (`processingOptions.capture` is `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not `default` or one of the other values that are related to shipping and/or handling.  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes. 

        :param product_name: The product_name of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        :type: str
        """
        if product_name is not None and len(product_name) > 255:
            raise ValueError("Invalid value for `product_name`, length must be less than or equal to `255`")

        self._product_name = product_name

    @property
    def product_code(self):
        """
        Gets the product_code of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        Type of product. The value for this field is used to identify the product category (electronic, handling, physical, service, or shipping). The default value is `default`.  If you are performing an authorization transaction (`processingOptions.capture` is set to `false`), and you set this field to a value other than `default` or one of the values related to shipping and/or handling, then `orderInformation.lineItems[].quantity`, `orderInformation.lineItems[].productName`, and `orderInformation.lineItems[].productSku` fields are required.  Optional field.  For details, see the `product_code` field description in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/).  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes.  To use the tax calculation service, use values listed in the Tax Product Code Guide. For information about this document, contact customer support. See \"Product Codes,\" page 14, for more information. 

        :return: The product_code of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        :rtype: str
        """
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        """
        Sets the product_code of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        Type of product. The value for this field is used to identify the product category (electronic, handling, physical, service, or shipping). The default value is `default`.  If you are performing an authorization transaction (`processingOptions.capture` is set to `false`), and you set this field to a value other than `default` or one of the values related to shipping and/or handling, then `orderInformation.lineItems[].quantity`, `orderInformation.lineItems[].productName`, and `orderInformation.lineItems[].productSku` fields are required.  Optional field.  For details, see the `product_code` field description in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/).  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes.  To use the tax calculation service, use values listed in the Tax Product Code Guide. For information about this document, contact customer support. See \"Product Codes,\" page 14, for more information. 

        :param product_code: The product_code of this Riskv1exportcomplianceinquiriesOrderInformationLineItems.
        :type: str
        """
        if product_code is not None and len(product_code) > 255:
            raise ValueError("Invalid value for `product_code`, length must be less than or equal to `255`")

        self._product_code = product_code

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
        if not isinstance(other, Riskv1exportcomplianceinquiriesOrderInformationLineItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
