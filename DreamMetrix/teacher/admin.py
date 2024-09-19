from django.contrib import admin
from .models import TeacherProfile, ParentProfile  # Import both models

# Register TeacherProfile
@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'subjects_taught', 'is_active', 'created_at')
    search_fields = ('user__username', 'first_name', 'last_name', 'subjects_taught')
    list_filter = ('is_active', 'created_at')
# Register ParentProfile
admin.site.register(ParentProfile)
