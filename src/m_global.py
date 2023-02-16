import subprocess

#subprocess.call("/home/bat/Project/Python/Kruger/Artix_gen/src/main.py", shell=True)
result = subprocess.run(["python3.11" ,"-u", "/home/bat/Project/Python/Kruger/Artix_gen/src/main.py"])
print(result)