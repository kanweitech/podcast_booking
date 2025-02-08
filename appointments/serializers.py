from rest_framework import serializers
from .models import Appointment, Studio
from users.models import User

class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    studio = StudioSerializer(read_only=True)
    studio_id = serializers.PrimaryKeyRelatedField(
        queryset=Studio.objects.all(), 
        source='studio', 
        write_only=True
    )

    class Meta:
        model = Appointment
        fields = ['id', 'user', 'studio', 'studio_id', 'start_time', 'end_time', 'status']
        read_only_fields = ['user', 'status']

    def validate(self, data):
        start = data.get('start_time')
        end = data.get('end_time')
        studio = data.get('studio')

        if end <= start:
            raise serializers.ValidationError("End time must be after start time.")

        overlapping = Appointment.objects.filter(
            studio=studio,
            start_time__lt=end,
            end_time__gt=start
        )

        if self.instance:
            overlapping = overlapping.exclude(id=self.instance.id)

        if overlapping.exists():
            raise serializers.ValidationError("This studio is already booked for the selected time.")

        return data