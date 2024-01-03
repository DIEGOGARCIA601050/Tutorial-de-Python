def Principal():
  Mi_nombre = "Diego"
  Mis_apellidos = "García Roldán"
  print(Mi_nombre + " " + Mis_apellidos)
  
  #formato
  template = "Hola mi nobre es " + Mi_nombre + " y mi apellido es " + Mis_apellidos
  print(template)
  
  template = "Hola mi nobre es {} y mis apellidos son {}".format(Mi_nombre,Mis_apellidos)
  print('v2', template)
  
  template = f"Hola mi nombre es {Mi_nombre} y mis apellidos son {Mis_apellidos}"
  print(template)
  
  edad = "16 años de edad"
  template = f"hola mi nombre es {Mi_nombre} y mis apellidos son {Mis_apellidos} y tengo {edad}"
  print(template)
  a = 3
  b = 4
  c = a + b
  print(c)
  
  #codigo para cambiar pesos por dolares
  Pesos = int(input("¿Cuantos pesos deseas cambiar"))
  Dolares = Pesos / 20
  print(Dolares)
  return Dolares