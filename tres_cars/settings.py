import dj_database_url
from pathlib import Path
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY")

DVLA_API_KEY = os.environ.get("DVLA_API_KEY", "")
DVLA_REQUEST_SITE = os.environ.get("DVLA_REQUEST_SITE", "")
DEBUG = "DEVELOPMENT" in os.environ

if DEBUG:
    ALLOWED_HOSTS = ["127.0.0.1", "*"]
    CSRF_TRUSTED_ORIGINS = [
        "http://localhost",
        "http://127.0.0.1",
        "http://127.0.0.1:8000/",
        "https://127.0.0.1:22/",
        "https://tres-cars.onrender.com/",
        "https://trescars.s3.amazonaws.com/",
    ]
else:
    ALLOWED_HOSTS = ["tres-cars.onrender.com", "localhost", "127.0.0.1"]
    CSRF_TRUSTED_ORIGINS = [
        "http://127.0.0.1",
        "https://tres-cars.onrender.com/",
        "https://trescars.s3.amazonaws.com/",
    ]

# Add Render.com URL to allowed hosts
RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME", "")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "home",
    "vehicles",
    "bag",
    "checkout",
    "profiles",
    "management",
    "accessories",
    "mailer",
    "crispy_forms",
    "mathfilters",
    "storages",
]

CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "tres_cars.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, "templates", "allauth"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
                "bag.contexts.vehicle_bag_contents",
                "bag.contexts.bag_contents",
            ],
            "builtins": [
                "crispy_forms.templatetags.crispy_forms_tags",
                "crispy_forms.templatetags.crispy_forms_field",
            ],
        },
    },
]

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

SITE_ID = 1

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENNGTH = 4
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"

WSGI_APPLICATION = "tres_cars.wsgi.application"

if "DATABASE_URL" in os.environ:
    DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

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
LANGUAGE_CODE = "en-gb"

TIME_ZONE = "GMT"

USE_I18N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

if "USE_AWS" in os.environ:

    AWS_S3_OBJECT_PARAMETERS = {
        "Expires": "Thu, 31 Dec 2099 20:00:00 GMT",
        "CacheControl": "max-age=94608000",
    }

    AWS_STORAGE_BUCKET_NAME = "trescars"
    AWS_S3_REGION_NAME = "eu-central-1"
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.eu-central-1.amazonaws.com"

    STATICFILES_STORAGE = "custom_storages.StaticStorage"
    STATICFILES_LOCATION = "static"
    DEFAULT_FILE_STORAGE = "custom_storages.MediaStorage"
    MEDIAFILES_LOCATION = "media"

    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

if "DEVELOPMENT" in os.environ:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASS")
    DEFAULT_FROM_EMAIL = os.environ.get("EMAIL_HOST_USER")

DEFAULT_RECEIVING_EMAIL = os.environ.get("DEFAULT_RECEIVING_EMAIL")

STRIPE_PUBLIC_KEY = os.getenv("STRIPE_PUBLIC_KEY", "")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_WH_SECRET = os.getenv("STRIPE_WH_SECRET", "")
STRIPE_CURRENCY = "gbp"
