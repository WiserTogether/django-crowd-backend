import logging

__version_tuple__ = (0, 0, 1, 'pre-alpha', 2)

def get_version():
    version = '%s.%s' % (__version_tuple__[0], __version_tuple__[1])
    if __version_tuple__[2]:
        version = '%s.%s' % (version, __version_tuple__[2])
    if __version_tuple__[3:] == ('alpha', 0):
        version = '%s.pre-alpha' % version
    else:
        if __version_tuple__[3] != 'final':
            version = "%s.%s" % (version, __version_tuple__[3])
            if __version_tuple__[4] != 0:
                version = '%s.%s' % (version, __version_tuple__[4])
    return version

__version__ = get_version()
logger = logging.getLogger(__name__)

