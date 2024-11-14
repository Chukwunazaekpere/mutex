from django.shortcuts import render
from .models import Logs
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import LogsSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render
from rest_framework.decorators import action
from .forms import LogForms


def create_logs(request, *args, **kwargs):
    try:
        template_name = 'create-log.html'
        serializer_class = LogsSerializer
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        client_ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META['REMOTE_ADDR']
        new_form = LogForms()
        if request.method == "POST":
            print("\n\t POST: ", request.POST)
            # print("\n\t operation: ", request.POST['operation'])
            print("\n\t body: ", request.body)
            new_form_entry = LogForms(request.POST)
            if new_form_entry.is_valid():
                data = {"operation": f"Created a new log operation: {request.POST['operation']}", "user_type": "Client", "ip_address": client_ip}
                new_form_entry.save()
        else:
            data = {"operation": "Entering a new log", "user_type": "Client", "ip_address": client_ip}
            serializer = serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
        return render(context={"form": new_form}, template_name=template_name, request=request, status=status.HTTP_200_OK)
    except Exception as error:
        return render(context={error}, request=request, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



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
    