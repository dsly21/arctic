import functools
import logging
import traceback

from django.db import transaction
from django.http import JsonResponse

JSON_DUMPS_PARAMS = {
    'ensure_ascii': False
}


# logger = logging.getLogger(__name__)
#
#
# def ret(json_object, status=200):
#     return JsonResponse(
#         json_object,
#         status=status,
#         safe=not isinstance(json_object, list),
#         json_dumps_params=JSON_DUMPS_PARAMS
#     )
#
#
# def error_response(exception):
#     res = {
#         "errorMessage": str(exception),
#         "traceback": traceback.format_exc()
#         }
#     return ret(res, status=400)
#
#
# def base_view(fn):
#     @functools.wraps(fn)
#     def inner(request, *args, **kwargs):
#         try:
#             with transaction.atomic():
#                 return fn(request, *args, **kwargs)
#         except Exception as e:
#             return error_response(e)
#     return inner
