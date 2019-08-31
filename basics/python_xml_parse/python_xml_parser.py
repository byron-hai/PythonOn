#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@ Desc:
  module xml
@ author: byron
@ Date: 2019-08-31
@ History: 
"""

from xml.dom.minidom import parse

DOMTree = parse('songs.xml')
genre = DOMTree.documentElement

songs = genre.getElementsByTagName("song")
for song in songs:
    if song.hasAttribute("title"):
        print("Title: " + song.getAttribute("title"))

        artist = song.getElementsByTagName('artist')[0]
        year = song.getElementsByTagName('year')[0]
        album = song.getElementsByTagName('album')[0]
        print("Artist: " + artist.firstChild.data)
        print("Year: " + year.firstChild.data)
        print("Album: " + album.firstChild.data + "\n")
