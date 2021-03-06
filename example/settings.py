# Before we do anything else, get some default settings built into Arkestra.
# They are not just Arkestra settings, but settings for other applications
# that Arkestra requires to be just so.
 
from arkestra_utilities.settings import *

# Django settings for arkestra_medic project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'example.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'
DATE_FORMAT = "jS F Y"
TIME_FORMAT = "H\.i"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

import os
import os.path

BASE_PATH = os.path.normpath(os.path.dirname(__file__))


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = BASE_PATH+'/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/topdog/html/arkestra_medic/static'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'legacy_finders.LegacyAppDirectoriesFinder',    
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'n!xrr^bssm6pf&rm$#vq7eg=p-n-p2wi*5^vocgitt5ez&##ra'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    'django.core.context_processors.static',
    'django.core.context_processors.csrf',
    'django.contrib.messages.context_processors.messages',

    "cms.context_processors.media",

    "arkestra_utilities.context_processors.arkestra_templates",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.media.PlaceholderMediaMiddleware',
    
)

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    )

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    BASE_PATH+'/templates/',
)

# ------------------------ Django CMS

gettext = lambda s: s

# this is only here because I don't know how to make other apps find it otherwise, and they rely on it.
CMS_MEDIA_URL = STATIC_URL + 'cms/'

CMS_TEMPLATES = (
    ('arkestra.html', gettext('Arkestra')),
    ('institute.html', gettext('Institute of Mediaeval Medicine')),
)

CMS_PAGE_FLAGS = (
    ('no_local_menu', 'Hide local menu') ,
    ('no_horizontal_menu', 'No horizontal menu') ,
    ('no_page_title', "Don't display page title") ,
    )

CMS_PLACEHOLDER_CONF = {                        
    'body': {
        "plugins": (
            'SemanticTextPlugin', 
            'CMSVacanciesPlugin', 
            'CMSNewsAndEventsPlugin', 
            'SnippetPlugin', 
            'LinksPlugin', 
            'CMSPublicationsPlugin', 
            'ImagePlugin', 
            'EntityAutoPageLinkPluginPublisher', 
            'FilerImagePlugin', 
            'EntityDirectoryPluginPublisher', 
            'CarouselPluginPublisher',
            'FocusOnPluginPublisher',
            ),
        "extra_context": {            
            "width":"880",
            },
        "name": gettext("body"),
    },
}

LANGUAGES = (
('en', gettext('English')),
('cy', gettext('Cymraeg')),
)


INSTALLED_APPS = (

     # Django CMS applications

    'cms',
    'menus',
    'appmedia',
    'cms.plugins.text',
    'cms.plugins.snippet',

    # Arkestra applications
    
    'contacts_and_people',
    'vacancies_and_studentships',
    'news_and_events',
    'links',
    'arkestra_utilities',
    'arkestra_utilities.widgets.combobox', # so that static-files picks it up
    'arkestra_image_plugin',    

    # other applications
    
    'polymorphic',
    'semanticeditor',
    'mptt',
    'easy_thumbnails',
    'typogrify',
    'filer',    
    'widgetry',
#    'south',

    # core Django applications

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.humanize',
    'django.contrib.staticfiles',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

from arkestra_settings import *