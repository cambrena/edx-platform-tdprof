from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('cms.djangoapps', 'contentstore.management.commands.generate_courses')

from cms.djangoapps.contentstore.management.commands.generate_courses import *