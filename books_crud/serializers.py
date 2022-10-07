from rest_framework import serializers
from .models import BookShelf


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.SerializerMethodField()

    class Meta:
        model = BookShelf
        fields = '__all__'

    def get_authors(self, obj):
        """This function returning the authors name in list form

        Args:
            obj (BookSerializer): _description_

        Returns:
            [str]: name of author
        """
        return [obj.author.author]
