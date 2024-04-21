from django.http import HttpResponse, JsonResponse,HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Customer,Order
from .serializers import CustomerSerializer,OrderSerializer

@csrf_exempt
def customer_list(request):
    """
    List all cutomers, or create a new customer.
    """
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def customer_detail(request, pk):
    """
    Retrieve, update or delete a customer.
    """
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(customer, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


def hello_world_view(request):
    return HttpResponse("Hello, World!")

@csrf_exempt
def sms_callback(request):
    # Get the raw request body as bytes
    raw_body = request.body
    
    # Decode it to a string if needed
    raw_body_str = raw_body.decode('utf-8')  # Decoding from bytes to string, assuming UTF-8 encoding
    
    # Print the raw body to the console
    print(raw_body_str)
    
    # Optionally, return the raw body in the response for debugging purposes
    return HttpResponse(f"Received raw data: {raw_body_str}")