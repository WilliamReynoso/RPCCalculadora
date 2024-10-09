import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
a = input("Primer numero: ")
b = input("Segundo numero: ")
op = ''
while op != '99':
    print(f"Tus numeros son a = {a} y b = {b}")
    op = input("Elige la operacion a solicitar al servidor: \n"+
           "1. a + b\n"+
           "2. a - b\n"+
           "3. a * b\n"+
           "4. a / b\n"+
           "99. salir\n Opcion -> ")
    if op == '1':
        result = proxy.suma(float(a), float(b))
        print(f"\n>>El resultado de a + b es: {result}")
        continue
    elif op == '2':
        result = proxy.resta(float(a), float(b))
        print(f"\n>>El resultado de a - b es: {result}")
        continue
    elif op == '3':
        result = proxy.multiplica(float(a), float(b))
        print(f"\n>>El resultado de a * b es: {result}")
        continue
    elif op == '4':
        result = proxy.divide(float(a), float(b))
        print(f"\n>>El resultado de a / b es: {result}")
        continue
    elif op == '99':
        print("Saliendo del programa")
        break