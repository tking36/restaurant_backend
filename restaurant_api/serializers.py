from rest_framework import serializers 
from .models import Restaurant, Review

class ReviewSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Review # tell django which model to use
        fields = ['id', 'comment', 'restaurant'] # tell django which fields to include

class RestaurantSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Restaurant # tell django which model to use
        fields = ['id', 'name', 'address', 'image', 'price', 'cuisine', 'number', 'reviews'] # tell django which fields to include

    def create(self, validated_data):
        reviews_data = validated_data.pop('reviews') # only reviews array with multiple comments gets popped off from validated_data which has everything (including restaurant info) and puts the reviews object into reviews_data
        restaurant = Restaurant.objects.create(**validated_data) # takes the remaining info of validated_data which is restaurant info and creates a new restaurant in restaurant table
        for review_data in reviews_data: # here we are looping through reviews_data since it is an array (aka dictionary) 
            Review.objects.create(**review_data, restaurant=restaurant) # for every review comment (array item) we create, we connect the restaurant info (that was just created above on line 18) in the 2nd parameter of the Review.create() above
        return restaurant # this should contain the whole thing - newly created restaurant with its reviews

    
