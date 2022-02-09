from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class KefirPaginator(PageNumberPagination):
    def get_paginated_response(self, data):
        # return Response(OrderedDict([
        #     # ('meta', ),
        #     ('total', self.page.paginator.count),
        #     ('page', self.request.query_params.get("page", "1")),
        #     ('size', len(data)),
        #     ('next', self.get_next_link()),
        #     ('previous', self.get_previous_link()),
        #     ('results', data)
        # ]))

        return Response({
            "meta": {
                "pagination": {
                'total': self.page.paginator.count,
                'page': self.request.query_params.get("page", "1"),
                'size': len(data)
            }},
            'data': data
        })
