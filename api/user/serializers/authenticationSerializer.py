from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class ObtainPairCustomSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(self,user):
        token = super().get_token(user)
        token['user']={
            'username':user.username,
            'email':user.email,
            'name':user.name,
            'last_name':user.last_name
        }
 
        return token


