from rest_framework.serializers import ModelSerializer

from lms.models import Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["name"]


