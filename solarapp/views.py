# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.contrib.auth.models import Group, User
from django.contrib import messages
from .models import *
from django.contrib.auth import login, authenticate, logout


# Create your views here.

def LogoutView(request):
	
	logout(request)
	return HttpResponseRedirect('login')



class HomePage(TemplateView):

	
	template_name ='index.html'

	def get(self, request, *args, **kwargs):
		
		return render(request, self.template_name,{})
		

class AboutUs(TemplateView):
	template_name ='about.html'
	def get(self, request, *args, **kwargs):
		
			return render(request, self.template_name,{})
	


class Works(TemplateView):
	template_name ='how-it-work.html'
	def get(self, request, *args, **kwargs):
		
			return render(request, self.template_name,{})
		

class ContactUs(TemplateView):
	template_name ='contact.html'

	def get(self, request, *args, **kwargs):
		
		
			return render(request, self.template_name,{})
	


class ContractorRegister(TemplateView):
	
	template_name ='contractorregister.html'
	def get(self, request, *args, **kwargs):
		
		return render(request, self.template_name,{})


	def post(self, request, *args, **kwargs):	
		
		
		first_name = self.request.POST.get('firstname')
		last_name = self.request.POST.get('lastname')
		email = self.request.POST.get('email')
		password1 = self.request.POST.get('password')
		password2 = self.request.POST.get('cpassword')
		contractor_address = self.request.POST.get('address1')
		contractor_zip_code = self.request.POST.get('zip')
		contractor_phone = self.request.POST.get('number')
		contractor_country = self.request.POST.get('country')
		company_name = self.request.POST.get('companyname')	
		about_company = self.request.POST.get('aboutcompany')
			
		contractor_state = self.request.POST.get('state')
		contractor_city = self.request.POST.get('city')
		fullname = first_name+' '+last_name
		print(fullname)
		
		
		try:
			user = User.objects.get(email=email)
			messages.error(request,'Already Registered')
			return HttpResponseRedirect('contractorregister')
		except User.DoesNotExist:
			if password1 and password2 and password1 != password2:
				messages.error(request,'password_mismatch!')
				return HttpResponseRedirect('contractorregister')

			user = User.objects.create_user(
				username=email,
				email=email,
				password=password1
			)

			user.first_name = first_name
			user.last_name = last_name
			user.is_active = True
			
			user.save()
			group, created  = Group.objects.get_or_create(name='ContractorGroup')
			group.user_set.add(user)

			contractorprofile = ContractorProfile.objects.create(
				
				user=user,
				name = fullname,
				address=contractor_address,
				companyname = company_name,
				aboutcompany = about_company,
				number = contractor_phone,
				city=contractor_city,
				state=contractor_state,
				country=contractor_country,
				zipcode=contractor_zip_code,
				
				
				)
			contractorprofile.save()
			return HttpResponseRedirect('login')

class UserRgistration (TemplateView):
	template_name ='userregistration.html'
	
	def get(self, request, *args, **kwargs):
		
		return render(request, self.template_name,{})


	def post(self, request, *args, **kwargs):	
		
		
		first_name = self.request.POST.get('firstname')
		last_name = self.request.POST.get('lastname')
		email = self.request.POST.get('email')
		password1 = self.request.POST.get('password')
		password2 = self.request.POST.get('cpassword')
		user_address = self.request.POST.get('address1')
		user_zip_code = self.request.POST.get('zip')
		user_phone = self.request.POST.get('number')
		user_country = self.request.POST.get('country')
		
		user_state = self.request.POST.get('state')
		user_city = self.request.POST.get('city')
	
		
		try:
			user = User.objects.get(email=email)
			messages.error(request,'Already Registered')
			return HttpResponseRedirect('userregistration')
		except User.DoesNotExist:
			if password1 and password2 and password1 != password2:
				messages.error(request,'password_mismatch!')
				return HttpResponseRedirect('userregistration')

			user = User.objects.create_user(
				username=email,
				email=email,
				password=password1
			)

			user.first_name = first_name
			user.last_name = last_name
			user.is_active = True
			
			user.save()
			group, created  = Group.objects.get_or_create(name='UserGroup')
			group.user_set.add(user)
			print(user)

			userprofile = UserProfile.objects.create(
				
				user=user,
				address=user_address,
				number = user_phone,
				city=user_city,
				state=user_state,
				country=user_country,
				zipcode=user_zip_code,
				
				
				)
			userprofile.save()
			return HttpResponseRedirect('login')
	


