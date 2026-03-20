from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    ## Serializer la ten goi cho test APIView
    
    name = serializers.CharField(max_length=10)
    # name la truong de nhap vao APIView, max_length la do dai toi da cua truong name
    