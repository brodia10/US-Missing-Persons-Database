"""
Django settings for usmp project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

PROJECT_DIR = "usmp"

DEBUG = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY", "changeme!")


# APP CONFIGURATION
# ------------------------------------------------------------------------------

DJANGO_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.gis",
)

THIRD_PARTY_APPS = (
    "import_export",
    "letsencrypt",
    "auditlog",
)

# Apps specific for this project go here.
LOCAL_APPS = ("usmp.core",)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.admindocs.middleware.XViewMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "auditlog.middleware.AuditlogMiddleware",
]

ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": config("DB_NAME", "usmp"),
        "USER": config("DB_USER", "usmp"),
        "PASSWORD": config("DB_PASS", "usmp"),
        "HOST": config("DB_HOST", "localhost"),
        "PORT": config("DB_PORT", "5432"),
    }
}

# Static file Settings
# ------------------------------------------------------------------------------
# (CSS, JavaScript, Images)

STATIC_ROOT = BASE_DIR / PROJECT_DIR / "staticfiles"
STATIC_URL = "/static/"

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (BASE_DIR / PROJECT_DIR / "static",)

# Media #
MEDIA_ROOT = BASE_DIR / PROJECT_DIR / "media"
MEDIA_URL = "/media/"

# Password validation
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Email Settings
# ------------------------------------------------------------------------------

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = config("GMAIL_USER", "")
EMAIL_HOST_PASSWORD = config("GMAIL_PASSWORD", "")
EMAIL_USE_TLS = True


# Django-Jazzmin Admin Theme Configs
# ------------------------------------------------------------------------------

X_FRAME_OPTIONS = "SAMEORIGIN"

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "USMP",
    # Title on the brand, and login screen (19 chars max)
    # (defaults to current_admin_site.site_header if absent or None)
    "site_header": "USMP Admin Site",
    # square logo to use for your site, must be present in static files, used for favicon and brand on top left
    "site_logo": "",
    # Welcome text on the login screen
    "welcome_sign": "Login to administration portal",
    # Copyright on the footer
    "copyright": "",
    # The model admin to search from the search bar, search bar omitted if excluded
    # "search_model": "auth.User",
    # Field name on user model that contains avatar image
    "user_avatar": "auth.User",
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        # App with dropdown menu to all its models pages (Permissions checked against models)
        # {"app": "email_tool"},
        # {"app": "candidates"},
        # {"app": "document"},
        # external url that opens in a new window (Permissions can be added)
        # {
        #     "name": "Fidelis Site",
        #     "url": "https://fidelis-partners.com",
        #     "new_window": True,
        # },
        # {"name": "Latest ERP News", "url": "https://erpnews.com/", "new_window": True},
        # # model admin to link to (Permissions checked against model)
        # {"model": "auth.User"},
    ],
    #############
    # User Menu #
    #############
    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        # {
        #     "name": "Fidelis Site",
        #     "url": "https://fidelis-partners.com",
        #     "new_window": True,
        # },
        # {"name": "Latest ERP News", "url": "https://erpnews.com/", "new_window": True},
        {"model": "auth.user"},
    ],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": True,
    # # Hide these apps when generating side menu e.g (auth)
    # "hide_apps": [],
    # # Hide these models when generating side menu (e.g auth.user)
    # "hide_models": [],
    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": [
        "auditlog",
        "letsencrypt",
        "auth",
    ],
    # Custom links to append to app groups, keyed on app name
    # "custom_links": {
    #     "books": [{
    #         "name": "Make Messages",
    #         "url": "make_messages",
    #         "icon": "fas fa-comments",
    #         "permissions": ["books.view_book"]
    #     }]
    # },
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free
    # for a list of icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-user-friends",
        # "email_tool.customer": "fas fa-users",
        # "email_tool.emailbatch": "fas fa-mail-bulk",
        # "email_tool.emailmessage": "fas fa-envelope",
        # "email_tool.imageresource": "fas fa-images",
        # "candidates.candidate": "fas fa-briefcase",
        # "candidates.techstack": "fas fa-laptop-code",
        # "document.document": "fas fa-file-upload",
        "auditlog.logentry": "fas fa-file-alt",
        "letsencrypt.acmechallenge": "fas fa-key",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": True,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": "jazzmin_ui_tweaks.css",
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    # Add a language dropdown into the admin
    "language_chooser": False,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": True,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-navy navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success",
    },
}
