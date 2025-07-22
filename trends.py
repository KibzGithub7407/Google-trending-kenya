from pytrends.request import TrendReq
from datetime import date, datetime

# Setup
pytrends = TrendReq(hl='en-US', tz=180)
df = pytrends.trending_searches(pn='kenya')

today = date.today().strftime("%B %d, %Y")
now = datetime.now().strftime("%H:%M:%S")
top = df[0].tolist()[:5]

# Post
post = f"🌍 *Top Google Trends in Kenya – {today} at {now}* 🇰🇪\n\n"
post += "\n".join(f"{i+1}. 🔥 *{trend}* – here's why it matters..." for i, trend in enumerate(top))
post += "\n\n#KenyaTrends #TrendingNow #Elimuhub"

# Save with timestamp
with open("daily_trends_post.txt", "w", encoding="utf-8") as f:
    f.write(post)

print(post)
