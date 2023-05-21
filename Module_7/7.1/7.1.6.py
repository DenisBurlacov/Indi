def get_body_mass_index(mass, growth):
    index = mass / ((growth / 100) ** 2)
    if index > 25:
        print('Избыточная масса тела')
    elif index < 18.5:
        print('Недостаточная масса тела')
    elif 18.5 <= index <= 25:
        print('Норма')


get_body_mass_index(74, 178)

def get_body_mass_index(weight, height):
    index = weight / ((height / 100) ** 2)
    if index > 25:
        print('Избыточная масса тела')
    elif index < 18.5:
        print('Недостаточная масса тела')
    elif 18.5 <= index <= 25:
        print('Норма')