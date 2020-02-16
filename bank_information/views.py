from rest_framework.decorators import api_view, permission_classes
from bank_information.serializers import BankSerializer
from bank_information.models import BankBranches
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status, permissions


@permission_classes((permissions.AllowAny,))
@api_view(['GET'])
def branch_search(request):
    """
    Endpoint to perform autocomplete search based on branch name
    params: branch name, offset and limit
    """
    try:
        paginator = LimitOffsetPagination()
        search_term = request.GET['q'] or ''
        search_object = BankBranches.objects.filter(branch__istartswith=search_term).order_by('ifsc')
        result_page = paginator.paginate_queryset(search_object, request)
        file_obj = BankSerializer(result_page, many=True)
        return Response(
            {
                'message': 'Branch details retrieved successfully!',
                'data': file_obj.data
            }, status=status.HTTP_200_OK)
    except BankBranches.DoesNotExist:
        return Response({'message': 'No matching data found for the search entries!'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((permissions.AllowAny,))
@api_view(['GET'])
def bank_details(request):
    """
    Endpoint to fetch the bank details
    params: search_query(q)
    """
    try:
        paginator = LimitOffsetPagination()
        search_term = request.GET['q'] or ''
        bank_details_object = BankBranches.objects.filter(
            (
                Q(branch__icontains= search_term) |
                Q(ifsc__icontains=search_term) |
                Q(city__icontains=search_term) |
                Q(district__icontains=search_term) |
                Q(state__icontains=search_term) |
                Q(bank_name__icontains=search_term) |
                Q(ifsc__icontains=search_term) |
                Q(address__icontains=search_term)
            )
        ).order_by('ifsc')
        result_page = paginator.paginate_queryset(bank_details_object, request)
        file_obj = BankSerializer(result_page, many=True)
        return Response(
            {
                'message': 'Bank details retrieved successfully!',
                'data': file_obj.data
            }, status=status.HTTP_200_OK)
    except BankBranches.DoesNotExist:
        return Response({'message': 'No matching data found for the search entries!'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_404_NOT_FOUND)