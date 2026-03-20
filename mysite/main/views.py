from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main import serializers


class HelloAPIView(APIView):
    # Test API View
    serializer_class = serializers.HelloSerializer
    def get(self,request,format=None):
        
        # return a list of APIView features
        an_apiview = [
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})
    
    def post(self,request):
        # Tao mot serializer instance va truyen du lieu tu request vao de validate
        serializer = self.serializer_class(data=request.data)
        # Neu du lieu hop le, lay ten tu validated_data va tra ve message chao hoi
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk=None):
        # Cap nhat mot object, chi su dung put de cap nhat tat ca cac truong cua object
        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
        # Cap nhat mot object, chi su dung patch de cap nhat mot so truong cua object
        return Response({'method':'PATCH'})
    
    def delete(self,request,pk=None):
        # Xoa mot object
        return Response({'method':'DELETE'})
        