from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import BookShelf
from .serializers import BookSerializer
import requests
from .utils import get_the_index_of_author
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class IceAndFireApi(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """show all books in local data base 
        Args:
            request (Http): it will hold the data
        Returns:
            response (json): data about all books
        """
        print("read all books", request.user)
        # import pdb; pdb.set_trace()
        data = BookShelf.objects.all()
            
        serializer = BookSerializer(data, many=True)
        response = {
            'status_code': 200,
            'status': "success",
            'data': serializer.data
        }
        return Response(response)

    def retrieve(self, request, pk=None):
        """This view show the details of a specific book
        # Args:
        #     pk (int): book id 
        #     request (Http): it will hold the data
        # Returns:
        #     response (json): data about the searched book
        # """

        id = pk
        obj = get_object_or_404(BookShelf, id=id)
        serializer = BookSerializer(obj)
        response = {
            "status_code": 200,
            "status": "success",
            "data": serializer.data
        }
        return Response(response)

    def create(self, request):
        """This view will add the book in local database
        Args:
            request (Http): it will hold the post data

        Returns:
            response (json): data about the added book
        """
        try:
            request.data['author'] = get_the_index_of_author(request)

            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print("serializer.save", serializer.data)
                response = {
                    'status_code': 201,
                    'status': "success",
                    'data': {"book": serializer.data}
                }
                return Response(response)
            return Response({"status": 404, 'message': "something went wrong while insertion !!"})
        except:
            return Response({"status": 404, 'message': "something went wrong while insertion !!"})

    def update(self, request, pk):
        """This view update the specific id book 

        Args:
            request (Http): it will hold the post data
            pk (int): book id 

        Returns:
            response (json): data about the updated book
        """
        try:
            update_obj = BookShelf.objects.get(id=pk)
            book_name = update_obj.name
            if "author" in request.data:
                request.data['author'] = get_the_index_of_author(request)

            # set partial=True to update a data partially
            serializer = BookSerializer(update_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                response = {
                    'status_code': 201,
                    'status': "success",
                    'message': f"The book {book_name} was Updated successfully",
                    'data': serializer.data
                }
                return Response(response)
            return Response({"status": 400, 'message': "somrthing went wrong while updation !!"})
        except:
            return Response({'status': 404, 'message': "somrthing went wrong while updation !!"})

    def partial_update(self, request, pk):
        """This view update the specific id book 

        Args:
            request (Http): it will hold the post data
            pk (int): book id 

        Returns:
            response (json): data about the updated book
        """
        id = pk
        try:
            update_obj = BookShelf.objects.get(id=id)
            book_name = update_obj.name
            if "author" in request.data:
                request.data['author'] = get_the_index_of_author(request)

            # set partial=True to update a data partially
            serializer = BookSerializer(
                update_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response = {
                    'status_code': 201,
                    'status': "success",
                    'message': f"The book {book_name} was Updated successfully",
                    'data': serializer.data
                }
                return Response(response)
            return Response({"status": 400, 'message': "somrthing went wrong while updation !!"})
        except:
            return Response({'status': 404, 'message': "somrthing went wrong while updation !!"})

    def destroy(self, request, pk):
        """This view will delete the specific id book
        Args:
            request (Http): it will hold the post data
            id (int): book id 

        Returns:
            response (json): data about the deleted book
        """
        try:
            id = pk
            obj = BookShelf.objects.get(id=id)
            book_name = obj.name
            obj.delete()
            response = {
                'status_code': 204,
                'status': "success",
                'message': f"The book {book_name} was deleted successfully",
                'data': []
            }
            return Response(response)
        except:
            return Response({'status': 404, 'message': "somrthing went wrong while deletion !!"})


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
