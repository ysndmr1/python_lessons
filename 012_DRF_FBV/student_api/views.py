from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def home(request):
    return Response(
        {
            'message': 'Hello World'
        }
    )


# -------------------------------------------------------------------
'''
    HTTP Request Types:
        GET -> Public verilerdir. Listeleme/Görüntüleme işlemlerinde kullanılır.
        POST -> Private verilerdir. Kayıt oluşturma işlemlerinde kullanılır. (ID'ye ihtiyaç duymaz.)
        * PUT -> Kayıt güncelleme işlemlerinde kullanılır. (Veri bir bütün olarak güncellenir.) (ID'ye ihtiyaç duyar.)
        * PATCH -> Kayıt güncelleme işlemlerinde kullanılır. (Verinin sadece ilgili kısmı güncellenir.) (ID'ye ihtiyaç duyar.)
        * DELETE -> Kayıt silme işlemlerinde kullanılır. (ID'ye ihtiyaç duyar.)
'''
# -------------------------------------------------------------------
# StudentSerializers Tüm Kayıtlar Görüntüleme:


@api_view(['GET'])  # Default: ['GET']
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(instance=students, many=True)
    # print(dir(serializer))
    # print(serializer.data)
    return Response(serializer.data)

# -------------------------------------------------------------------
# StudentSerializers Yeni Kayıt Ekleme:

# HTTP Status Codes:
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status


@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Created Successfully"
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            "message": "Data not validated",
            "data": serializer.data
        }, status=status.HTTP_400_BAD_REQUEST)


# -------------------------------------------------------------------
# StudentSerializers Tek Kayıt Görüntüleme:


@api_view(['GET'])
def student_detail(request, pk):
    # student = Student.objects.get(id=pk)
    student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(instance=student)
    return Response(serializer.data)


@api_view(['PUT'])
def student_update(request, pk):
    student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Created Successfully"
        }, status=status.HTTP_202_ACCEPTED)
    else:
        return Response({
            "message": "Data not validated",
            "data": serializer.data
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def student_delete(request, pk):
    student = get_object_or_404(Student, id=pk)
    student.delete()
    return Response({
        "message": "Deleted Successfully"
    }, status=status.HTTP_204_NO_CONTENT)

# ---------------------------------------------------------------
# ---------------------------------------------------------------
# Benzer Fonksiyonlari Birlestirme


@api_view(['GET', 'POST'])
def student_list_create(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    else:
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Created Successfully"
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "message": "Data not validated",
                "data": serializer.data
            }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail_update_delete(request, pk):

    student = get_object_or_404(Student, id=pk)

    match request.method:
        case 'GET':
            # Tek kayıt görüntüle:
            serializer = StudentSerializer(instance=student)
            return Response(serializer.data)

        case 'PUT':
            # Tek kayıt güncelle:
            serializer = StudentSerializer(instance=student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Updated Successfully"
                }, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({
                    "message": "Data not validated",
                    "data": serializer.data
                }, status=status.HTTP_400_BAD_REQUEST)

        case 'DELETE':
            # Tek kayıt sil:
            student.delete()
            return Response({
                "message": "Deleted Successfully"
            }, status=status.HTTP_204_NO_CONTENT)
