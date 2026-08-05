class api_fetch:
    def fetch(self):

        print("Fetching data from API")

class db_fetch:
    def fetch(self):

        print("Fetching data from Database")

class s3_fetch:
    def fetch(self):

        print("Fetching data from S3")

obj = api_fetch()
obj.fetch() 

#Polymorphism: Same method name but different implementation