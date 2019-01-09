# InstaScrape
A lightweight instagram scraper that extracts all image links from a list of instagram accounts. This gets around security techniques like randomly generated html class names and forcing users to scroll down to view more images.

This script is meant to work in conjunction with a secondary process that builds a corpus of images to train statistical models for image detection/recognition. A problem I ran into early on working on image recognition was programatically getting thousands of images from the internet. This script helps collect a relatively annoying source of images.

## Methods

The scraper goes out to the url using selenium and tells the driver to scroll down, wait 3 seconds, and keep scrolling until it has reached the end of the page. After each scroll, the HTML data is grabbed and parsed so that each additional page is captured individually. This is to combat a somewhat persistent problem of the body of the HTML replacing itself instead of appending each scroll.

At the end of the loop, the parsed code is searched for the string value '/p/' and returns just the suffix of the individual image URL.
