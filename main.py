# Import necessary classes from http.server module
from http.server import HTTPServer, BaseHTTPRequestHandler  
# Import time module for timestamp functionality
import time  

# Set the host IP address
HOST = "192.168.20.154"
# Set the port number
PORT = 9999  

# Define a custom HTTP request handler class
class NeuralHTTP(BaseHTTPRequestHandler):  
    # Method to handle GET requests
    def do_GET(self):  
        # Send a 200 OK response
        self.send_response(200) 
        # Set the content type to HTML
        self.send_header("Content-type", "text/html")  
        # Send the end of headers
        self.end_headers()  
       
        # Write the HTML response body
        self.wfile.write(bytes("<html><body><h1>HELLO WORD!</h1></body></html>", "utf-8"))
    
    # Method to handle POST requests
    def do_POST(self): 
        # Send a 200 OK response
        self.send_response(200)  
        # Set the content type to JSON
        self.send_header("Content-type", "application/json")
        # Send the end of headers
        self.end_headers()  
        
        # Get the current date and time
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        
        # Write the JSON response body with the current time
        self.wfile.write(bytes('{"time": "' + date + '"}', "utf-8"))

# Create an HTTP server instance
server = HTTPServer((HOST, PORT), NeuralHTTP)
# Print a message indicating the server is running
print("Server now running...") 
# Start the server and keep it running indefinitely
server.serve_forever()  

# The following lines are unreachable due to serve_forever():
# Close the server
server.server_close()  
# Print a message indicating the server has stopped
print("Server stopped!")