import os
import sys 

# for i in range(100):
# 	print("%03d" % i)

for i, file in enumerate(os.listdir('bearwithus/')):
	new_name = "%04d" % i
	# print(new_name)
	os.rename("bearwithus/" + file , "bearwithus/" + new_name + ".jpg")
