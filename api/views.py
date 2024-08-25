from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from .gemini import AIMatchmake
import requests

class UserView(APIView):
    def get(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                # Extract the token from the header (assuming it's a Bearer token)
                token = auth_header.split(' ')[1]
                user_id = RequestUserIf(token)

                # Retrieve the user from the database
                user, created = User.objects.get_or_create(id=user_id)

                serializer = UserSerializer(user)
                return Response({"message": "Token received", "user": serializer.data})

            except User.DoesNotExist:
                return Response({"message": "Invalid user"}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "No token provided"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                # Extract the token from the header (assuming it's a Bearer token)
                token = auth_header.split(' ')[1]
                user_id = RequestUserIf(token)

                # Retrieve the user from the database
                user = User.objects.get(id=user_id)

                # Update the user data
                serializer = UserSerializer(user, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message": "User updated successfully", "user": serializer.data})
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            except User.DoesNotExist:
                return Response({"message": "Invalid user"}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "No token provided"}, status=status.HTTP_400_BAD_REQUEST)

def RequestUserIf(accessToken):
    url = "https://kapi.kakao.com/v1/user/access_token_info"
    headers = {
        'Authorization': f"Bearer {accessToken}",
        'Content-Type': 'application/json'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError if the response code was unsuccessful
        
        # Extract the user ID from the response
        user_data = response.json()
        user_id = user_data.get('id')
        if not user_id:
            raise ValueError("User ID not found in the response")

        return user_id

    except requests.exceptions.HTTPError as errh:
        raise ValueError(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        raise ValueError(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        raise ValueError(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        raise ValueError(f"Something went wrong: {err}")