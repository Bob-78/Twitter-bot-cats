# Twitter-bot-cats

This is a Python Twitter bot for deployment on Heroku

With regular intervals, it fetches a random image of a cat, posts it to twitter, and then follows some cat lovers. 
I can be modified easily to follow other things. 

To get it up and running on Heroku
1. Install Heroku
2. Open a terminal in the app folder
3. git init
4. heroku create app-name
5. git add . 
6. git commit -m "commitmessage"
7. git push heroku master
8. set the environment variables: (replace "secret" with your codes from https://developer.twitter.com)

- heroku config:set access_secret=secret
- heroku config:set access_token=secret
- heroku config:set consumer_key=secret
- heroku config:set consumer_secret=secret

9. heroku ps:scale worker=1

Procfile (no extension) should contain the following line:
worker: python main.py

requirements.txt should contain the list of modules needed for the app to run
You can generate the file with:
1. pip freeze > requirements.txt.

Push to github:
https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/


