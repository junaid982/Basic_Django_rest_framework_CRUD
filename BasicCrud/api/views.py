from django.shortcuts import render

from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import StudentSerializer
from .models import StudentModel
# Create your views here.


class Crudapi_view(APIView):
    
    def post(self , request):

        data = request.data
        # print(data)

        serializer = StudentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()

            return Response({'msg':"Successfully Data stored"} , status= status.HTTP_200_OK)

        return  Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

        
    

    def get(self , request):

        id = request.data.get("id" , None)

        if id:
            try:
                student_data = StudentModel.objects.get(id = id) 
                serializer = StudentSerializer(student_data )
                return Response(serializer.data , status= status.HTTP_200_OK)
            except:
                return Response({'error' : "Data Does not exists "} , status=status.HTTP_404_NOT_FOUND)


        student_data = StudentModel.objects.all()

        serializer = StudentSerializer(student_data , many = True)
        return Response(serializer.data , status= status.HTTP_200_OK)



    def patch(self , request):
        
        new_data = request.data
        id =  request.data.get('id' , None)
        

        if id:
            try:
                student_data = StudentModel.objects.get(id = id)
                serializer = StudentSerializer(student_data ,new_data , partial = True )
                if serializer.is_valid():
                    serializer.save()

                    return Response(serializer.data , status=status.HTTP_200_OK)

            except:
                return Response({'error' : "Data does not exists "} , status= status.HTTP_404_NOT_FOUND)

        return Response({'error':"Student Identification Fail"} , status=status.HTTP_400_BAD_REQUEST)

    
    
    def delete(self , request):

        id = request.data.get('id' , None)

        if id:
            
            try:
                student_data = StudentModel.objects.get(id = id)
                student_data.delete()

                return Response({'success':"Successfully Data Delete"}, status=status.HTTP_200_OK)
            
            except:
                return Response({'error' : "Data does not exists "} , status= status.HTTP_404_NOT_FOUND)


        
        return Response({'error':"Student Identification Fail"} , status=status.HTTP_400_BAD_REQUEST)


