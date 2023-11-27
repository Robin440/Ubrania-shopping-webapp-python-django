from django.db import models



class Customer(models.Model):
    password = models.CharField(max_length=128, verbose_name='password')
    last_login = models.DateTimeField(blank=True, null=True, verbose_name='last login')
    is_superuser = models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')
    first_name = models.CharField(blank=True, max_length=150, verbose_name='first name')
    last_name = models.CharField(blank=True, max_length=150, verbose_name='last name')
    email = models.EmailField(blank=True, max_length=254, verbose_name='email address')
    is_staff = models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')
    is_active = models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='date joined')
    mobile = models.CharField(max_length=30)
    username = models.CharField(max_length=159, unique=True)
    dob = models.DateField()
    is_blocked = models.BooleanField(default=False, help_text='Indicates whether the user is blocked.')

    def __str__(self):
        return "%s %s %s %s %s %s" % (self.first_name, self.last_name, self.mobile, self.username, self.email, self.dob)
