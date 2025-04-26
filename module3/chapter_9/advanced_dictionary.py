my_garage = {"subaru": "forester", "ford":"f150", "geo": "metro", "bae":"lmtv"}
my_track_garage = {"mazda":"miata", "subaru":"wrx"}

my_combined_garage = my_garage | my_track_garage
#the key, "subaru", in the second dictionary supplants the first if on the right side of the pipe operator
print(my_combined_garage)

settings = {"theme": "light", "notifications": "off"}
user_settings = {"theme": "dark"}
# settings = settings | user_settings
settings |= user_settings

print(settings)