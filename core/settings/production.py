from core.settings.base import *

ALLOWED_HOSTS = ["abkk-org.dev-space.uz"]

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.str("DB_PASS"),
        "HOST": env.str("DB_HOST"),
        "PORT": env.str("DB_PORT"),
    }
}

CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ["https://abkk-org.dev-space.uz"]

TELEGRAM_CHAT_ID = env.str("TELEGRAM_CHAT_ID")
TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN")
