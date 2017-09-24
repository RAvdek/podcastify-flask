# Podcastify

**Because reading is for nerds and you're not multi-tasking enough!**

Podcastify is a web app which which plays news articles as audio.

# How to get it running

0. If you don't do a lot of python dev, you should run `pip install -r requirements.txt` to install dependencies.
1. Create an account on [Voice RSS](http://www.voicerss.org/login.aspx) and get an API key.
2. Copy and paste your key into `run.sh`.
3. `bash run.sh` will start the web app on your computer running at 127.0.0.1:5000
4. Plug in a URL to `/article?url=blahblah` and listen!

Here's an example:

http://127.0.0.1:5000/article?url=https://www.nytimes.com/2017/09/24/sports/nfl-trump-anthem-protests.html
