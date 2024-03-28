#Created for during TCM Academy Detection Engineering 101 course
import os

for root, dirs, files in os.walk("elastic_rules"): 
    for file in files:
        if file.endswith(".toml"):
            print(file)