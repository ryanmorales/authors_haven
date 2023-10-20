from .base import * #noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = "3DsRqctGOzcXDDRFFaqY98cxT-aP6Ilb8EFuKRhMK8HVZwPy7BI"
SECRET_KEY = env(
    "DJANGO_SECRET_KEY", 
    default="3DsRqctGOzcXDDRFFaqY98cxT-aP6Ilb8EFuKRhMK8HVZwPy7BI",
)


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

