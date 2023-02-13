from django.shortcuts import render, get_object_or_404, redirect


from .models import UniversityCampus


def admin_console(request):
    campus = UniversityCampus.objects.all()
    return render(request, {'campus': campus})

