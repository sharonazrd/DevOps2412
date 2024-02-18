# 1. Testing Github API - Create a program in python that goes to the following API and
# checks that at least 5 git repositories exists - https://api.github.com/users/avielb/repos

import requests
from selenium import webdriver
from time import sleep

my_driver = webdriver.Chrome()

repositories = requests.get("https://api.github.com/users/avielb/repos")
repos = len(repositories.json())
if repos < 5:
    print("Less that 5 repositories exist in https://api.github.com/users/avielb/repos")
else:
    print ("Number of existing Repositories in https://api.github.com/users/avielb/repos:",repos)


#======================================================================================

# 2. Testing agify API - Create a program in python that generates 3 random names and
# checks that the age from the reply in this link: https://api.agify.io/?name=<name> is
# between 0 - 120

name = input("Please enter your name: ")
web_address = "https://api.agify.io/?name=" + name
# response = requests.get(web_address)
# data = response.json()
# age = data.get('age')
age = requests.get(web_address).json()["age"]
print("The predicted age for ",name ," is:", age)
assert (age > 0 and age < 120)

#======================================================================================

# 3. Testing universities API - Go to http://universities.hipolabs.com/search?country=Israel
#and make sure that israel has at least 5 universities

unis_count = len(requests.get("http://universities.hipolabs.com/search?country=Israel").json())
print("There are ", unis_count, " universities in Israel")
assert unis_count > 5

#======================================================================================

# 4. Using Selenium go to https://www.ycombinator.com/ and test that the title is “Y
# Combinator”

dr = webdriver.Chrome()
dr.get("https://www.ycombinator.com/")
title = dr.title
assert title == "Y Combinator"
print("The website title is: ",title)

#======================================================================================

# 5. Using selenium go to https://hub.docker.com and test the the title is “Docker Hub
# Container Idocker run -d --name my-jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins:ltsmage Library | App Containerization”

dr = webdriver.Chrome()
dr.get("https://hub.docker.com")
sleep(10)
title = dr.title
assert title == "Docker Hub Container Image Library | App Containerization"
print("The website title is: ",title)