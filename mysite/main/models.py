from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin , BaseUserManager


class UserProfileManager(BaseUserManager):
    # Quan ly user profile trong he thong
    def create_user(self,email,name,password=None):
        # tao user moi voi email va password
        if not email:
            raise ValueError('User must have an email address')
        
        email = self.normalize_email(email) # chuan hoa email
        user = self.model(email=email,name=name) # tao user moi voi email va name
        user.set_password(password) # dat password cho user
        user.save(using=self._db) # luu user vao database
        
        return user 
    
    def create_superuser(self,email,name,password):
        # tao superuser moi voi email va password
        user = self.create_user(email,name,password) # tao user moi voi email va name
        user.is_superuser = True # dat quyen superuser cho user
        user.is_staff = True # dat quyen staff cho user
        user.save(using=self._db) # luu user vao database
        
        return user
        
     

class UserProfile(AbstractBaseUser, PermissionsMixin):
    # Database models for users in the system 
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)# xac dinh profile co dc active hay chua 
    is_staff = models.BooleanField(default=False) # khong cho user su dung quyen admin
    
    
    objects = UserProfileManager() # quan ly user profile
    
    USERNAME_FIELD = 'email' # truong de dang nhap vao he thong
    REQUIRED_FIELDS = ['name'] # truong de tao user moi
    
    def get_full_name(self):
        # lay ten day du cua user
        return self.name
    
    def get_short_name(self):
        # lay ten ngan gon cua user
        return self.name
    
    def __str__(self):
        # tra ve chuoi de hien thi user
        return self.email
     
    
    


