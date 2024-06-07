import environ

from django.utils.translation import gettext_lazy as _
from pathlib import Path

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = "zi6e#u)51eu)2@)jhz0!suj6us0_j(z!qv(-n)so(@7#3%rys#"

DJANGO_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

CUSTOM_APPS = [
    "theme",
    "apps.common",
    "apps.about",
    "apps.kurash",
    "apps.competitions",
    "apps.events",
    "apps.gallery",
]

THIRD_PARTY_APPS = [
    "rosetta",
    "tailwind",
    "django_browser_reload",
    "ckeditor",
    "modeltranslation",
    "sorl.thumbnail",
]

INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # other middlewares
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "core.middleware.ErrorHandlerMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "core.wsgi.application"

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

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

TIME_ZONE = "Asia/Tashkent"

USE_L10N = True
USE_I18N = True
USE_TZ = True

LANGUAGE_CODE = "en"
LANGUAGES = (
    ("ru", _("Russian")),
    ("uz", _("Uzbek")),
    ("en", _("English")),
)
LOCALE_PATHS = (BASE_DIR / "locale/",)

STATIC_URL = "static/"
STATICFILES_DIRS = (BASE_DIR / "staticfiles",)
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

TAILWIND_APP_NAME = "theme"
INTERNAL_IPS = [
    "127.0.0.1",
]
NPM_BIN_PATH = env.str("NPM_BIN_PATH")

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "full",
        "width": "auto",
        "height": 800,
    },
}

MODELTRANSLATION_LANGUAGES = ("ru", "uz", "en")
