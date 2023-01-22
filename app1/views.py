from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from app1.models import Student
from app1.serializers import StudentSerializer

# Create your views here.
class StudentDetails(viewsets.ViewSet):
    def list(self, request):
        std = Student.objects.all()
        serializer = StudentSerializer(std, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        try:
            std = Student.objects.get(rn=pk)
        except Student.DoesNotExist:
            msg = {"msg":"Student Does not Exist"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(std)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        try:
            std = Student.objects.get(rn=pk)
        except Student.DoesNotExist:
            msg = {"msg":"Student Does not Exist"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(std, request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        try:
            std = Student.objects.get(rn=pk)
        except Student.DoesNotExist:
            msg = {"msg":"Student Does not Exist"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        std.delete()
        return Response({"msg":"Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
  