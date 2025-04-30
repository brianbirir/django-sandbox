"""To import the User model in Django, there are a few methods available, 
each suited to different scenarios
"""

# Using from django.contrib.auth.models import User
"""
This is the most straightforward way to import the default User model. 
It's suitable for standard projects where a custom user model is not required.
"""

from django.contrib.auth.models import User


# Using settings.AUTH_USER_MODEL
"""
This approach is recommended when referencing the User model in models,
especially when a custom user model might be used. 
It avoids circular import issues and makes the code adaptable to custom user models.
"""

from django.conf import settings
from django.db import models

class MyModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


# Using get_user_model()
"""
This method is best for reusable apps or when working outside of model definitions.
It dynamically retrieves the active User model, whether it's the default or a custom one.
"""

from django.contrib.auth import get_user_model

User = get_user_model()
# Now you can use the User model, e.g., User.objects.all()