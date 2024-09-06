from rest_framework import serializers
from gk_app.models import OTP,registration,User

class RegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = registration
        fields = ('id','userName','mobileNo','password','aadharNo','native','roleId')

        def create(self, validated_Data):
            username = validated_Data.get('userName')
            mobileNo = validated_Data.get('mobileNo')
            password = validated_Data.get('password')
            aadharNo = validated_Data.get('aadharNo')
            native = validated_Data.get('native')
            roleId = validated_Data.get('roleId')

            admin = registration.objects.create(
                userName = username,
                mobileNo = mobileNo,
                password = password,
                aadharNo = aadharNo,
                native = native,
                roleId = roleId
            )

            return admin
            
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = '__all__'
