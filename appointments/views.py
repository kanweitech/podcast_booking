from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Appointment
from .serializers import AppointmentSerializer
#from rest_framework import permissions

from .permissions import IsAdminPermission  # Local import

class UserAppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Appointment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AdminAppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    #permission_classes = [permissions.IsAdminPermission]
    permission_classes = [IsAdminPermission]  #Use your custom class
