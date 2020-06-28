import requests
import sqlite3 as db


class Post:
    def __init__(self,title, body, author):
        self.title = title
        self.body = body
        self.author = author


def insert_posts(post,cursor):
    insert_post_string = " insert into Posts(title, body) values(:title, :body)";
    cursor.execute(insert_post_string, {'title': post['title'], 'body': post['body']})


# function return userId with  most posts
def getUserIdWithMostPosts(posts):
    postNumberForUsers = {}
    # result 'for loop': we will have a dict where we have  userId in corresponding post number
    for post in posts:
        userId = post['userId']
        if (userId in postNumberForUsers):
            postNumberForUsers[userId] += 1
        else:
            postNumberForUsers[userId] = 1

    # Actual get userId with most posts
    mostPostsUserId = None
    mostPosts = 0
    for userId in postNumberForUsers:
        if(postNumberForUsers[userId] > mostPosts):
            mostPosts = postNumberForUsers[userId]
            mostPostsUserId = userId

    return mostPostsUserId


def getPostsByUserId(posts,userId):
    result = []
    for post in posts:
        if (post['userId'] == userId):
            result.append(post)
    return result

# Run for getUserIdWithMostPosts
# response = requests.get("http://jsonplaceholder.typicode.com/posts", timeout=6)
# if (response.ok):
#     # return list of posts where each individual post is a dict with JSON format
#     posts = response.json()
#     print(getUserIdWithMostPosts(posts))
#     print(posts)
# else:
#     print("error happened with status code: ", response.status_code)


# run for getPostsByUserId
# response = requests.get("http://jsonplaceholder.typicode.com/posts", timeout=6)
# if (response.ok):
#     # return list of posts where each individual post is a dict with JSON format
#     posts = response.json()
#     userId = getUserIdWithMostPosts(posts)
#     print(userId)
#     posts_for_user = getPostsByUserId(posts, userId)
#     print(posts_for_user)
# else:
#     print("error happened with status code: ", response.status_code)
#

#  run for db
response = requests.get("http://jsonplaceholder.typicode.com/posts", timeout=6)
connection = db.connect("my_database.db")
cursor = connection.cursor()

create_posts_table_string = '''
    CREATE TABLE Posts(
        id  INTEGER PRIMARY KEY AUTOINCREMENT,
        title text,
        body text
        );
'''
cursor.execute(create_posts_table_string)

connection.commit()
if (response.ok):
    # return list of posts where each individual post is a dict with JSON format
    posts = response.json()
    userId = getUserIdWithMostPosts(posts)
    print(userId)
    posts_for_user = getPostsByUserId(posts, userId)
    for post in posts_for_user:
        insert_posts(post, cursor)

    connection.commit()
    print(posts_for_user)
else:
    print("error happened with status code: ", response.status_code)