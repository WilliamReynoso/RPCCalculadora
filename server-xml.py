from xmlrpc.server import SimpleXMLRPCServer

def suma_numeros(a, b):
    return a + b
def resta_numeros(a, b):
    return a - b
def multiplica_numeros(a, b):
    return a * b
def divide_numeros(a, b):
    return a / b

server = SimpleXMLRPCServer(('localhost', 8000))
print("Listening on port 9000...")
server.register_function(suma_numeros, 'suma')
server.register_function(resta_numeros, 'resta')
server.register_function(multiplica_numeros, 'multiplica')
server.register_function(divide_numeros, 'divide')

server.serve_forever()