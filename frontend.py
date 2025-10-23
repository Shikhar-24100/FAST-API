import aiohttp
import asyncio
import pandas as pd
from tqdm.asyncio import tqdm
import time

# pick a few interesting Stack Exchange sites
SITES = [
    "philosophy", "psychology", "academia",
    "history", "politics", "writers", "english"
]

API_BASE = "https://api.stackexchange.com/2.3"
TARGET = 1500
MIN_LEN = 300
MAX_LEN = 3000


async def fetch_answers(session, site, page):
    url = f"{API_BASE}/answers"
    params = {
        'page': page,
        'pagesize': 100,
        'order': 'desc',
        'sort': 'votes',
        'site': site,
        'filter': 'withbody'
    }
    
    try:
        async with session.get(url, params=params) as resp:
            if resp.status != 200:
                print(f"❌ Error {resp.status} for {site} page {page}")
                return []
            
            # Stack Exchange API returns gzipped JSON by default
            data = await resp.json()
            
            # Check for API errors
            if 'error_id' in data:
                print(f"❌ API Error: {data.get('error_message', 'Unknown error')}")
                return []
            
            # Check quota
            quota = data.get('quota_remaining', 'unknown')
            if page == 1:
                print(f"   API quota remaining: {quota}")
            
            return data.get("items", [])
            
    except Exception as e:
        print(f"❌ Exception fetching {site} page {page}: {e}")
        return []


async def gather_all():
    # Add headers to identify your app (good practice for Stack Exchange API)
    headers = {
        'User-Agent': 'StackExchange Answer Collector/1.0'
    }
    
    async with aiohttp.ClientSession(headers=headers) as session:
        all_rows = []
        
        for site in SITES:
            print(f"\n🔍 Collecting from {site}.stackexchange.com …")
            
            for page in tqdm(range(1, 16)):
                answers = await fetch_answers(session, site, page)
                
                if not answers:
                    print(f"   No answers returned for page {page}")
                    break
                
                filtered_count = 0
                for a in answers:
                    body = a.get("body_markdown", "").strip()
                    if MIN_LEN <= len(body) <= MAX_LEN:
                        all_rows.append({
                            "site": site,
                            "answer_id": a["answer_id"],
                            "question_id": a["question_id"],
                            "score": a["score"],
                            "is_accepted": a.get("is_accepted", False),
                            "text": body
                        })
                        filtered_count += 1
                
                if page == 1:
                    print(f"   Found {len(answers)} answers, {filtered_count} match length criteria")
                
                # Be nice to the API - small delay between requests
                await asyncio.sleep(0.1)
                
                if len(all_rows) >= TARGET:
                    print(f"\n🎯 Reached target of {TARGET} answers!")
                    return all_rows
        
        return all_rows


def main():
    rows = asyncio.run(gather_all())
    
    if not rows:
        print("\n❌ No rows collected! Check API errors above.")
        return
    
    df = pd.DataFrame(rows)
    print(f"\n📊 Collected {len(df)} total answers")
    
    df.drop_duplicates(subset=["text"], inplace=True)
    print(f"📊 After deduplication: {len(df)} unique answers")
    
    df = df.sample(min(len(df), TARGET))
    df.to_csv("stackexchange_answers.csv", index=False, encoding="utf-8-sig")
    
    print(f"\n✅ Saved {len(df)} detailed answers to stackexchange_answers.csv")
    print(f"📈 Score range: {df['score'].min()} to {df['score'].max()}")
    print(f"📏 Length range: {df['text'].str.len().min()} to {df['text'].str.len().max()} chars")


if __name__ == "__main__":
    main()