# Instagram Bot Using Instabot

This guide will help you set up and use the `instabot` library to perform various actions on Instagram, such as logging in, following a user, uploading a photo, liking posts, commenting on posts, and sending direct messages.

## Requirements

- Python 3.x
- `instabot` library

## Installation

First, you need to install the `instabot` library. You can do this using pip:

```sh
pip install instabot
```

## Step-by-Step Guide

### 1. Import Libraries

```python
from instabot import Bot
import os
```

### 2. Initialize the Bot

```python
# Initialize the bot
bot = Bot()
```

### 3. Remove Previous Session (if any)

```python
# Remove previous session if any
if os.path.exists("config"):
    import shutil
    shutil.rmtree("config")
```

### 4. Login to Instagram

```python
# Login to Instagram
bot.login(username="coffin___xp", password="2jd*(VMCX@i^2_(")
```

### 5. Follow a User

```python
# Follow a user
bot.follow("salik_seraj_naik")
```

### 6. Upload a Photo with a Caption

```python
# Upload a photo with a caption
bot.upload_photo("C:/Users/Salik/OneDrive/Pictures/Screenshots/Saved Pictures/wallpaper.jpg", caption="We are Anonymous")
```

### 7. Get User ID

```python
# Get user ID
user_id = bot.get_user_id_from_username("salik_seraj_naik")
```

### 8. Get Last 3 Posts of the User

```python
# Get last 3 posts of the user
user_posts = bot.get_user_medias(user_id, filtration=False)[:3]
```

### 9. Like the Last 3 Posts

```python
# Like the last 3 posts
for post in user_posts:
    bot.like(post)
```

### 10. Comment on the First Post

```python
# Comment on the first post
bot.comment(user_posts[0], "Nice post!")
```

### 11. Send a Direct Message

```python
# Send a direct message
bot.send_message("Hello! This is a bot message.", ["salik_seraj_naik"])
```

### 12. Complete the Bot Actions

```python
print("Bot actions completed!")
```

## Complete Script

```python
from instabot import Bot
import os

# Initialize the bot
bot = Bot()

# Remove previous session if any
if os.path.exists("config"):
    import shutil
    shutil.rmtree("config")

# Login to Instagram
bot.login(username="coffin___xp", password="2jd*(VMCX@i^2_(")

# Follow a user
bot.follow("salik_seraj_naik")

# Upload a photo with a caption
bot.upload_photo("C:/Users/Salik/OneDrive/Pictures/Screenshots/Saved Pictures/wallpaper.jpg", caption="We are Anonymous")

# Get user ID
user_id = bot.get_user_id_from_username("salik_seraj_naik")

# Get last 3 posts of the user
user_posts = bot.get_user_medias(user_id, filtration=False)[:3]

# Like the last 3 posts
for post in user_posts:
    bot.like(post)

# Comment on the first post
bot.comment(user_posts[0], "Nice post!")

# Send a direct message
bot.send_message("Hello! This is a bot message.", ["salik_seraj_naik"])

print("Bot actions completed!")
```


## Follow Me

If you found this guide helpful, follow me for more tutorials and projects on GitHub and other social media platforms!

- [GitHub](https://github.com/Salik-Seraj)
- [X](https://twitter.com/code_with_ssn)
- [LinkedIn](https://linkedin.com/in/salik-seraj-naik)
- [Personal Website](https://linktr.ee/SalikSerajNaik)