import json, os, re, requests

TOKEN = os.environ["LINKEDIN_ACCESS_TOKEN"]
AUTHOR_URN = os.environ["LINKEDIN_PERSON_URN"]

def escape_little_text(text):
    # LinkedIn Little Text Format के reserved characters को escape करता है (hashtags को छोड़कर)
    text = re.sub(r'([\\|{}@\[\]()<>*_~])', r'\\\1', text)
    text = re.sub(r'#(?![A-Za-z0-9])', r'\#', text)
    return text

with open("posts_queue.json", "r", encoding="utf-8") as f:
    queue = json.load(f)

next_post = next((item for item in queue if not item["posted"]), None)
if not next_post:
    print("All queued posts are already published!")
    exit(0)

# 1. पहले सामान्य टेक्स्ट के ब्रैकेट्स ( ) और सिंबल्स को सुरक्षित (escape) करें
content_text = escape_little_text(next_post["content"])

# 2. अब Mentions को @[Name](urn) फॉर्मेट में बदलें ताकि वे नीले टैग बनें
if "mentions" in next_post:
    for mention in next_post["mentions"]:
        escaped_name = escape_little_text(mention["text"])
        mention_tag = f"@[{mention['text']}]({mention['urn']})"
        content_text = content_text.replace(escaped_name, mention_tag)

url = "https://api.linkedin.com/rest/posts"
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "LinkedIn-Version": "202610",
    "X-Restli-Protocol-Version": "2.0.0",
    "Content-Type": "application/json"
}

payload = {
    "author": AUTHOR_URN,
    "commentary": content_text,
    "visibility": "PUBLIC",
    "distribution": {
        "feedDistribution": "MAIN_FEED"
    },
    "lifecycleState": "PUBLISHED",
    "isReshareDisabledByAuthor": False
}

res = requests.post(url, headers=headers, json=payload)

if res.status_code != 201:
    print("Error from LinkedIn:", res.text)
res.raise_for_status()

next_post["posted"] = True
with open("posts_queue.json", "w", encoding="utf-8") as f:
    json.dump(queue, f, indent=2, ensure_ascii=False)

print(f"Successfully published Day {next_post['day']} with Mentions!")
