class CustomAPIError(Exception):
    pass

    def api_check(key):

        try :

            mydict = {"name": "Jamal","education":"MCA"}
            print(mydict[key])

            if (mydict[key] == None):
                raise CustomAPIError("Key not found")

            
        
        except CustomAPIError as e:
            print(e)

    api_check("game")
# api_check("name")