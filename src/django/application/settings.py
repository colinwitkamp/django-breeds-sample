#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Default settings for the project. All settings which remain consistent across each of the different environments should
be added here.
"""
import multiprocessing
import os
import sys


def _(s):
    """
    Dummy get text function to allow for Django to find and mark strings for translation.
    """
    return s


# ------------------------------------------------------------ #


# ----------------------------------------------- #
# Settings Variables:
# ----------------------------------------------- #
DEBUG = bool(int(os.getenv("DJANGO_DEBUG", True)))
TEST_ENV = "test" in sys.argv

PROJECT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
)

ENVIRONMENT = "local"
SITE_URL = "http://localhost:8000"

# ------------------------------------------------------------ #


# ----------------------------------------------- #
# Applications:
# ----------------------------------------------- #
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.sites",
    "django.contrib.contenttypes",
    "django.contrib.humanize",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.contrib.admin",
    "authentication",
    "breeds"
]

THIRDPARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "sekizai",
    "sorl.thumbnail",
]

APPS = []

INSTALLED_APPS = DJANGO_APPS + THIRDPARTY_APPS + APPS

# ------------------------------------------------------------ #


# ----------------------------------------------- #
# Auth & Security:
# ----------------------------------------------- #
ALLOWED_HOSTS = ["*"]

SECRET_KEY = "e=ng@bcpsf$sm@_h-9o40&_dna&8jd%=gpq!2olu9n)yie+-d0"

# CSRF:
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SECURE = False

# Sessions:
SESSION_COOKIE_SECURE = True
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Authentication:
AUTH_USER_MODEL = "authentication.User"
AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.ModelBackend"]

# Rest framework:
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
}

# ------------------------------------------------------------ #


# ----------------------------------------------- #
# Caching:
# ----------------------------------------------- #
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    },
}

# ------------------------------------------------------------ #


# ----------------------------------------------- #
# Emails:
# ----------------------------------------------- #
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
TEST_EMAIL = "tech.test@thisisdare.com"

# ------------------------------------------------------------ #


# ----------------------------------------------- #
# Internationalisation:
# ----------------------------------------------- #
LANGUAGE_CODE = "en-gb"
TIME_ZONE = "UTC"

USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = (("en-gb", "GB - English"),)

# ------------------------------------------------------------ #


# ----------------------------------------------- #
# Logging:
# ----------------------------------------------- #
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
        },
    },
    "loggers": {"": {"handlers": ["console"], "propagate": True},},
}

# ------------------------------------------------------------ #


# ----------------------------------------------- #
# Media & Static:
# ----------------------------------------------- #
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(PROJECT_DIR, "static")
STATICFILES_DIRS = [os.path.join(PROJECT_DIR, "frontend", "dist")]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, "media")

UPLOADS_PATH = "uploads"

# Image Processing:
THUMBNAIL_DEBUG = True
THUMBNAIL_DUMMY = True
THUMBNAIL_QUALITY = 85
THUMBNAIL_URL_TIMEOUT = 30

# ------------------------------------------------------------ #


# ----------------------------------------------- #
# Middleware:
# ----------------------------------------------- #
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ------------------------------------------------------------ #


# ----------------------------------------------- #
# Storage & Cache:
# ----------------------------------------------- #
# Database:
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DATABASE_BACKEND"),
        "NAME": os.environ.get("MYSQL_DATABASE"),
        "USER": os.environ.get("MYSQL_USER"),
        "PASSWORD": os.environ.get("MYSQL_PASSWORD"),
        "HOST": "database",
        "PORT": os.environ.get("DATABASE_PORT"),
        "OPTIONS": {"autocommit": True, "charset": "utf8mb4", "use_pure": True},
    }
}

# Caches:
CACHES = {
    "default": {
        "BACKEND": "redis_cache.RedisCache",
        "LOCATION": "cache:{}".format(os.environ.get("REDIS_PORT")),
        "KEY_PREFIX": "python_django_test_local",
        "OPTIONS": {
            "CLIENT_CLASS": "redis_client.DefaultClient",
            "COMPRESSOR_CLASS": "redis_cache.compressors.ZLibCompressor",
            "COMPRESSOR_CLASS_KWARGS": {"level": 5},
            "DB": 1,
            "PARSER_CLASS": "redis.connection.HiredisParser",
            "SOCKET_TIMEOUT": 10,
            "SOCKET_CONNECT_TIMEOUT": 10,
        },
    }
}

# ------------------------------------------------------------ #


# ----------------------------------------------- #
# Templates:
# ----------------------------------------------- #
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_DIR, "frontend", "templates"),],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.request",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.contrib.messages.context_processors.messages",
                "sekizai.context_processors.sekizai",
                "application.context_processors.settings_variables",
            ]
        },
    },
]

# ------------------------------------------------------------ #


# ----------------------------------------------- #
# Sites & Misc Configs:
# ----------------------------------------------- #
SITE_ID = 1

ROOT_URLCONF = "application.urls"
WSGI_APPLICATION = "application.wsgi.application"
