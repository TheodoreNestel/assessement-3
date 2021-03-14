from unittest import TestCase
from app import app , conversion ,convert ,check_cur ,home_page

class ForexCoverter(TestCase):

    def test_convert(self):

        self.assertEqual(convert("cdc","cdc",3),6)

    def test_check_cur(self):
        return

    def test_form(self):
        with app.test_client() as client: ##this is meant to be the way to run code off line with client being the server
            res = client.get("/")##This gives us the / page contents 
            html = res.get_data(as_text=True) ##this turns all the data to string

                 ##now that the setup is done we can write asertions to make sure we're getting what we want
                
            
                ##Now lets check to see if the unique h1 in  our template exists in this html response 
            self.assertIn("<title>Conversion form </title>", html) ##this one works by looking for a specified string

    
    def test_conversion(self):
        with app.test_client() as client: 
            res = client.get("/conversion") 
            html = res.get_data(as_text=True) 
            self.assertIn("<title>converstion</title>", html) 
