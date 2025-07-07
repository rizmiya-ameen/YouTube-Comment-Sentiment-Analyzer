from flask import Flask, request, render_template
from analyze_comments import predict_sentiments
from youtube_comments import get_video_comments
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def analyze_video(video_id):
    if not video_id:
        return {"error": "video_id is required"}

    comments = get_video_comments(video_id)
    predictions = predict_sentiments(comments)

    positive = predictions.count("Positive")
    negative = predictions.count("Negative")
    neutral = predictions.count("Neutral")

    summary = {
        "positive": positive,
        "negative": negative,
        "neutral": neutral,
        "num_comments": len(comments),
        "rating": (positive / len(comments)) * 100 if len(comments) > 0 else 0
    }

    return {"predictions": predictions, "comments": comments, "summary": summary}

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = None
    comments = []
    if request.method == 'POST':
        video_url = request.form.get('video_url')
        if "v=" in video_url:
            video_id = video_url.split("v=")[1].split("&")[0]
            data = analyze_video(video_id)

            summary = data['summary']
            comments = list(zip(data['comments'], data['predictions']))
        else:
            summary = {"error": "Invalid video URL"}
    return render_template('index.html', summary=summary, comments=comments)

if __name__ == '__main__':
    app.run(debug=True)
