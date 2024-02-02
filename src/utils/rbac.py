# def access_control(*role):
#     def inner(func):
#         def wrapper(*args, **kwargs):
#             jwt = get_jwt()
#             get_role = jwt["role"]
#             if get_role in role:
#                 return func(*args, **kwargs)
#             else:
#                 abort(401, message = "You are not authorized to access these resource.")
#         return wrapper
#     return inner
