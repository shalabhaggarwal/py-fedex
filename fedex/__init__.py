#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    fedex

    Fedex API

    :copyright: (c) 2010 by Sharoon Thomas.
    :copyright: (c) 2010-2013 by Openlabs Technologies & Consulting (P) Ltd.
    :license: GPLv3, see LICENSE for more details
'''
__all__ = (
    'AddressValidationService',
    'AccountInformation',
    'load_accountinfo_from_file',
    'ProcessShipmentRequest',
)

from .api import VERSION as __version__
from .address_validation_service import AddressValidationService
from .ship_services import ProcessShipmentRequest
from .structures import AccountInformation, load_accountinfo_from_file
