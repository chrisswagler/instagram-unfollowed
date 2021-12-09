#instagram unfollowed tracker

import instaloader

#get instance
L = instaloader.Instaloader()

#login - change login credentials
USERNAME = input('username:')
PASSWORD = input('password:')
print('loading...')
L.login(USERNAME, PASSWORD)

#obtain my profile using _USERNAME_
myprofile = instaloader.Profile.from_username(L.context, USERNAME)

#obtain my followers
follower_iterator = myprofile.get_followers()
follower_dict = {}
for follower in follower_iterator:
    follower_dict.update({follower.username: follower})
    
#obtain my followees (people I follow)
followee_iterator = myprofile.get_followees()
followee_dict = {}
for followee in followee_iterator:
    followee_dict.update({followee.username: followee})

#determine the list of usernames that have unfollowed 
unfollowed_list = []

#for each of the people that I follow
for followee_username in followee_dict.keys():
    #if they aren't one of my followers
    if followee_username not in follower_dict:
        #add them to the unfollowed list
        unfollowed_list.append(followee)
        #print their username and if verified or not
        if not followee_dict.get(followee_username).is_verified:
            print(followee_username)
        else:
            print(followee_username + ' (verified)')

print('There are ' + str(len(unfollowed_list)) + ' users that aren\'t following back')
