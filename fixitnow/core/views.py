from django.shortcuts import render,redirect,get_object_or_404
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "core/home.html")

@login_required
def service_request_list(request):
    categories = ServiceRequest.CATEGORY_CHOICES
    categorized_requests = {}

    for key, label in categories:
        categorized_requests[label] = ServiceRequest.objects.filter(category=key)

    return render(request, "core/service_request_list.html", {"categorized_requests": categorized_requests})
@login_required
def service_request_detail(request, request_id):
    request_obj = get_object_or_404(ServiceRequest, id=request_id)
    return render(request, "core/service_request_detail.html", {"request_obj": request_obj})
@login_required
def create_service_request(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("service_request_list")
    else:
        form = ServiceRequestForm()  

    return render(request, "core/service_request_form.html", {"form": form})
@login_required
def aboutus (request):
    return render(request,"core/about.html")
@login_required
def update_service_request(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    if request.method == "POST":
        form = ServiceRequestForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            return redirect("service_request_detail", pk=service_request.pk)
    else:
        form = ServiceRequestForm(instance=service_request)
    return render(request, "core/service_request_form.html", {"form": form, "update": True})
@login_required
def delete_service_request(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    if request.method == "POST":
        service_request.delete()
        return redirect("service_request_list")
    return render(request, "core/service_request_confirm_delete.html", {"service_request": service_request})