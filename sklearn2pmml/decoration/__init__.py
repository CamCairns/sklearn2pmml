#!/usr/bin/env python

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils import column_or_1d

import numpy

__copyright__ = "Copyright (c) 2016 Villu Ruusmann"
__license__ = "GNU Affero General Public License (AGPL) version 3.0"

class Domain(BaseEstimator, TransformerMixin):

	def __init__(self, invalid_value_treatment = "return_invalid"):
		invalid_value_treatments = ["return_invalid", "as_is", "as_missing"]
		if invalid_value_treatment not in invalid_value_treatments:
			raise ValueError("Invalid value treatment {0} not in {1}".format(invalid_value_treatment, invalid_value_treatments))
		self.invalid_value_treatment = invalid_value_treatment

class CategoricalDomain(Domain):

	def __init__(self, invalid_value_treatment = "return_invalid"):
		Domain.__init__(self, invalid_value_treatment)

	def fit(self, y):
		y = column_or_1d(y, warn = True)
		self.data_ = numpy.unique(y[~numpy.isnan(y)])
		return self

	def transform(self, y):
		return y

class ContinuousDomain(Domain):

	def __init__(self, invalid_value_treatment = "return_invalid"):
		Domain.__init__(self, invalid_value_treatment)

	def fit(self, X, y = None):
		self.data_min_ = numpy.nanmin(X, axis = 0)
		self.data_max_ = numpy.nanmax(X, axis = 0)
		return self

	def transform(self, X):
		return X
