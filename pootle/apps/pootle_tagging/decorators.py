#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2013 Zuza Software Foundation
#
# This file is part of Pootle.
#
# Pootle is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# Pootle is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Pootle; if not, see <http://www.gnu.org/licenses/>.

import logging
from functools import wraps

from django.conf import settings
from django.core.cache import cache
from django.utils.encoding import iri_to_uri


def get_from_cache_for_path(func, timeout=settings.OBJECT_CACHE_TIMEOUT):
    @wraps(func)
    def wrapper(instance, pootle_path, *args, **kwargs):
        key = iri_to_uri(":".join([instance.pootle_path, pootle_path,
                                   func.__name__]))
        result = cache.get(key)
        if result is None:
            logging.debug(u"cache miss for %s", key)
            result = func(instance, pootle_path, *args, **kwargs)
            cache.set(key, result, timeout)
        return result
    return wrapper
