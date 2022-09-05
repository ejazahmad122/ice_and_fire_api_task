from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import BookShelf
from .serializers import BookSerializer
from .utils import get_the_index_of_author
from rest_framework import generics
from rest_framework import status
import requests


class IceAndFireApi(generics.ListCreateAPIView):

    queryset = BookShelf.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        """Override the create method of CreateAPIView for adding the logic of author name change to relevant object

        Args:
            request (http): it will hold the post data

        Returns:
            http: response of the requested data
        """
        try:
            request.data['author'] = get_the_index_of_author(request)

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response({
                'status_code': status.HTTP_201_CREATED,
                'status': "success",
                'data': {"books": serializer.data},
            })
        except:
            return Response({"status": status.HTTP_400_BAD_REQUEST, 'message': "something went wrong while insertion !!"})


class IceAndFireApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookShelf.objects.all()
    serializer_class = BookSerializer

    def update(self, request, pk, *args, **kwargs):
        """Override the update method of UpdateAPIView for adding the logic of author name change to relevant object

        Args:
            request (http): it will hold the post data
            pk (int): book id

        Returns:
            http: response of the requested data
        """
        try:
            update_obj = BookShelf.objects.get(id=pk)
            book_name = update_obj.name
            if "author" in request.data:
                request.data['author'] = get_the_index_of_author(request)

            # set partial=True to update a data partially
            serializer = BookSerializer(
                update_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response = {
                    'status_code': status.HTTP_202_ACCEPTED,
                    'status': "success",
                    'message': f"The book {book_name} was Updated successfully",
                    'data': serializer.data
                }
                return Response(response)
            return Response({"status": status.HTTP_400_BAD_REQUEST, 'message': "somrthing went wrong while updation !!"})
        except:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': "somrthing went wrong while updation !!"})


@api_view(['GET'])
def ice_and_fire_api(request, name_of_book):
    """This view is used for getting data from ice and fire api of a specific searched book name
    Args:
        name_of_book (str): book name that is going to be seached
        request (Http): it will hold the post data

    Returns:
        response (json): data about the searched book name
    """
    url = f'https://www.anapioficeandfire.com/api/books/?name={name_of_book}'
    result = requests.get(url).json()
    if result:
        data = {
            'name': result[0]['name'],
            'isbn': result[0]['isbn'],
            'author': result[0]['authors'],
            'country': result[0]['country'],
            'number_of_pages': result[0]['numberOfPages'],
            'publisher': result[0]['publisher'],
            'release_date': result[0]['released'],
        }
        response = {
            'status_code': 200,
            'status': "success",
            'data': data
        }
    else:
        response = {
            'status_code': 200,
            'status': "success",
            'message': 'There is no such book here !!',
            'data': []
        }
    return Response(response)
