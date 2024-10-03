from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers

@api_view(['GET', 'POST'])
def getData(request):
    dictTest = {'records': 0, 'fetched': 0, 'message': 0}
    if request.method == 'POST':
        data = request.data
        print(data)
        dictTest['records'] = "Hello world"
        
    return Response(dictTest)