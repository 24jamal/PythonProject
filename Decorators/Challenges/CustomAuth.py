class PermissionError(Exception):
    pass


user = {"role" : "admin", "name" : "jamal"}

def requires_role(role):
    def decorator(func):
        def wrapper(*args, **kwargs):

            current_role = user.get("role")
            if current_role != role:
                raise PermissionError("Access Denied !! Only Admin can be done this action")
            func(*args,**kwargs)
            
        return wrapper
    return decorator

@requires_role('admin')
def delete_user():

    print("User is deleted")

delete_user()