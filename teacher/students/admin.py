from django.contrib import admin
from .models import Articles, Memos, Recommendations


admin.site.register(Articles)
admin.site.register(Memos)
admin.site.register(Recommendations)
