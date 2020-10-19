from django.shortcuts import render

from accounts.models import StaffUser
from accounts.views.utils import staff_login_required


@staff_login_required
def list_staff_user(request):
    title = 'Staff User List'
    queryset = StaffUser.objects.all()
    context = {
        'user': request.user,
        "object_list": queryset,
        "title": title,
    }
    return render(request, "user_list.html", context)
