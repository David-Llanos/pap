import os



## App settings
name = "De Problemas a Proyectos - PaP"

host = "0.0.0.0"

port = int(os.environ.get("PORT", 8050))

debug = True

contacts = "https://www.linkedin.com/in/david-llanos-47193528/"

code = "https://github.com/David-Llanos/pap"

fontawesome = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'



## File system
root = os.path.dirname(os.path.dirname(__file__)) + "/"



## DB