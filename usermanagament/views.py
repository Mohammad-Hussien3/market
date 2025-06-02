from usermanagament.models import Admin
from rest_framework.views import APIView, Response, status

class UpdatePassword(APIView):

    def put(self, request):
        data = request.data
        old_password = data['old_password']
        new_password = data['new_password']
        if Admin.admin_password == old_password or Admin.sub_admin_password == old_password:
            if Admin.admin_password == old_password:
                Admin.admin_password = new_password
                Admin.save()
            else:
                Admin.sub_admin_password = new_password
                Admin.save()
            
            return Response({'success':'success'}, status=status.HTTP_200_OK)
        
        else:
            return Response({'error':'error'}, status=status.HTTP_404_NOT_FOUND)