from fastapi import FastAPI, HTTPException, Query
import requests

app = FastAPI()

@app.get("/sub.php")
def fetch_nid(
    action: str = Query(None),
    nid: str = Query(None),
    dob: str = Query(None)
):
    # যদি action=fetch এবং nid ও dob দেওয়া থাকে
    if action == "fetch" and nid and dob:
        target_url = f"http://rexogod.page.gd/sub.php?action=fetch&nid={nid}&dob={dob}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 14; CPH2621 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/151.0.7922.199 Mobile Safari/537.36',
            'Accept': 'application/json',
            'Cookie': '__test=84bc0fc5e78f30a71d2b6d181a9e3503'
        }
        
        try:
            # মূল API-এ রিকোয়েস্ট পাঠানো
            response = requests.get(target_url, headers=headers)
            data = response.json()
            
            # সফল হলে api_owner পরিবর্তন করে @keretoi167 বসিয়ে দেওয়া
            if data and data.get("success"):
                data["api_owner"] = "@keretoi167"
                
            return data
            
        except Exception as e:
            return {
                "code": 500,
                "success": False,
                "message": "Internal Server Error or Upstream API down.",
                "error": str(e),
                "api_owner": "@keretoi167"
            }
    else:
        return {
            "code": 400,
            "success": False,
            "message": "Invalid parameters! Please provide action=fetch, nid, and dob.",
            "api_owner": "@keretoi167"
        }
      
