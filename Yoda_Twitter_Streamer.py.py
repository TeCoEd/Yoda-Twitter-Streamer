#!/usr/bin/env python3
import sys
import sys, subprocess, urllib, time, tweepy
from PIL import Image
from PIL import ImageFont
import time

import inkyphat
import textwrap
font = ImageFont.truetype(inkyphat.fonts.FredokaOne, 12)

inkyphat.set_image(Image.open("/home/pi/StarWars/WAIT.png"))
inkyphat.show()
inkyphat.clear()

time.sleep(10)

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key= 'xxxxxxxxxxxxxxxxx'
consumer_secret= 'xxxxxxxxxxxxxxxxx'

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
access_token= 'xxxxxxxxxx'
access_token_secret= 'xxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class Social_Media_Mirror_StreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        
        tweet_to_check = tweet.text # checks the tweet

        does_the_tweet_contain_key_word = tweet_to_check.find("@Dan_Aldred") ### find MENTIONS replace with your Twitter handle
        does_the_tweet_contain_STAR_WARS = tweet_to_check.find("#StarWars") ### find star wars hash tag
        
        print (does_the_tweet_contain_key_word)
        
        try:        
            if does_the_tweet_contain_key_word >= 0:
                           
                user = tweet.user.screen_name #gets the user name
                print (user) ###prints the user's name

                # responds to a mention @dan_aldred           
                inkyphat.set_image(Image.open("/home/pi/StarWars/MENTION.png"))
                inkyphat.show()
                inkyphat.clear()

                ###### display message ####
                print (tweet_to_check)
                message = tweet_to_check
                txt = textwrap.fill(message, 31)
                w, h = inkyphat._draw.multiline_textsize(txt, font)
                x = (inkyphat.WIDTH / 2) - (w / 2)
                y = (inkyphat.HEIGHT / 2) - (h / 2)
                inkyphat._draw.multiline_text((x, y), txt, inkyphat.BLACK, font)
                inkyphat.show()

                time.sleep(2)
                inkyphat.clear()

            ### STAR WARS response
            elif does_the_tweet_contain_STAR_WARS >= 0:
                ### display SW intro picture ###
                print ("star wars picture")
                print ("star wars rleated tweet")
                inkyphat.set_image(Image.open("/home/pi/StarWars/STAR.png"))
                inkyphat.show()
                time.sleep(1)
                inkyphat.clear()

                # SHOW MESSAGE
                print (tweet_to_check)
                message = tweet_to_check
                txt = textwrap.fill(message, 31)
                w, h = inkyphat._draw.multiline_textsize(txt, font)
                x = (inkyphat.WIDTH / 2) - (w / 2)
                y = (inkyphat.HEIGHT / 2) - (h / 2)
                inkyphat._draw.multiline_text((x, y), txt, inkyphat.BLACK, font)
                inkyphat.show()

                time.sleep(10)
                inkyphat.clear()

            else:
                
                inkyphat.clear()
                pass

        except: ### if there is an emoji and the tweet cannot be displayed
               print ("Cannot render tweet")
               inkyphat.set_image(Image.open("/home/pi/StarWars/FAIL.png"))
               inkyphat.show()
               time.sleep(1)
               inkyphat.clear()

stream = tweepy.Stream(auth, Social_Media_Mirror_StreamListener())            
            
while True:
    stream.userstream()
