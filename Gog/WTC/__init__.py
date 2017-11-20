from django.contrib import admin, auth

admin.default_app_config = 'WTC.admin.AdminConfig'
auth.default_app_config = 'WTC.admin.AuthConfig'
default_app_config = 'WTC.admin.WTCConfig'