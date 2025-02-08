from rest_framework import serializers

from .models import Student

# Model Serializers
class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only = True)    # Validation
    # Validators
    def start_with_s(value):
        if value[0].lower() !='s':
            raise serializers.ValidationError("Name Should Start from S!")
    name = serializers.CharField(validators = [start_with_s])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        # read_only_fields = ['name', 'roll']  # Validation
        # extra_kwargs = {'city':{'read_only':True}}   # Validation

# we can also used field, object level validation and validator with Model Serializers

    # Field Level Validation
    def validate_roll(self, value):
        if value >=200:
            raise serializers.ValidationError("Seats Are FULL!")
        return value
    
    # Object Level Validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'farhan' and ct.lower() != 'bangladesh':
            raise serializers.ValidationError("City must be Bangladesh")
        return data

# Regular Serializers

# Validators
# def start_with_s(value):
#     if value[0].lower() !='s':
#         raise serializers.ValidationError("Name Should Start from S!")

# class StudentSerializer(serializers.Serializer):
#     # id = serializers.IntegerField()
#     name = serializers.CharField(max_length=100, validators = [start_with_s])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)

#     def create(self, validate_data):
#         return Student.objects.create(**validate_data)
    
#     def update(self, instance, validated_data):
#         print(instance.name)
#         instance.name = validated_data.get('name', instance.name)
#         print(instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance
   
#     # Field Level Validation
#     def validate_roll(self, value):
#         if value >=200:
#             raise serializers.ValidationError("Seats Are FULL!")
#         return value
    
#     # Object Level Validation
#     def validate(self, data):
#         nm = data.get('name')
#         ct = data.get('city')
#         if nm.lower() == 'ahmad' and ct.lower() != 'mingora':
#             raise serializers.ValidationError("City must be Mingora")
#         return data