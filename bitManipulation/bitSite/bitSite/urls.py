"""bitSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home
from pages.views import bin_to_hex
from pages.views import bin_to_oct
from pages.views import bin_to_dec
from pages.views import hex_to_bin
from pages.views import hex_to_oct
from pages.views import hex_to_dec
from pages.views import oct_to_hex
from pages.views import oct_to_bin
from pages.views import oct_to_dec
from pages.views import dec_to_hex
from pages.views import dec_to_oct
from pages.views import dec_to_bin
from pages.views import hex_calc
from pages.views import bin_calc
from pages.views import oct_calc
from pages.views import ieee_754_calc
from pages.views import ip_class
from pages.views import ones_compliment

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('bin_to_hex/', bin_to_hex ,name='bin_to_hex'),
    path('bin_to_oct/',bin_to_oct ,name='bin_to_oct'),
    path('bin_to_dec/',bin_to_dec ,name='bin_to_dec'),
    path('hex_to_bin/',hex_to_bin ,name='hex_to_bin'),
    path('hex_to_oct/',hex_to_oct ,name='hex_to_oct'),
    path('hex_to_dec/',hex_to_dec ,name='hex_to_dec'),
    path('oct_to_hex/',oct_to_hex ,name='oct_to_hex'),
    path('oct_to_bin/',oct_to_bin ,name='oct_to_bin'),
    path('oct_to_dec/',oct_to_dec ,name='oct_to_dec'),
    path('dec_to_hex/',dec_to_hex ,name='dec_to_hex'),
    path('dec_to_oct/',dec_to_oct ,name='dec_to_oct'),
    path('dec_to_bin/',dec_to_bin ,name='dec_to_bin'),
    path('hex_calc/',hex_calc ,name='hex_calc'),
    path('bin_calc/',bin_calc ,name='bin_calc'),
    path('oct_calc/',oct_calc ,name='oct_calc'),
    path('ieee_754/',ieee_754_calc ,name='ieee_754'),
    path('ip_class/',ip_class ,name='ip_class'),
    path('ones_compliment/',ones_compliment ,name='ones_compliment'),


    path('admin/', admin.site.urls),
]
