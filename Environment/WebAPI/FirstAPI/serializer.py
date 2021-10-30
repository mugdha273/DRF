from .models import Person
from rest_framework import serializers



class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields= '__all__'
        #fields = ("Name", "Age")
        
    