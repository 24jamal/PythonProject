class FileManager:

    def __init__(self, filename, mode):

        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Opening file")
        self.file = open(self.filename,self.mode )
        return self.file
    
    def __exit__(self, exc_type,exc_val, trace ):
        print("Closing file")
        if self.file:
            self.file.close()

        if exc_type is not None:

            print(f"{exc_type.__name__} is the error -- {exc_val}")
            return True
        return False

##################################
with FileManager("ErrorAndExceptionsHandling\Challenges\data.txt","w") as f:

    f.write("First line is written")
    x = 12/0

    f.write("THis line will not executed")
