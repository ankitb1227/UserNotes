from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Notes, Attachment
from rest_framework.views import APIView
from NotesApp.serializer import RegistrationSerializer, CreateNoteSerializer, AttachNoteSerializer, ListNotesSerializer, \
    UpdateNotesSerializer
from rest_framework.response import Response
from .forms import Userform

class UserRegistration(APIView):
    def post(self, request):
        serialized_data = RegistrationSerializer(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return Response(serialized_data.data)


class CreateNotes(APIView):
    def post(self, request):
        serialized_data = CreateNoteSerializer(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return Response(serialized_data.data)


# class Attachment(APIView):
#     def post(self, request):
#         serialized_data = AttachNoteSerializer(data=request.data)
#         if serialized_data.is_valid(raise_exception=True):
#             serialized_data.save()
#             return Response(serialized_data.data)


def upload_image(request):
    # return HttpResponse("Image uploaded")
    if request.method == "POST":
        form = Userform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = Userform()
    img = Attachment.objects.all()
    return render(request, 'Index.html', {'img': img, 'form': form})



class ListNotes(APIView):
    def get(self, request):
        user = Notes.objects.all()
        serialized_data = ListNotesSerializer(user, many=True)
        return Response(serialized_data.data)


class UpdateNotes(APIView):
    def put(self, request, id):
        note = Notes.objects.filter(id=id)
        mydata = request.data
        if not note.exists():
            return Response({"data": "This id doesn't exists."})
        serialized_data = UpdateNotesSerializer(data=mydata, instance=note.first())
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return Response(serialized_data.data)

    def delete(self, request, id):
        note = Notes.objects.filter(id=id)
        if not note.exists():
            return Response({"data": "This id doesn't exists."})
        name = note.first().user.name
        note.first().delete()
        return Response({'Message': f"The note for {name} has been deleted"})
