from rest_framework import serializers
from .models import Borrowing
from book_service.models import Book


class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book",
            "user",
        )
        read_only_fields = ("id", "actual_return_date", "user")

    def validate(self, attrs):
        Borrowing.validate_borrowing(
            attrs.get("borrow_date"),
            attrs.get("expected_return_date"),
            serializers.ValidationError,
        )

        book = attrs.get("book")
        if book.inventory <= 0:
            raise serializers.ValidationError("This is not available now.")

        return attrs
