import requests

# Instagram API Access_token of the owner << used in the scope of basic, public_content, likes ,comments >>
APP_ACCESS_TOKEN = '1598029108.a88c6e0.b2a4559815d640e7be0299013d01a1a8'
# Base URL common for all the requests in the file.
BASE_URL = 'https://api.instagram.com/v1/'


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
    if info_of_owner['data']['website'] != "":  # If Bio of the owner is mentioned
        print "Website                  :", info_of_owner["data"]["website"]
    if info_of_owner['data']['bio'] != '':
        print "Bio                      :", info_of_owner["data"]["bio"]
    print "\n************************************************************************************************"
    if info_of_owner['meta']['code'] == 200:
        print "\nInformation successfully displayed"
    else:
        print "\nYou faced an error in getting the information.\nTry again later!"

owner_info()
