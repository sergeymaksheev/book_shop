from rest_framework import serializers
from orders.models import Order, OrderDetail
from catalog.models import Book
from users.models import CustomUser
from rest_framework.exceptions import ValidationError
        
    
# class OrderSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     user = serializers.PrimaryKeyRelatedField(many=True, read_only=False)
#     book = serializers.PrimaryKeyRelatedField(many=True, read_only=False)

#     def create(self, validated_data):
#         return Order.objects.create(**validated_data)

    # def validate_title(self, value):
        
    #     if 'django' not in value.lower():
    #         raise serializers.ValidationError('dsdas')
    #     return value

class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
    
        model = OrderDetail
        fields = ['order_id', 'book_id', 'quantity']
        read_only_fields = ['total_price']

    def validate(self, data):
        if data['quantity'] < 1:
            raise ValidationError(
                'Вы не выбрали необходимое количество книг. Пожалуйста выберете необходимое количество'
            )
        return data

    def create(self, validated_data):
        total_price = (Book.objects.get(pk = 'order_id'))

    # def create(self, validated_data, context):
    #     books_id = [b['id'] for b in validated_data['books']]
    #     total_price = sum(Book.objects.filter(id__in=books_id).values_list('price'))
    #     order = Order.objects.create(user=context['user'], total_price=total_price)
    #     book_detail_data = []
    #     OrderDetail.objects.bulk_create(book_detail_data)


    # def get_total_price(self) -> int:
    #         total_price = self.quantity * 100 # Book['book_id'].price
    #         return total_price
    


