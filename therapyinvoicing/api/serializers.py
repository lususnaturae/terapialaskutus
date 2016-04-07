from rest_framework import serializers
from rest_framework.serializers import ReadOnlyField


class MonthlyRevenueSerializer(serializers.Serializer):
    year = ReadOnlyField()
    month = ReadOnlyField()
    customerRevenue = ReadOnlyField()
    kelaRevenue = ReadOnlyField()




