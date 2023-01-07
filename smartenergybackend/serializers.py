## @package urls
#  Contem o ficheiro com os serializadores. Um serializador permite mapear e verificar pedidos a objectos de modelos. Neste caso,
# o User do Django e o Group do Django
# 
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate

# Serializers define the API representation.
# Serializador de um group
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # O modelo do serializador e o group
        model = Group
        # Capos da base de dados que serao retornados
        fields = ['pk','url','name']

# Serializers define the API representation.
# Serializador de um user Django
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # O modelo do serializador e o User
        model = User
        # Campos da base de dados que serao retornados
        fields = ['pk','url', 'username', 'email', 'is_staff', 'groups']
        

# Serializador do login
# Permite receber dois campos, username e password, verifica na base de dados se batem certo. Se sim, marca o utilizador como autenticado e de seguida pode
# aceder aos servicos que requerem autenticacao        
class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """
    # Campo de username (string)
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    # Campo de password (string)
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    # Funcao de validacao do pedido
    # Se nao validar, retorna uma excecao
    # Se validar, retorna o objecto que identifica o utilizador
    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs