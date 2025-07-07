from youtube_comments import get_video_comments

# Replace with the video ID you want to scrape
video_id = "lVbElR_HwXQ"  # Example: "dQw4w9WgXcQ" (Rickroll)

# Fetch comments
comments = get_video_comments(video_id)

print(f"Fetched {len(comments)} comments.")
print("Sample comments:")
for c in comments[:10]:
    print("-", c)
