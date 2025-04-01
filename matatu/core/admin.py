from django.contrib import admin
from .models import User, Matatu, Driver, Tout, Payment, Expense, Maintenance, Route

admin.site.register(User)
admin.site.register(Matatu)
admin.site.register(Driver)
admin.site.register(Tout)
admin.site.register(Payment)
admin.site.register(Expense)
admin.site.register(Maintenance)
admin.site.register(Route)
