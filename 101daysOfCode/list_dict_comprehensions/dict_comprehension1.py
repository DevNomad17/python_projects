sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

words_list = sentence.split()
result = {item:len(item) for item in words_list}
print(result)