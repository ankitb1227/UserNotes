from django.contrib import admin
from .models import User, Attachment, Notes
# Register your models here.

admin.site.register(User)
admin.site.register(Attachment)
admin.site.register(Notes)