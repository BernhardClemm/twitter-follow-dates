#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 17:25:37 2019

@author: bernhardclemm
"""

from datetime import datetime

def following_dates(follower_list): 
    
    # Recode all "created_at" time stamps into datetime format
    for follower in follower_list:
        follower["created_at"] = datetime.strptime(follower["created_at"], "%a %b %d %H:%M:%S %z %Y")
    
    # Create variable that takes on date of most recent follower during loop, starting with oldest
    most_recent = follower_list[-1]["created_at"]
    
    # Loop through followers starting from oldest one (end of list)
    for follower in reversed(follower_list):
        created_at = follower["created_at"]
        if created_at <= most_recent: 
            follower["followed_at_earliest"] = most_recent
        else:
            follower["followed_at_earliest"] = created_at
            most_recent = created_at
        