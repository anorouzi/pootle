# -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

from __future__ import absolute_import

from babel import (UnknownLocaleError, core as babel_core,
                   support as babel_support)

from django.conf import settings
from django.utils.translation import get_language, to_locale


def _get_locale_formats():
    try:
        locale = babel_core.Locale.parse(to_locale(get_language()))
    except UnknownLocaleError:
        locale = settings.LANGUAGE_CODE
    return babel_support.Format(locale)


def _clean_zero(number):
    if number is None or number == '':
        return 0
    return number


def number(number):
    number = _clean_zero(number)
    return _get_locale_formats().number(number)


def percent(number, format=None):
    number = _clean_zero(number)
    return _get_locale_formats().percent(number, format)
