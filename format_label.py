
def format_data():
    f = open("template", "r")

    data = f.read()

    data = data.replace("{vin}", "WAULF78K59N031106")
    data = data.replace("{year}", "16")
    data = data.replace("{make}", "TOYOTA")
    data = data.replace("{model}", "RAV 4")
    data = data.replace("{color}", "METALLIC SILVER")
    data = data.replace("{stock}", "8371AD3A")
    data = data.replace("{mileage}", "35,630 MILES")
    data = data.replace("{entry_date}", "JAN 05")
    data = data.replace("{dealership}", "Kenny Kent Toyota")

    return data

# this function is for testing on the Cayenne
def format_porsche_data():
    f = open("template", "r")

    data = f.read()

    data = data.replace("{vin}", "WP1AA2AY0KDA00835")
    data = data.replace("{year}", "19")
    data = data.replace("{make}", "PORSCHE")
    data = data.replace("{model}", "CAYENNE")
    data = data.replace("{color}", "BLUE")
    data = data.replace("{stock}", "KDA00835")
    data = data.replace("{mileage}", "19,872 MILES")
    data = data.replace("{entry_date}", "JAN 05")
    data = data.replace("{dealership}", "DPatrick Motoplex")

    return data


def format_danny_data():
    f = open("template", "r")

    data = f.read()

    data = data.replace("{vin}", "JTMZFREV1GJ089869")
    data = data.replace("{year}", "2016")
    data = data.replace("{make}", "TOYOTA")
    data = data.replace("{model}", "RAV 4")
    data = data.replace("{color}", "METALLIC SILVER")
    data = data.replace("{small_color}", "METALLIC SLVR")
    data = data.replace("{stock}", "8371AD3A")
    data = data.replace("{mileage}", "35,630 MILES")
    data = data.replace("{entry_date}", "JAN 05")
    data = data.replace("{dealership}", "")

    return data
if __name__ == "__main__":

    # label = format_data()
    label = format_danny_data()
    # label = format_porsche_data()
    print(label)

# print(data)
