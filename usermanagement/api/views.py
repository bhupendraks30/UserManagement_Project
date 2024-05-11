from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

# Create your views here.
class UserRegister(APIView):
    
    def post(self,request):
        user_count = User.objects.all().filter(email=request.data['email']).count()
       
        if(user_count>0):
            return Response({'error':'002','message':'User exist'})
        else:
            result=User.objects.create(
                name = request.data['name'],
                email= request.data['email'],
                password =request.data['password']
            ).save()
            final_count = User.objects.filter(email=request.data['email']).count()
            if final_count > user_count:
                print("User created zsuccessfully!")
                return Response({'error':'000','message':'register successful'})
            else:
                print("User with this email already exists.")
                return Response({'error':'001','message':'register unsuccessful'})
    
class ShowUsers(APIView):
    def get(self,request):
        user = User.objects.all().values()
        return Response({(user)})

class DeleteUser(APIView):
    def post(self,request):
        User.objects.all().filter(email=request.data['email']).delete()
        User.save(self)
        return Response({'status':'success'})

class LoginUser(APIView):
    def post(self,request):
        count = User.objects.filter(email=request.data.get('email')).count()
        if count == 1:
            try:
                user = User.objects.get(email=request.data.get('email'), password=request.data.get('password'))
                user_data = {'id': user.id, 'name': user.name, 'email': user.email}
                return Response({'user': user_data, 'error': '200', 'message': 'login success'}) 
            except User.DoesNotExist:
                return Response({'error': '500', 'message': 'wrong credential'})
        else:
            return Response({'error': '400', 'message': 'User does not exist'})
        # count=User.objects.all().filter(email=request.data['email']).count()
        # if (count==1):
        #     try:
        #         count =User.objects.all().filter(email=request.data['email'],password=request.data['password']).count()                                   
        #         user = User.objects.get(email=request.data['email'], password=request.data['password'])
        #         user_data = {'id': user.id, 'name': user.name, 'email': user.email}
        #         return Response({'user':user_data,'error':'200','message':'login success'}) 
        #     except User.DoesNotExist:
        #             Response({'error':'200','message':'wrong credential'})                 
        # else:
        #     return Response({'error':'400','message':'User does not exist'})
class postImage(APIView):
    def post(self,request):
        # save=ImageFiles.objects.create(
        #     image=request.data['image']
        # )
        # save.save()
        image=request.data.get('image')
        myImage=ImageFiles(image=image)
        myImage.save()
        return Response({"successfu"})
    
class getImages(APIView):
    def get(self,request):
        images = ImageFiles.objects.all().values()
        return Response(images)