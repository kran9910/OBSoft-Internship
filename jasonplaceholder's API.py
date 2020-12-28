import requests
import json

# Getters to fetch data from jsonplaceholder's API

#Fetch all posts in the API
def get_all_posts():
    request = requests.get(
        str('https://jsonplaceholder.typicode.com/posts'),
    )
    posts = request.json()
    return posts

#Fecth a post from the API using its id
def get_post_by_id(post_id):
    url = 'https://jsonplaceholder.typicode.com/posts/' + str(post_id)
    request = requests.get(
        str(url),
    )
    post = request.json()
    return post

#Fetch all photos' url in the API
def get_all_photos():
    request = requests.get(
        str('https://jsonplaceholder.typicode.com/photos'),
    )
    photos = request.json()
    return photos

#Fecth a photo url from the API using its id
def get_photo_by_id(photo_id):
    url = 'https://jsonplaceholder.typicode.com/photos/' + str(photo_id)
    request = requests.get(
        str(url),
    )
    photo = request.json()
    return photo

#Fetch all todos in the API
def get_all_todos():
    url = 'https://jsonplaceholder.typicode.com/todos/'
    request = requests.get(
        str(url),
    )
    todos = request.json()
    return todos

#Fecth a todo from the API using its id
def get_todo_by_id(post_id):
    url = 'https://jsonplaceholder.typicode.com/todos/' + str(post_id)
    request = requests.get(
        str(url),
    )
    todo = request.json()
    return todo





#Functions to Display Data fetched using the Getters
def print_three_posts():
    counter = 0
    print("\nThe first 3 bodies of the Posts that are fetched from the API will be printed below:\n")
    all_posts = get_all_posts()
    for post in all_posts:
        if counter < 3:
            print(post.get('body'))
            print("\n")
            counter += 1
        else:
            return 0

def print_five_todos():
    counter = 0
    print("\nThe first 5 TODOs that are fetched from the API will be printed below:\n")
    all_todos = get_all_todos()
    for todo in all_todos:
        if counter < 5:
            print(todo)
            counter += 1
        else:
            return 0

def print_five_photos():
    counter = 0
    print("\nThe first 5 photos' URLs fetched from the API will be printed below:\n")
    all_photos = get_all_photos()
    for photo in all_photos:
        if counter < 5:
            print(photo.get('url'))
            print("\n")
            counter += 1
        else:
            return 0

def print_todo_by_id():
    id = input("\nEnter the ID (integer between 1 and 200) of your todo and its details will be printed below: ")
    todo = get_todo_by_id(id)
    if (todo == {}):
	    print("No TODO matches this ID")
    else:
        print(todo)

def print_post_by_id():
    id = input("\nEnter the ID (integer between 1 and 100) of your post and its details will be printed below: ")
    post = get_post_by_id(id)
    if (post == {}):
	    print("No post matches this ID")
    else:
        print(post)

def print_photo_by_id():
    id = input("\nEnter the ID (integer between 1 and 5000) of your photo and its URL will be printed below: ")
    photo = get_photo_by_id(id)
    if (photo == {}):
	    print("No photo matches this ID")
    else:
        print(photo.get('url'))



    
print_three_posts()
print_five_todos()
print_five_photos()
print_todo_by_id()
print_post_by_id()
print_photo_by_id()

exit = input("\nPress enter to exit...")

