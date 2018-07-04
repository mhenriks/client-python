# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BigInt(object):
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
        'abs': 'list[BigWord]',
        'neg': 'bool'
    }

    attribute_map = {
        'abs': 'abs',
        'neg': 'neg'
    }

    def __init__(self, abs=None, neg=None):
        """
        BigInt - a model defined in Swagger
        """

        self._abs = None
        self._neg = None

        self.abs = abs
        self.neg = neg

    @property
    def abs(self):
        """
        Gets the abs of this BigInt.

        :return: The abs of this BigInt.
        :rtype: list[BigWord]
        """
        return self._abs

    @abs.setter
    def abs(self, abs):
        """
        Sets the abs of this BigInt.

        :param abs: The abs of this BigInt.
        :type: list[BigWord]
        """
        if abs is None:
            raise ValueError("Invalid value for `abs`, must not be `None`")

        self._abs = abs

    @property
    def neg(self):
        """
        Gets the neg of this BigInt.

        :return: The neg of this BigInt.
        :rtype: bool
        """
        return self._neg

    @neg.setter
    def neg(self, neg):
        """
        Sets the neg of this BigInt.

        :param neg: The neg of this BigInt.
        :type: bool
        """
        if neg is None:
            raise ValueError("Invalid value for `neg`, must not be `None`")

        self._neg = neg

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
        if not isinstance(other, BigInt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other