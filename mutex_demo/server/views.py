from django.shortcuts import render
from .models import Logs
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import LogsSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render
from rest_framework.decorators import action
import json

class TransactionsTemplateHTMLRender(TemplateHTMLRenderer):
    def get_template_context(self, data, renderer_context):
        data = super().get_template_context(data, renderer_context)
        if not data:
            return {}
        else:
            return data
        

# class LogsViewSet(viewsets.ModelViewSet):
#     queryset = Logs.objects.all()
#     serializer_class = LogsSerializer
#     renderer_classes = [TemplateHTMLRenderer]


def create_logs(request, *args, **kwargs):
    try:
        template_name = 'index.html'
        serializer_class = LogsSerializer
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        client_ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META['REMOTE_ADDR']
        data = {"operation": "Created a new log", "user_type": "Client", "ip_address": client_ip}
        serializer = serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
        return render(context={}, template_name=template_name, content_type="application/json", request=request, status=status.HTTP_200_OK)
    except Exception as error:
        return render(context={error}, request=request, content_type="application/json", status=status.HTTP_500_INTERNAL_SERVER_ERROR)



def get_logs(request, *args, **kwargs):
    try:
        serializer_class = LogsSerializer
        queryset = Logs.objects.reverse()
        template_name = 'index.html'
        arr = []
        for index, ops in enumerate(queryset):
            data = {"operation": ops.operation, "address": ops.ip_address, "date": ops.date_created}
            arr.append(data)
            if index == 20: break
        print("\n\t arr: ", arr)
        # ==================================== ========================================= #
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        client_ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META['REMOTE_ADDR']
        data = {"operation": "Visited logs report page", "user_type": "Client", "ip_address": client_ip}
        serializer = serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
        return render(context={"arr": arr}, template_name=template_name, request=request, status=status.HTTP_200_OK)
    except Exception as error:
        return render(context={error}, request=request, content_type="application/json", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   

def home(request, *args, **kwargs):
    try:
        template_name = 'index.html'
        serializer_class = LogsSerializer
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        client_ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META['REMOTE_ADDR']
        data = {"operation": "Visited home", "user_type": "Client", "ip_address": client_ip}
        serializer = serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return render(context={"data": data}, template_name=template_name, request=request, status=status.HTTP_200_OK)
    except Exception as error:
        return render(context={"data": error}, request=request, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    