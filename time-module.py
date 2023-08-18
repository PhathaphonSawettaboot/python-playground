import time

#Getting the Current Time:
current_time = time.time()  # Returns the current time in seconds since the epoch (January 1, 1970)
print("Current time:", current_time)


timestamp = time.mktime((2023, 7, 31, 12, 0, 0, 0, 0, 0))
print("Timestamp:", timestamp)


local_time = time.localtime()
print("Local time:", local_time)
