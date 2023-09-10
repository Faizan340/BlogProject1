
# class VenturesCreateView(CreateView):
#     """
#     class to create ventures
#     """
#     model = Organisation
#     fields = '__all__'
#     template_name = "ventures/ventures_create.html"

#     def post(self, request,  *args, **kwargs):
#         # Getting the html form data from the request
#         name = request.POST.get('name')
#         image = request.FILES.get('image')
#         website = request.POST.get('website')
#         founder = request.POST.get('founder')
#         founded_on = request.POST.get('founded_on')
#         address = request.POST.get('address')
#         contact_no = request.POST.get('contact_no')
#         organisation_type = request.POST.get('organisation_type')
#         area_served = request.POST.get('area_served')
#         description = request.POST.get('description')

#         print(image)
#         print('33333333333333')

#         # Getting the data from the venture object
#         venture_data = {
#             "name": name,
#             "image": image,
#             "website": website,
#             "founder": founder,
#             "founded_on": founded_on,
#             "address": address,
#             "contact_no": contact_no,
#             "organisation_type": organisation_type,
#             "area_served": area_served,
#             "description": description
#         }
#         username = username1
#         password = password1

#         # Sending a POST request to the specified URL/API with the job data
#         url = "http://127.0.0.1:8000/venture/create_organisation/"
#         response = requests.post(url, data=venture_data, files={'image': image}, auth=(username, password))
#         print(response.json())
#         print('11111111111111111111')

#         # Checking the response status and handling accordingly
#         if response.status_code == 201:
#             return redirect("admindashboard:ventures")
#         else:
#             return HttpResponse("Error occurred while creating the organization.")


# class VenturesUpdateView(UpdateView):
#     """
#     class to update ventures
#     """
#     model = Organisation
#     fields = '__all__'
#     template_name = "ventures/ventures_update.html"

#     # function to get context data
#     def get_context_data(self,  *args, **kwargs):
#         context = super().get_context_data(**kwargs)
#         slug = self.kwargs['slug']  # Get the slug from the URL parameters
#         context['slug'] = slug
#         return context

#     def post(self, request,  *args, **kwargs):
#         slug = self.kwargs['slug']  # Get the slug from the URL parameters
#         # Getting the html form data from the request
#         name = request.POST.get('name')
#         image = request.FILES.get('image')
#         website = request.POST.get('website')
#         founder = request.POST.get('founder')
#         founded_on = request.POST.get('founded_on')
#         address = request.POST.get('address')
#         contact_no = request.POST.get('contact_no')
#         organisation_type = request.POST.get('organisation_type')
#         area_served = request.POST.get('area_served')
#         description = request.POST.get('description')

#         # Getting the data from the job object
#         venture_data = {
#             "name": name,
#             "image": image,
#             "website": website,
#             "founder": founder,
#             "founded_on": founded_on,
#             "address": address,
#             "contact_no": contact_no,
#             "organisation_type": organisation_type,
#             "area_served": area_served,
#             "description": description
#         }
#         username = username1
#         password = password1

#         # Sending a POST request to the specified URL/API with the job data
#         url = (f'http://127.0.0.1:8000/venture/update_organisation/{slug}')
#         response = requests.put(url, data=venture_data, files={'image': image}, auth=(username, password))
#         print(response)
#         print(response.json())
#         print('11111111111111111111')

#         # Checking the response status and handling accordingly
#         if response.status_code == 200:
#             return redirect("admindashboard:ventures")
#         else:
#             return HttpResponse("Error occurred while updating the organization.")
