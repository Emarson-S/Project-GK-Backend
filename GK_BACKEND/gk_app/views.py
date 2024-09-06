from django.views.decorators.csrf import csrf_exempt
import jwt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from gk_app.models import registration,User,OTP
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
import base64
from rest_framework.exceptions import AuthenticationFailed
from gk_app.serializers import RegistrationSerializers, UserSerializer, OTPSerializer

# Views starts here

class MyPostView(APIView):
    permission_classes = [AllowAny]  # Use IsAuthenticated or another permission as appropriate

    def post(self, request, *args, **kwargs):
        parsedData = JSONParser().parse(request)
        print("parsedData", parsedData)
        print("mob", parsedData.get('mobileNo'))

        checkMobileExist = registration.objects.filter(mobileNo = parsedData.get('mobileNo')).values()
        print("Check", checkMobileExist)
        
        if checkMobileExist:
            response_data = {
                'statusCode': "1111",
                'message': "Mobile Number already Exists",
            }
            return Response(response_data,status=status.HTTP_200_OK)
        
        else:
            serializer = RegistrationSerializers(data=parsedData)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
           
                if user is not None:
                    user.save()
                    response_data = {
                        'statusCode': "0000",
                        'message': "Success",
                        "data": serializer.data 
                    }
                    return Response(response_data, status=status.HTTP_200_OK)
                    
class ProtectedView(APIView):
     def get(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None
        try:
            auth_type, auth_string = auth_header.split(' ')
            if auth_type.lower() != 'basic':
                raise AuthenticationFailed('Invalid authentication type')
            
            decoded_auth = base64.b64decode(auth_string).decode('utf-8')
            userPhone, otp = decoded_auth.split(':')
        except (ValueError, TypeError, base64.binascii.Error):
            raise AuthenticationFailed('Invalid Authorization header')

        user = User.objects.get(userPhone=userPhone)
        otpVal=OTP.objects.get(userPhone=user.userPhone)

        if userPhone == user.userPhone and otp == otpVal.otp:

            payload = {
                'user_id': user.id,
                'username': user.userName,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                'iat': datetime.datetime.utcnow(), 
            }
    
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    
            userData = {
                    'id': user.id,
                    'userName': user.userName,
                    'token' :token
                }
            
            return Response({"data":userData})