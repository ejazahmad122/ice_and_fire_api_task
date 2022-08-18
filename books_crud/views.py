from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import BookShelf, Author
from .serializers import BookSerializer
import requests
from .utils import get_the_index_of_author


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
            'name' : result[0]['name'],
            'isbn' : result[0]['isbn'],
            'author' : result[0]['authors'],
            'country' : result[0]['country'],
            'number_of_pages' : result[0]['numberOfPages'],
            'publisher' : result[0]['publisher'],
            'release_date' : result[0]['released'],
        }
        response = {
            'status_code':200,
            'status':"success",
            'data':data
        }
    else:
        response = {
            'status_code':200,
            'status':"success",
            'message':'There is no such book here !!',
            'data': []
        }   
    return Response(response)

@api_view(['GET'])
def show_all_books(request):
    """show all books in local data base 
    Args:
        request (Http): it will hold the data
    Returns:
        response (json): data about all books
    """
    data = BookShelf.objects.all()
    serializer = BookSerializer(data, many=True)
    response = {
        'status_code':200,
        'status':"success",
        'data':serializer.data
    }
    return Response(response)

@api_view(['POST'])
def add_book(request):
    """This view will add the book in local database

    Args:
        request (Http): it will hold the post data

    Returns:
        response (json): data about the added book
    """
    try:
        request.data['author'] = get_the_index_of_author(request)

        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status_code':201,
                'status':"success",
                'data':{"book":serializer.data}
            }
            return Response(response)
        return Response({"status":404, 'message':"something went wrong while insertion !!"})
    except:
        return Response({"status":404, 'message':"something went wrong while insertion !!"})

@api_view(['POST'])
def delete_book(request, id):
    """This view will delete the specific id book

    Args:
        request (Http): it will hold the post data
        id (int): book id 

    Returns:
        response (json): data about the deleted book
    """
    try:
        obj = BookShelf.objects.get(id=id)
        book_name = obj.name
        if request.method == 'POST':
            obj.delete()
            response = {
                'status_code':204,
                'status':"success",
                'message':f"The book {book_name} was deleted successfully",
                'data':[]
            }
            return Response(response)
        return Response({'status':404, 'message':"somrthing went wrong while deletion !!"})
    except :
        return Response({'status':404, 'message':"somrthing went wrong while deletion !!"})

@api_view(['POST'])
def update_book(request, id):
    """This view update the specific id book 

    Args:
        request (Http): it will hold the post data
        id (int): book id 

    Returns:
        response (json): data about the updated book
    """
    try:
        update_obj = BookShelf.objects.get(id=id)
        book_name = update_obj.name
        if "author" in request.data:
            request.data['author'] = get_the_index_of_author(request)
                
        serializer = BookSerializer(update_obj, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            response = {
                'status_code':201,
                'status':"success",
                'message':f"The book {book_name} was Updated successfully",
                'data':serializer.data
            }
            return Response(response)
        return Response({"status":400, 'message':"somrthing went wrong while updation !!"})
    except:
        return Response({'status':404, 'message':"somrthing went wrong while updation !!"})

@api_view(['GET'])
def show_specific_book(request, id):
    """This view show the details of a specific book
    Args:
        id (int): book id 
        request (Http): it will hold the data
    Returns:
        response (json): data about the searched book
    """
    obj = get_object_or_404(BookShelf, id=id)
    serializer = BookSerializer(obj)
    response = {
        "status_code":200,
        "status":"success",
        "data":serializer.data
    }
    return Response(response)