class LoginView (TemplateView):
	template_name ='login.html'
	
	def get(self, request, *args, **kwargs):

		
		return render(request, self.template_name,{})

	def post(self, request, *args, **kwargs):

		email = request.POST.get('email')
		print(email)
		password1 = request.POST.get('password')
		print(password1)

		try:
			user = User.objects.get(email=email)
			# user_first_name = user.firstname
			

		
			userauth = authenticate(username=user.email, password=password1)


			if userauth:

				login(request, user)

				if request.user.is_authenticated:


						users_in_group = Group.objects.get(name="UserGroup").user_set.all()
						if user in users_in_group:
					
							return HttpResponseRedirect('userprofile')

						#  user.is_staff:
						elif request.user.is_staff or request.user.is_superuser:


							return HttpResponseRedirect('adminhomepage')


						else:
							return HttpResponseRedirect('cprofile')
				else:
					return HttpResponseRedirect('login')
			
			else:
				messages.error(request,'Incorrect password  given.')
				return HttpResponseRedirect('login')
		except User.DoesNotExist:
			messages.error(request,'Incorrect email address given.')
			return HttpResponseRedirect('login')


class RegisterView (TemplateView):
	template_name ='registeration.html'
	
	def get(self, request, *args, **kwargs):
		
		return render(request, self.template_name,{})


class CprofileView (TemplateView):

	template_name ='cprofile.html'


	
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
		

			return render(request, self.template_name,{})
		else:
			return HttpResponseRedirect('login')



class UserProfileView (TemplateView):
	template_name ='userprofile.html'
	
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			

			return render(request, self.template_name,{})
		else:

			return HttpResponseRedirect('login')


class EditContractorProfile(TemplateView):
	template_name = 'editcontractorprofile.html'
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:

			user_id = request.user.id
			print(user_id)
			obj, obj1 = ContractorProfile.objects.get_or_create(user_id = user_id)
			name = obj.name
			companyname = obj.companyname
			about_company = obj.aboutcompany
			print("___________________________________________")
			print(about_company)
			address = obj.address
			number = obj.number
			city=obj.city
			state=obj.state
			country=obj.country
			zipcode=obj.zipcode


			return render(request, self.template_name,{'name':name,'company' : companyname, 'aboutcompany': about_company, 'address': address,'number': number, 'city':city,'state': state,'country':country,'zipcode':zipcode})
		else:
			return HttpResponseRedirect('login')

	def post(self, request, *args, **kwargs):
		user_id = request.user.id

		name = request.POST.get('name')
		address = request.POST.get('address')
		company = request.POST.get('company')
		aboutcompany = request.POST.get('aboutcompany')
		print(aboutcompany)
		number = request.POST.get('number')
		city = request.POST.get('city')
		state = request.POST.get('state')
		country = request.POST.get('country')
		zipcode = request.POST.get('zipcode')

		editinfo = ContractorProfile.objects.get(user_id = user_id)
		editinfo.name = name
		editinfo.address = address
		editinfo.companyname = company
		editinfo.aboutcompany = aboutcompany
		editinfo.number = number
		editinfo.city = city
		editinfo.state = state
		editinfo.country = country
		editinfo.zipcode = zipcode

			
		editinfo.save()

		return HttpResponseRedirect('cprofile')



class AdminRegisterView(TemplateView):
	template_name = 'admin/adminregister.html'
	def get(self, request, *args, **kwargs):
		

		return render(request, self.template_name,{})


	def post(self, request, *args, **kwargs):

		first_name = request.POST.get('firstname')
		last_name = request.POST.get('lastname')
		email = request.POST.get('email')
		password1 = request.POST.get('password')
		cpassword = request.POST.get('confirmpassword')


		
		try:
			user = User.objects.get(email=email)
			messages.error(request,'Already Registered, Try to login.')
			return HttpResponseRedirect('adminsignup')
		except User.DoesNotExist:
			if password1 and cpassword and password1 != cpassword:
				messages.error(request,'password_mismatch!')
				return HttpResponseRedirect('adminsignup')

			user = User.objects.create_user(
				username=email,
				email=email,
				password=password1
			)

			user.first_name = first_name
			user.last_name = last_name
			user.is_active = True
			user.is_staff = True
			
			user.save()

			return HttpResponseRedirect('login')


class AdminHomeView(TemplateView):
	template_name = 'admin/adminhome.html'
	def get(self, request, *args, **kwargs):

		if request.user.is_authenticated:

			allcontlist = ContractorProfile.objects.all().values()

			
			return render(request, self.template_name,{'data':allcontlist})
		else:

			return HttpResponseRedirect('login')