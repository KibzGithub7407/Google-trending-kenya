from pytrends.request import TrendReq
from datetime import date, datetime

# Setup
pytrends = TrendReq(hl='en-US', tz=180)
try:
    df = pytrends.trending_searches(pn='kenya')
    print("Fetched DataFrame:")
    print(df)
    if df.empty or 0 not in df.columns:
        raise ValueError("Trending searches DataFrame is empty or column 0 does not exist.")
    top = df[0].tolist()[:5]
except Exception as e:
    print("Error fetching or processing trends:", e)
    top = ["No trends available"]

today = date.today().strftime("%B %d, %Y")
now = datetime.now().strftime("%H:%M:%S")

# Post
post = f"🌍 *Top Google Trends in Kenya – {today} at {now}* 🇰🇪\n\n"
post += "\n".join(f"{i+1}. 🔥 *{trend}* – here's why it matters..." for i, trend in enumerate(top))
post += "\n\n#KenyaTrends #TrendingNow #Elimuhub"

# Save with timestamp
with open("daily_trends_post.txt", "w", encoding="utf-8") as f:
    f.write(post)

print(post)
