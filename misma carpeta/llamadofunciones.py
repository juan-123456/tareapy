#llamamos las funciones declaradas en otro archivo
import funcionesexternas as f

#invocamos las funciones 
f.funcion1()

#invocamos la otra funcion
q=input('introduzca un dato ')
w=input('introduzca otro dato ')

print(f.funcion2(q,w))

