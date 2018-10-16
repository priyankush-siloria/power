from django.conf.urls import url
from .views import *

urlpatterns = [

		url(r'^$', HomePage.as_view(), name='homepage'),
		url(r'about_us', AboutUs.as_view(), name='aboutus'),
		url(r'how_it_works', Works.as_view(), name='howitworks'),
		url(r'contact_us', ContactUs.as_view(), name='contact_us'),
		url(r'userregistration', UserRgistration.as_view(), name='userregistration'),
		url(r'contractorregister', ContractorRegister.as_view(), name='contractorregister'),
		url(r'login', LoginView.as_view(), name='login'),
		url(r'register', RegisterView.as_view(), name='register'),
		url(r'cprofile', CprofileView.as_view(), name='cprofile'),
		url(r'editcontprofile', EditContractorProfile.as_view(), name='editcontprofile'),
		url(r'userprofile', UserProfileView.as_view(), name='userprofile'),
		url(r'adminsignup', AdminRegisterView.as_view(), name='adminsignup'),
		url(r'adminhomepage', AdminHomeView.as_view(), name='adminhomepage'),
		url(r'logout', LogoutView, name='logout'),
		    
]
