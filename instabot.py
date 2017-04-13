# Here we imported Requests library to make network requests
import requests

# Instagram API Access_token of the owner << used in the scope of basic, public_content, likes ,comments >>
APP_ACCESS_TOKEN = '1598029108.a88c6e0.b2a4559815d640e7be0299013d01a1a8'
# Base URL common for all the requests in the file.
BASE_URL = 'https://api.instagram.com/v1/'

# Function below is to check whether we have succeeded or not.
def success_or_failure(data):
    print "\n************************************************************************************************"
    if data['meta']['code'] == 200:
        print "Your task was successfully performed."
    else:
        print "Sorry!!!\nYou faced an error while performing your task.\nTry again later!"
    print "\n************************************************************************************************"


# The function below gets the information about the owner of the access_token() using 'GET'.
def owner_info():
    request_owner_url = BASE_URL + "users/self/?access_token=" + APP_ACCESS_TOKEN
    info_of_owner = requests.get(
        request_owner_url).json()  # GET call to fetch the information of the access_token's owner
    print "Full Name                :", info_of_owner["data"]["full_name"]
    print "UserName                 :", info_of_owner["data"]["username"]
    print "User Id                  :", info_of_owner["data"]["id"]
    print "Total Media              :", info_of_owner["data"]["counts"]["media"]
    print "Follows                  :", info_of_owner["data"]["counts"]["follows"]
    print "Followed by              :", info_of_owner["data"]["counts"]["followed_by"]
    print "Link to profile picture  :", info_of_owner["data"]["profile_picture"]
    if info_of_owner['data']['website'] != "":  # If Website of the owner is mentioned
        print "Website                  :", info_of_owner["data"]["website"]
    if info_of_owner['data']['bio'] != '':  # If Bio of the owner is mentioned
        print "Bio                      :", info_of_owner["data"]["bio"]
    success_or_failure(info_of_owner) # To check whether we have succeeded or not.


owner_info()


# The function below gets the information about the User.
def display_user_info(username):
    request_user_url = BASE_URL + "users/search?q=" + username + "&access_token=" + APP_ACCESS_TOKEN
    user_info = requests.get(request_user_url).json()  # GET call to search user for the informaion
    print "**************************************| User Information |**************************************"
    print "\nFull Name                :", user_info["data"][0]["full_name"]
    print "UserName                 :", user_info["data"][0]["username"]
    print "User Id                  :", user_info["data"][0]["id"]
    print "\n************************************************************************************************"


display_user_info("api_17790")


# The function below gets the information about the User and return user's ID using 'GET'.
def get_user_id(username):
    request_user_url = BASE_URL + "users/search?q=" + username + "&access_token=" + APP_ACCESS_TOKEN
    user_info = requests.get(request_user_url).json()  # GET call to search user for the information
    user_id = user_info["data"][0]["id"]
    return user_id  # To Return user's id


get_user_id("api_17790")


# The function below fetches public post starting from the most recent one published by the user using 'GET'.
def get_user_post(username):
    user_id = get_user_id(username)  # get_user_id(username) function called here to get the user's ID
    user_url = BASE_URL + "users/" + user_id + "/media/recent/?access_token=" + APP_ACCESS_TOKEN
    request_user_recent_post = requests.get(user_url).json()
    return request_user_recent_post


# The function below chooses the post in a creative way
# i.e the one with minimum/maximum no. likes/comments or most recent one.
def get_post_by_choice(username, option=0, selection=0):
    requested_post = get_user_post(username)  # This function is called here to get the user's post details.
    post_index = 0
    like_list_on_each_post = []
    comment_list_on_each_post = []
    total_user_media = len(requested_post['data'])  # To get the total no. of media
    if total_user_media == 0:
        print("\nThis User has no post!")
    else:
        if option == 1:
            for each_media in range(0, total_user_media):
                like_list_on_each_post.append(requested_post['data'][each_media]['likes']['count'])
            if selection == 1:
                least_count = min(like_list_on_each_post)
                post_index = like_list_on_each_post.index(least_count)
            if selection == 3:
                most_count = max(like_list_on_each_post)
                post_index = like_list_on_each_post.index(most_count)
        if option == 2:
            for each_media in range(0, total_user_media):
                comment_list_on_each_post.append(requested_post['data'][each_media]['comments']['count'])
            if selection == 1:
                least_count = min(comment_list_on_each_post)
                post_index = comment_list_on_each_post.index(least_count)
            if selection == 3:
                most_count = max(comment_list_on_each_post)
                post_index = comment_list_on_each_post.index(most_count)
        print "Link to the Media        :", requested_post['data'][post_index]['link']  # To print the link to a media.
        post_id = requested_post["data"][post_index]['id']
        return post_id  # To return the particular media ID


# The function below sets a like on a particular media by the currently authenticated user using 'post'.
def like_user_post(username, option, selection):
    post_id = get_post_by_choice(username, option, selection)  # get_user_post_id()function called here to get post ID
    payload = {'access_token': APP_ACCESS_TOKEN}
    like_post_url = BASE_URL + "media/" + post_id + "/likes"
    like = requests.post(like_post_url, payload).json()  # Post call to like the post
    success_or_failure(like) # To check whether we have succeeded or not.


like_user_post("api_17790", 0, 1)


# The function below creates a comment on a media object using 'post'.
def post_comment(username, option, selection):
    media_id = get_post_by_choice(username, option,
                                  selection)  # get_user_post_id(username) function called here to get post ID
    url_post_comment = BASE_URL + "media/" + media_id + "/comments"
    input_comment = raw_input("Write a comment you want to post.\n")
    request_data = {"access_token": APP_ACCESS_TOKEN, 'text': input_comment}  # Required to created a comment.
    comment = requests.post(url_post_comment, request_data).json()  # Post call to comment the post
    success_or_failure(comment) # To check whether we have succeeded or not.


post_comment("api_17790", 0, 1)


# The Function returns comment Id that contains a particular word in a particular post
def word_search_in_comment(username, option, selection):
    media_id = get_post_by_choice(username, option, selection)  # get_user_post_id(username) function called here to get post ID
    url_post_comment = BASE_URL + "media/" + media_id + "/comments?access_token=" + APP_ACCESS_TOKEN
    various_comments = requests.get(url_post_comment).json()
    word_search = raw_input("Enter a word you want to search in the comments")
    print "\n************************************************************************************************"
    comments_id = []
    comments_list = []
    user_name = []
    for each_comment in various_comments['data']:
        comments_list.append(each_comment['text'])
        comments_id.append(each_comment['id'])
        user_name.append(each_comment['from']['username'])
    comments_id_matched = []
    comments_matched = []
    user_found = []
    for each_item in range(len(comments_list)):
        if word_search in comments_list[each_item]:
            comments_matched.append(comments_list[each_item])
            comments_id_matched.append(comments_id[each_item])
            user_found.append(user_name[each_item])
    if len(comments_matched) == 0:
        print "No comment have " + word_search + " word"
        return False,media_id, False, False
    else:
        print "Following are the comments that contains the " + word_search + " word:"
        for i in range(len(comments_matched)):
            print("-->  " + comments_matched[i])
        return comments_id_matched, media_id, comments_matched, user_found
