my_dinner = ["warren buffet", "canserbero", "jesus", "messi"]

print(f"Hola! {my_dinner[0].title()}, ven a cenar conmigo para hablar de inversiones y economía.")
print(f"Hola! {my_dinner[1].title()}, ven a cenar conmigo para hablar de rap, política y problematicas sociales.")
print(f"Hola! {my_dinner[-2].title()}, ven a cenar conmigo para hablar de tu vida, tu verdad y tu impacto en la historia.")
print(f"Hola! {my_dinner[3].title()},ven a cenar conmigo para hablar de fútbol, tu historia, y tu grandeza.")

print(f"Ups, parece que {my_dinner[-1].title()} no va a poder venir el día de hoy")

my_dinner.remove("messi")
my_dinner.append("Papá")

print(f"Hola! {my_dinner[0].title()}, ven a cenar conmigo para hablar de inversiones y economía.")
print(f"Hola! {my_dinner[1].title()}, ven a cenar conmigo para hablar de rap, política y problematicas sociales.")
print(f"Hola! {my_dinner[-2].title()}, ven a cenar conmigo para hablar de tu vida, tu verdad y tu impacto en la historia.")
print(f"Hola! {my_dinner[3].title()}, ven a cenar conmigo para hablar de nuestra vida, compartir como padre e hijo.")

print("Para todos mis invitados, acabo de encontrar una mesa más grande, con mas asientos, más personas se nos unirán")

my_dinner.insert(0, "Charlie Munger")
my_dinner.insert(2, "Steve Jobs")
my_dinner.append("Elon Musk")

print("-------------------------------------------------------")

print(f"Hola! {my_dinner[0].title()}, ven a cenar conmigo para hablar de tu origen, tus motivaciones, como llegaste a Berkshire y tu equipo con Warren")
print(f"Hola! {my_dinner[1].title()}, ven a cenar conmigo para hablar de inversiones y economía.")
print(f"Hola! {my_dinner[2].title()}, ven a cenar conmigo para hablar de tu vida, visión, que opinas de Apple en la actualidad, tu lucha con el cáncer, y la formación de Apple")
print(f"Hola! {my_dinner[3].title()}, ven a cenar conmigo para hablar de rap, política y problematicas sociales.")
print(f"Hola! {my_dinner[4].title()}, ven a cenar conmigo para hablar de tu vida, tu verdad y tu impacto en la historia.")
print(f"Hola! {my_dinner[5].title()}, ven a cenar conmigo para hablar de nuestra vida, compartir como padre e hijo.")
print(f"Hola! {my_dinner[-1].title()}, ven a cenar conmigo para hablar de tus logros, que se siente ser el hombre mas rico delm mundo, como aprendiste a programar y como funciona tu cerebro")

print("PARA TODOS: Lo lamento, la mesa no alcanzará a llegar para la cena, solo podré invitar a dos de ustedes")

primero_fuera = my_dinner.pop()

print(f"Lo siento {primero_fuera}, no hay espacio para ti en mi cena.")

segundo_fuera = my_dinner.pop()

print(f"Lo siento {segundo_fuera}, no hay espacio para ti en mi cena.")

tercero_fuera = my_dinner.pop()

print(f"Lo siento {tercero_fuera}, no hay espacio para ti en mi cena.")

cuarto_fuera = my_dinner.pop()

print(f"Lo siento {cuarto_fuera}, no hay espacio para ti en mi cena.")

quinto_fuera = my_dinner.pop()

print(f"Lo siento {quinto_fuera}, no hay espacio para ti en mi cena.")

print("--------------------------")

print(f"{my_dinner[0]}, te espero sin falta a mi cena! Estará chida")
print(f"{my_dinner[1]}, te espero sin falta a mi cena! Estará chida")

del my_dinner[0]
del my_dinner [0]

print(my_dinner)