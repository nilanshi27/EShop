from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View

# for serving signup page using function in this we have to call multiple function
'''def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        return registerUser(request)
'''


# serving view page using class view in this we form funtion inside this only
class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST  # this shows all detail in dictionary form
        first_name = postData.get('firstname')  # extracts name from dictionary
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        value = {'first_name': first_name,
                 'last_name': last_name,
                 'phone': phone,
                 'email': email

                 }
        error_message = None
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        # this function will validate
        error_message = self.validateCustomer(customer)
        # saving data if our validation is done and if not then we will return same page again with error message
        if not error_message:
            customer.password = make_password(customer.password)  # used for hashing password
            customer.register()
            return redirect('homepage')  # this is used to redirect to homepage and name is also given in urls.py
        else:
            # to save the data which is already filled
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    # validation
    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "First  name requied!!"
        elif len(customer.first_name) < 4:
            error_message = "First name must be 4 character long"
        elif not customer.last_name:
            error_message = 'Last Name Required'
        elif len(customer.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email is already registered'
        return error_message
