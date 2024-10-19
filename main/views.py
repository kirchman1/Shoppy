from .serializers import ItemSerializer, OrderSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item, Order
from cloudipsp import Api, Checkout
import time


class ItemsPage(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class OrderAdd(APIView):
    def post(self, req):
        order = OrderSerializer(data=req.data)

        if order.is_valid():
            order.save()

            api = Api(merchant_id=1396424,
                      secret_key='test')
            checkout = Checkout(api=api)
            data = {
                "currency": "USD",
                "amount": int(req.data['sum']) * 100,
                "order_desc": "Payment",
                "order_id": str(time.time())
            }
            url = checkout.url(data).get('checkout_url')

            return Response({'result': 'Wait...', 'url': url})

        return Response({'result': 'Error'})

class ItemEdit(APIView):
    def put(self, req, *args, **kwargs):
        item = Item.objects.filter(slug=kwargs['slug']).first()

        item.image = req.data['image']
        item.title = req.data['title']
        item.desc = req.data['desc']
        item.price = req.data['price']

        item.save()

        return Response({'result': 'Done'})
