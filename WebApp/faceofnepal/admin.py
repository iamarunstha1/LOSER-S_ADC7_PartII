from django.contrib import admin
from .models import Freelancer
from .models import Visitor
from .models import Payment
from .models import Business
from .models import Administrator



# Register your models here.
admin.site.register(Freelancer)
admin.site.register(Visitor)
admin.site.register(Payment)
admin.site.register(Business)
admin.site.register(Administrator)



