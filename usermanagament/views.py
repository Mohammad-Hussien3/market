from usermanagament.models import Admin
from rest_framework.views import APIView
from usermanagament.serializers import AdminSerializer


# class UpdatePassword(APIView):

#     def post(self, request):
#         data = request.data
#         old_password = data['old_password']
#         new_password = data['new_password']
#         if Admin.admin_password == old_password or Admin.sub_admin_password == old_password:
            