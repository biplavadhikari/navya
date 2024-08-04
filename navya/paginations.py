from rest_framework.pagination import PageNumberPagination

from transaction.utils import CustomResponse


class BasePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100
    page_query_param = "page"

    def get_paginated_response(self, data):
        return CustomResponse(
            {
                "meta": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                    "count": self.page.paginator.count,
                },
                "results": data,
            }
        )
