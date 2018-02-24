import memory_profiler
import random
import time

names = ["John", "Corey", "Adam", "Steve", "Rick", "Thomas"]
majors = ["Math", "Engineering", "Compsci", "Arts", "Business"]

print("Memory before {} MB".format(memory_profiler.memory_usage()))

def people_list(num_people):
	result= []
	for i in range(num_people):
		person = {
			"id": i,
			"name": random.choice(names),
			"major": random.choice(majors)
		}

		result.append(person)
	return result

def people_generator(num_people):
	for i in range(num_people):
		person = {
			"id": i,
			"name": random.choice(names),
			"major": random.choice(majors)
		}

		yield person

# t1 = time.time()
# people = people_list(1000000)
# t2 = time.time()

t1 = time.time()
people = people_generator(1000000)
t2 = time.time()

print("Memory after: {} MB".format(memory_profiler.memory_usage()))
print("Took {}".format(t2-t1))


# def square_numbers(nums):
# 	for i in nums:
# 		yield (i*i)

# # my_nums = square_numbers([1,2,3,4,5])

# my_nums = (x*x for x in [1,2,3,4,5])
# print (list(my_nums))

# for num in my_nums:
# 	print(num)