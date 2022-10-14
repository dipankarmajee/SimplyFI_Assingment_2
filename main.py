# Amsterdam, Kiev, Zurich, Prague, Berlin, Barcelona.
# Paris-Skopje, Zurich-Amsterdam, Prague-Zurich, Barcelona-Berlin, Kiev-Prague, Skopje-Paris, Amsterdam-Barcelona, Berlin-Kiev, Berlin-Amsterdam.
# You know that your kid started with Kiev
# Write a data structure and algorithm that will give you the route which your son was traveling.

def travelling_routes(available_tickets_list, cities_list, initial_cities):
    new_available_tickets_list = []
    for i in available_tickets_list:
        new_available_tickets_list.append(i.split('-'))
    
    final_travelling_routes = []
    counter = 0
    while cities_list:
        if initial_cities in cities_list:
            for j in new_available_tickets_list:
                if j[0] == initial_cities:
                    final_travelling_routes.append(j)
                    new_available_tickets_list.remove(j)
                    cities_list.remove(initial_cities)
                    break
        else:
            last_city = final_travelling_routes[counter][1]
            for k in new_available_tickets_list:
                if k[0] == last_city:
                    final_travelling_routes.append(k)
                    new_available_tickets_list.remove(k)
                    cities_list.remove(last_city)
                    counter += 1
    
    travelling_routes_number = 1
    for l in final_travelling_routes:
        # print("-".join(l))
        print("The {} travelling route is {}".format(travelling_routes_number, "-".join(l)))
        travelling_routes_number += 1          
                
                    

cities_list = ['Amsterdam', 'Kiev', 'Zurich', 'Prague', 'Berlin', 'Barcelona']
available_tickets_list = ['Paris-Skopje', 'Zurich-Amsterdam', 'Prague-Zurich', 'Barcelona-Berlin', 'Kiev-Prague', 'Skopje-Paris', 'Amsterdam-Barcelona', 'Berlin-Kiev', 'Berlin-Amsterdam']
initial_cities = 'Kiev'

travelling_routes(available_tickets_list, cities_list, initial_cities)
