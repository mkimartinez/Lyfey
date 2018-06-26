from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
	class Meta:
		model=Job
		# fields=('title','location','salary','company-name')
		fields = '__all__'