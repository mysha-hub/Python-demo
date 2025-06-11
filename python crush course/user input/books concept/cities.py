
prompt = "type a city name:"
prompt += "we will reeturn you the value untill you type 'exit'."
while True:
    city = input(prompt)
    if city == 'exit':
        break
    else:
        print(f"I would like to vist {city.title()}")
