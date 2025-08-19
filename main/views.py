from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def home(request):
    form = ContactForm()

    # ✅ Updated services list
    services = [
        {"title": "Towing", "desc": "24/7 towing service for all vehicle types.", "image": "images/Towing.png"},
        {"title": "Jump Start", "desc": "Quick battery jump start and roadside assistance.", "image": "images/jumpstart.png"},
        {"title": "Lockout Service", "desc": "Locked out? We’ll get you back inside.", "image": "images/Lockedout.png"},
        {"title": "Battery Service", "desc": "On-site battery replacement and diagnostics.", "image": "images/battery.png"},
        {"title": "Fuel Delivery", "desc": "Ran out of fuel? We deliver directly to your location.", "image": "images/fuel.png"},
        {"title": "Motorcycle Towing", "desc": "Safe and secure towing for motorcycles.", "image": "images/motorcycle.png"},
    ]

    # ✅ Added service areas list
    areas = [
        "Al Talaa",
        "Al Rafaa",
        "Al Darari",
        "Al Tarfa",
        "Al Yash",
        "Muwaileh Commercial",
        "Al Swaihat",
        "Al Zahia",
        "Al Juraina",
        "University City",
        "Al Noaf",
        "Hay Hoshi",
        "Al Ruqa Al Hamra",
        "Al Qarayen",
        "Al Rahmania",
    ]

    return render(request, "home.html", {"form": form, "services": services, "areas": areas})


def contact_submit(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        # ✅ Same service & area lists here so errors still render correctly
        services = [
            {"title": "Towing", "desc": "24/7 towing service for all vehicle types.", "image": "images/service1.png"},
            {"title": "Jump Start", "desc": "Quick battery jump start and roadside assistance.", "image": "images/service2.png"},
            {"title": "Lockout Service", "desc": "Locked out? We’ll get you back inside.", "image": "images/service3.png"},
            {"title": "Battery Service", "desc": "On-site battery replacement and diagnostics.", "image": "images/battery.png"},
            {"title": "Fuel Delivery", "desc": "Ran out of fuel? We deliver directly to your location.", "image": "images/fuel.png"},
            {"title": "Motorcycle Towing", "desc": "Safe and secure towing for motorcycles.", "image": "images/motorcycle.png"},
        ]

        areas = [
            "Al Talaa",
            "Al Rafaa",
            "Al Darari",
            "Al Tarfa",
            "Al Yash",
            "Muwaileh Commercial",
            "Al Swaihat",
            "Al Zahia",
            "Al Juraina",
            "University City",
            "Al Noaf",
            "Hay Hoshi",
            "Al Ruqa Al Hamra",
            "Al Qarayen",
            "Al Rahmania",
        ]

        if form.is_valid():
            # TODO: Implement email sending or saving to database
            messages.success(request, "✅ Your message has been sent successfully!")
            return redirect("home")
        else:
            messages.error(request, "⚠️ Please correct the errors below.")
            return render(request, "home.html", {"form": form, "services": services, "areas": areas})

    return redirect("home")
