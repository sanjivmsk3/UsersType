from django.contrib import admin
from app.models import User, Post, Categories, BookAppointment, TimeSchedule

# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Categories)
admin.site.register(TimeSchedule)
admin.site.register(BookAppointment)
