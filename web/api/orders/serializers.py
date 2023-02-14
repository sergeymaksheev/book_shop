from rest_framework import serializers
from orders.models import Order, OrderDetail
from catalog.models import Book
from rest_framework.exceptions import ValidationError
        



class BooksToOrderSerializer(serializers.Serializer):
    book_id = serializers.IntegerField(min_value=1)
    quantity = serializers.IntegerField(min_value=0)
    

class OrderDataSerializer(serializers.Serializer):
    order_data = BooksToOrderSerializer(many=True)


class OrderResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def validate(self, data):
        for order_item in self.context['order']['order_data']:
            try:
                id = order_item['book_id']
                quantity = order_item['quantity']
                book = Book.objects.get(pk=id)

                if book.therestofthebook.quantity < quantity:
                    raise ValidationError(
                        f'В остатках недостаточно книги {book.title} для заказа в количестве {quantity}!'
                    )    
            except Book.DoesNotExist:
                raise ValidationError(
                    f'Книги с id {id} не существует!'
                )     
        
        return data

    def create(self, validated_data):
        created_order = Order.objects.create(user=self.context['user'])
        created_order.save()
        order_detail = []

        for order_item in self.context['order']['order_data']: 
            quantity = order_item['quantity']
            try:
                book = Book.objects.get(pk=order_item['book_id'])
                order_detail.append(
                    OrderDetail(
                        order_id = created_order.id,
                        book_id=book.id,
                        quantity=quantity,
                        price_for_quantity=quantity * book.price
                    )
                )
            except Book.DoesNotExist:
                raise ValidationError(
                    f"Книги с id {order_item['book_id']} не существует!"
                )
        
        OrderDetail.objects.bulk_create(order_detail, batch_size=100)

        return created_order

class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = '__all__'
        


class OrderListSerializer(serializers.ModelSerializer):
    order_detail = OrderDetailSerializer(many=True, read_only=True)
    total_price = serializers.FloatField()

    class Meta:
        model = Order
        fields = ('id', 'user', 'status', 'is_paid', 'created_at', 'updated_at', 'order_detail', 'total_price')


class OrderStatusSerializer(serializers.ModelSerializer):
    order_detail = OrderDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'status', 'created_at', 'updated_at', 'order_detail')


class OrderPaidSerializer(serializers.ModelSerializer):
    order_detail = OrderDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'is_paid', 'status', 'created_at', 'updated_at', 'order_detail')
        read_only_fields = ('status',)

    def update(self, instance, validated_data):

        instance.is_paid = validated_data.get('is_paid', instance.is_paid)
        if instance.is_paid == True:
            instance.status = '2'
        instance.save()
        return instance
