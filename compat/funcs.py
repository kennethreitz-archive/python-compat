# -*- coding: utf-8 -*-

"""
compat.funcs
~~~~~~~~~~~~

This module contains helper functions.
"""


from .flags import is_py2, is_py3



if is_py3:
    from io import BytesIO
    unicode = str
    bytes = bytes
    basestring = str

else:
    from cStringIO import StringIO as BytesIO
