from django.contrib import admin

# Register your models here.

# Board app 관련 추가
from .models import Board
admin.site.register(Board)

