from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User, Notes, Attachment


class RegistrationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CreateNoteSerializer(ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'


class AttachNoteSerializer(ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'


class ListNotesSerializer(ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'


class UpdateNotesSerializer(ModelSerializer):
    class Meta:
        model = Notes
        fields = ['text']
