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
followers = set(myprofile.get_followers())
    
#obtain my followees (people I follow)
followees = set(myprofile.get_followees())

#determine the list of usernames that have unfollowed 
unfollowed_set = followees - followers

#obtain and print the usernames
unfollowed_users = [(o.username + ' (verified)') if o.is_verified
                    else (o.username) for o in unfollowed_set]

print(*unfollowed_users, sep = "\n")

print('There are ' + str(len(unfollowed_users)) + ' users that aren\'t following back')
