import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

def diagnose_x():
    api_key = os.getenv("X_API_KEY")
    api_secret = os.getenv("X_API_SECRET")
    access_token = os.getenv("X_ACCESS_TOKEN")
    access_secret = os.getenv("X_ACCESS_SECRET")
    
    print("Checking X.com Credentials...")
    
    # Try to authenticate with OAuth 1.0a (required for DMs)
    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
    api = tweepy.API(auth)
    
    try:
        user = api.verify_credentials()
        print(f"Successfully authenticated as: @{user.screen_name}")
        
        # Test DM permission specifically
        print("Testing DM permission status...")
        # This will likely throw the 403 error if the tier or permission is wrong
        api.get_direct_messages(count=1)
        print("SUCCESS: Your account has DM permissions.")
        
    except tweepy.TweepyException as e:
        print(f"\nDIAGNOSIS ERROR: {e}")
        if "403 Forbidden" in str(e):
            print("\nPOSSIBLE CAUSES:")
            print("1. Your X account is on the 'Free' tier (DMs require 'Basic' tier).")
            print("2. The 'Direct Message' permission was not enabled when tokens were generated.")
            print("3. OAuth 1.0a is not enabled in 'User authentication settings'.")

if __name__ == "__main__":
    diagnose_x()
