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
bot.follow("modi")

# Upload a photo with a caption
bot.upload_photo("C:/Users/naitro/OneDrive/Pictures/Screenshots/Saved Pictures/wallpaper.jpg", caption="We are Anonymous")

# Get user ID
user_id = bot.get_user_id_from_username("modi")

# Get last 3 posts of the user
user_posts = bot.get_user_medias(user_id, filtration=False)[:3]

# Like the last 3 posts
for post in user_posts:
    bot.like(post)

# Comment on the first post
bot.comment(user_posts[0], "Nice post!")

# Send a direct message
bot.send_message("Hello! This is a bot message.", ["modi"])

print("Bot actions completed!")
