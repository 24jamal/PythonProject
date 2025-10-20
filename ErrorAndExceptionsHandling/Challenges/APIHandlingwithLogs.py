import logging

logging.basicConfig(
    filename = "applogs.txt",
    level = logging.DEBUG,
    format= "%(asctime)s %(levelname)s %(message)s"
)


def APIError(Exception):
    pass


def api_call(endpoint):

    api_data = {
        "user" : {"name" : "Jamal", "age" : 23, "education" : "mca"},
        "products" : {"mobile" : "Redmi", "Food" : "Icecream", "Shirt": "Otto"}
    }

    try :
        if endpoint not in api_data:

            logging.error(f"Data not found for the key {endpoint}")
            raise APIError("Data is not found in API Data")
            
        else :
            response = {
                "status" : 200,
                "message" : "Data found in API Data"
            }
            print(f"Console Log : {response}")
            logging.info(f"Data  found for the key {endpoint}")
            return response
    except APIError as e :
        response = {
                "status" : "400",
                "message" : "Data is not found in API Data"
            }
        print(e)
        print(f"Console Log : {response}")
        logging.error(f"Error :: {e}")
        return response

        
    
print(api_call("user2"))