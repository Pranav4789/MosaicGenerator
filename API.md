To run this code, you need two terminals. First terminal that needs to be run has to be cd into the project-1989 with the command: python3 -m flask run --host=0.0.0.0 --port=2000

The second terminal needs to be cd into the folder named app_folder. Once you are in there you need to run the command: python3 -m flask run --host=0.0.0.0 --port=1000

High-Level Overview
The mosaic generator system is a microservices-based architecture, composed of a middleware service and multiple Microservice Mosaic Generators (MMGs). The middleware acts as the central point of communication between the frontend and the MMGs. To run the system, start the middleware Flask application and each of the MMGs Flask applications on their respective ports.

Connecting an MMG to the Middleware
An MMG connects to the middleware by sending an HTTP PUT request to the /addMG endpoint, including the MMG's URL in the JSON payload (e.g., {"url": "http://sp23-cs340-080.cs.illinois.edu:1000"}). Upon receiving a valid request, the middleware stores the MMG's URL and uses it to forward future mosaic generation requests.

Requesting a Mosaic from an MMG
When a user uploads a base image, the middleware forwards the request to the connected MMGs by sending an HTTP POST request to their /makeMosaic/<tilesAcross>/<tileSize> endpoints. The middleware passes the base image and the parameters tilesAcross and tileSize in the request.

Additional Details and Advanced Features
In this system, the middleware is responsible for managing connections with multiple MMGs, making it easy to scale the number of mosaic generators. By implementing the mosaic generation logic as standalone microservices, the system can handle a variety of themes and customizations.

