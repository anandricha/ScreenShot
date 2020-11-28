
import configparser


config = configparser.ConfigParser()

def read_property_file(section,key):

    config.read('C:/Users/richa.anand/PycharmProjects/POM_Using_Pytest/Pom_Project/Config/config.properties')
    sec = dict(config.items(section))
    print(sec[key])
    return sec[key]




