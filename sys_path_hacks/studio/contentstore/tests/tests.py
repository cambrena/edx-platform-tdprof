from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('cms.djangoapps', 'contentstore.tests.tests')

from cms.djangoapps.contentstore.tests.tests import *