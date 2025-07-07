from youtube_comments import get_video_comments
from analyze_comments import predict_sentiments

# Replace with your YouTube video ID
video_id = "lVbElR_HwXQ"  # Example

# Fetch comments
comments = get_video_comments(video_id)
print(f"Fetched {len(comments)} comments.")

# Check if comments exist
if comments:
    # Predict sentiments
    sentiments = predict_sentiments(comments)

    # Show results
    for comment, sentiment in zip(comments, sentiments):
        print(f"[{sentiment}] {comment}")
else:
    print("No comments found. Please check video ID or API key.")
