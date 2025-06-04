from usermanagament.models import Admin
from rest_framework.views import APIView, Response, status

class UpdatePassword(APIView):

    def patch(self, request):
        data = request.data
        old_password = data['old_password']
        new_password = data['new_password']
        admin = Admin.get_instance()
        if admin.admin_password == old_password or admin.sub_admin_password == old_password:
            if admin.admin_password == old_password:
                if new_password == admin.sub_admin_password:
                    return Response({'error':'error'}, status=status.HTTP_404_NOT_FOUND)
                admin.admin_password = new_password
                admin.save()
            else:
                if new_password == admin.admin_password:
                    return Response({'error':'error'}, status=status.HTTP_404_NOT_FOUND)
                admin.sub_admin_password = new_password
                admin.save()
            
            return Response({'success':'success'}, status=status.HTTP_200_OK)
        
        else:
            return Response({'error':'error'}, status=status.HTTP_404_NOT_FOUND)
        

class LogIn(APIView):

    def post(self, request):
        data = request.data
        password = data['password']
        admin = Admin.get_instance()
        if admin.admin_password == password:
            return Response({'status':'admin'}, status=status.HTTP_200_OK)
        elif admin.sub_admin_password == password:
            return Response({'status':'sub_admin'}, status=status.HTTP_200_OK)
        else:
            return Response({'status':'error'}, status=status.HTTP_404_NOT_FOUND)
