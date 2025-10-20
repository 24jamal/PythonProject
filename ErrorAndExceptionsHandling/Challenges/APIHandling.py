class APIError(Exception):

    pass

def api_call(endpoint):

    api_data = {
        "user" : {"name" : "Jamal", "age" : 23, "Education" : "MCA"},
        "products" : {"Book" : "War and Peace" ,"TV" : "Sony" , "favFood" : "Burger"},
        "info" : {"hobby" : "coin collecting"}
    }

    try : 

        if endpoint not in api_data:
            raise APIError("API key not found")
        else:
            return {
                "status" : 200,
                "message" : f"API response :: {api_data[endpoint]}"
            }

    except APIError as e:
        print(e)
        return {
            "status" : 400,
            "Message" : "Key is not in api_data"
        }
    
print(api_call("userd"))
    
