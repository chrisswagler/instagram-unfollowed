#instagram unfollowed tracker

import instaloader

#get instance
L = instaloader.Instaloader()

#login - change login credentials
USERNAME = 'ig_username'
PASSWORD = 'ig_password'
L.login(USERNAME, PASSWORD)

#obtain my profile using _USERNAME_
myprofile = instaloader.Profile.from_username(L.context, USERNAME)

#obtain the list of my followers
follower_iterator = myprofile.get_followers()
follower_list = []
for follower in follower_iterator:
    follower_list.append(follower.username)
    
#obtain the list of the people I follow
followee_iterator = myprofile.get_followees()
followee_list = []
for followee in followee_iterator:
    followee_list.append(followee.username)

#determine the list of usernames that have unfollowed 
unfollowed_list = []

#for each of the people I follow
for followee in followee_list:
    #if they aren't one of my followers
    if followee not in follower_list:
        #add them to the unfollowed list and print
        unfollowed_list.append(followee)
        print(followee)

print('There are ' + str(len(unfollowed_list)) + ' users that aren\'t following back')
