from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

"""
Both Static & Media storage classes created with the purpose of to avoid
overwriting existing static files with media files.
"""
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
    
class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION