from rest_framework import serializers 
from .models import Restaurant, Review

class ReviewSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Review # tell django which model to use
        fields = ['id', 'comment', 'restaurant'] # tell django which fields to include

class RestaurantSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    reviews = ReviewSerializer(source="restaurant", many=True)

    class Meta:
        model = Restaurant # tell django which model to use
        fields = ['id', 'name', 'address', 'image', 'price', 'cuisine', 'number', 'reviews'] # tell django which fields to include

    def create(self, validated_data):
        reviews_data = validated_data.pop('reviews')
        restaurant = Restaurant.objects.create(**validated_data)
        for review_data in reviews_data:
            Review.objects.create(**review_data, restaurant=restaurant)
        return restaurant

