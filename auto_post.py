import json, os, requests

TOKEN = os.environ["LINKEDIN_ACCESS_TOKEN"]
AUTHOR_URN = os.environ["LINKEDIN_PERSON_URN"] # e.g., "urn:li:person:YOUR_ID"

with open("posts_queue.json", "r", encoding="utf-8") as f:
    queue = json.load(f)

# Find the next unposted post
next_post = next((item for item in queue if not item["posted"]), None)
if not next_post:
    print("All queued posts are already published!")
    exit(0)

content_text = next_post["content"]

# NEW MAGIC: Automatically convert normal text into LinkedIn API Mentions
if "mentions" in next_post:
    for mention in next_post["mentions"]:
        # Example: Converts "IBM" into "@[IBM](urn:li:organization:1009)"
        mention_tag = f"@[{mention['text']}]({mention['urn']})"
        content_text = content_text.replace(mention["text"], mention_tag)

# Using the newer /rest/posts API
url = "https://api.linkedin.com/rest/posts"
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "LinkedIn-Version": "202409", # Required for new rest APIs
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

# Catch errors clearly
if res.status_code != 201:
    print("Error from LinkedIn:", res.text)
res.raise_for_status()

# Mark as posted and save
next_post["posted"] = True
with open("posts_queue.json", "w", encoding="utf-8") as f:
    json.dump(queue, f, indent=2, ensure_ascii=False)

print(f"Successfully published Day {next_post['day']} with Mentions!")
