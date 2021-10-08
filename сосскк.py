from pprint import pprint
def get_data(file_name):
    data = dict()
    with open (file_name) as file:
        for line in file:
            name_cook = line.strip()
            counter = int(file.readline())

            temp_list = []
            for item in range(counter):
                inred, quantity, heft = file.readline().split("|")
                temp_list.append({"Ингредиенты": inred.strip(), "Колличество": quantity.strip(), "Вес": heft.strip()})
            data[name_cook] = temp_list
            file.readline()
    return data
file = 'recipes.txt'
data = get_data(file)
#pprint(data)

def get_shop_list_by_dishes(dishes, person_count):
    cook_dict = {}
    for dish in dishes:
        if dish in data:
            for ingress_diets in data[dish]:
                dict_ing = {}
                if ingress_diets['Ингредиенты'] in cook_dict:
                    cook_dict[ingress_diets['Ингредиенты']].get('Колличество') + ingress_diets['Колличество'] * person_count
                    cook_dict[ingress_diets['Ингредиенты']].update

                else:
                    dict_ing['Вес'] = ingress_diets['Вес']
                    dict_ing['Колличество'] = ((ingress_diets['Колличество'] * person_count))
                    cook_dict[ingress_diets['Ингредиенты']] = dict_ing
    return cook_dict


pprint(get_shop_list_by_dishes({'Омлет', 'Фахитос', 'Запеченный картофель'}, 4))








