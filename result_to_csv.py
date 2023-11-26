import pandas as pd

def result_to_csv(file_name, car, quantity_car, average_speed_car, van, quantity_van, average_speed_van, bus, quantity_bus, average_speed_bus):
    init_keys = ["file_name", "car", "quantity_car", "average_speed_car", "van", "quantity_van", "average_speed_van", "bus", "quantity_bus", "average_speed_bus"]

    try:
        df = pd.read_csv('vehicles_data.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=init_keys)

    new_row = {key: [value] for key, value in zip(init_keys, [file_name, car, quantity_car, average_speed_car, van, quantity_van, average_speed_van, bus, quantity_bus, average_speed_bus])}
    df = pd.concat([df, pd.DataFrame(new_row)], ignore_index=True)
    df.to_csv('py\\result.csv', index=False)

file_name = 'KRA-2-7-2023-08-22-evening'
car = 'car'
quantity_car = 430
average_speed_car = 32.64
van = 'van'
quantity_van = 15
average_speed_van = 25.30
bus = 'bus'
quantity_bus = 22
average_speed_bus = 26.75

result_to_csv(file_name, car, quantity_car, average_speed_car, van, quantity_van, average_speed_van, bus, quantity_bus, average_speed_bus)
