# 1. Write the following code: a = 1/0;
# 2. Build a corresponding try-except block to avoid exception.
try:
    a = 1 / 0
except:
    print("Division by zero")

print("----------------------------------")

# 3. Is the following code legal?
try:
    x = 1
finally:
    print("finally")

print("----------------------------------")

# 4. What exception types can be caught by the following handler?
# Except:
# A: All exceptions errors

# 5. What is wrong with using the above type of exception handler?
# A: too general

# 6. What exceptions can be caught by the following handlers?
# except IOError
# A: IOError is an exception raised for input/output-related errors
# except ZeroDivisionError
# A: This exception occurs when you try to divide a number by zero, which is mathematically undefined.

# 7. Create a text file named “words.txt”
# programmatically
# 8. Write your name into the file
# 9. Read your file content and print it

write_to_file = open("words.txt", "a+")
write_to_file.write("sharon\n")
write_to_file.write("azrad\n")
write_to_file.close()
read_from_file = open("words.txt","r")
print(read_from_file.read())

print("----------------------------------")

# 10. Write Hebrew content into your text file and print its content programmatically.
write_to_file = open("words.txt", "w")
write_to_file.write("סתם משפט בעברית")
write_to_file.close()

read_from_file = open("words.txt","r")
print(read_from_file.read())

print("----------------------------------")

# 11. Create an image from code (png file) Hint: use Pillow
from PIL import Image

# Create a new white image with dimensions 300x200
width, height = 300, 200
new_image = Image.new("RGB", (width, height), "white")

# Save the image to a file
new_image.save("blank_image.jpg")

# Close the image (optional, as it will be automatically closed when it goes out of scope)
new_image.close()