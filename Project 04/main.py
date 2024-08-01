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