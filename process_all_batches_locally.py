#!/usr/bin/env python3
"""
ChatGPT Plugin Registration URLs Extractor
Process all 4 batches and extract OAUTH registration URLs
Run this script on your local machine with: python3 process_all_batches_locally.py
"""

import json
import subprocess
import time
import sys

# Configuration
TOKEN = "eyJhbGciOiJSUzI1NiIsImtpZCI6IldjNzdXREtWTkN2N1ZYSGxqZUhzZjZZUjFhM3I3MmxYMnhJdG9zaVF4NHciLCJ0eXAiOiJKV1QifQ.eyJhdWQiOlsiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS92MSJdLCJjbGllbnRfaWQiOiJhcHBfWDh6WTZ2VzJwUTl0UjNkRTduSzFqTDVnSCIsImh0dHBzOi8vYXBpLm9wZW5haS5jb20vYXV0aCI6eyJhbXIiOlsidXJuOm9wZW5haTphbXI6Z29vZ2xlIl0sImNoYXRncHRfYWNjb3VudF9pZCI6IjM4MWJkMjgzLTkwNDctNGJjMy05YTMxLTgxN2ExZmNlMDJjMiIsImNoYXRncHRfYWNjb3VudF91c2VyX2lkIjoidXNlci1jRHhURG1TSEU2YnJkZTlOaFpFU2JvbmFfXzM4MWJkMjgzLTkwNDctNGJjMy05YTMxLTgxN2ExZmNlMDJjMiIsImNoYXRncHRfY29tcHV0ZV9yZXNpZGVuY3kiOiJub19jb25zdHJhaW50IiwiY2hhdGdwdF9wbGFuX3R5cGUiOiJmcmVlIiwiY2hhdGdwdF91c2VyX2lkIjoidXNlci1jRHhURG1TSEU2YnJkZTlOaFpFU2JvbmEiLCJ1c2VyX2lkIjoidXNlci1jRHhURG1TSEU2YnJkZTlOaFpFU2JvbmEifSwiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS9wcm9maWxlIjp7ImVtYWlsIjoidHJhdmVsb2thZmJAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZhbWlseV9uYW1lIjoiS2F1c2hpayIsImdpdmVuX25hbWUiOiJOaWtoaWwiLCJuYW1lIjoiTmlraGlsIEthdXNoaWsiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jS3hnZkQwdzAxZk9mTllYVXZCMmFsaFRuV0xmRnl4LURiUTgxX2lEbERKRlNKWjJ3PXM5Ni1jIn0sImlzcyI6Imh0dHBzOi8vYXV0aC5vcGVuYWkuY29tIiwicHdkX2F1dGhfdGltZSI6MTc4NDQ1ODgwOTMwOCwic2NwIjpbIm9wZW5pZCIsImVtYWlsIiwicHJvZmlsZSIsIm9mZmxpbmVfYWNjZXNzIiwibW9kZWwucmVxdWVzdCIsIm1vZGVsLnJlYWQiLCJvcmdhbml6YXRpb24ucmVhZCIsIm9yZ2FuaXphdGlvbi53cml0ZSJdLCJzZXNzaW9uX2lkIjoiYXV0aHNlc3NfbzBQUVNuWU9hejFVWkJjRWt6b3Q1SFlmIiwic2wiOnRydWUsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA2ODEwNzEyOTE2ODMzMzkzNTAzIiwiaWF0IjoxNzg0NDU4ODEwLCJleHAiOjE3ODUzMjI4MTAsImp0aSI6IjA0YjBkMDlkZWVjYzQxNjM5ZjE0NmQ3MzYyY2YxODFiIiwibmJmIjoxNzg0NDU4ODEwfQ.CUUSm2WdGHlVkRgCbqvizZU4_TDjEUT3Uqs9UEF3Xc4N3yt4-UhLbKAena8bLIRgtT5Cnoyn5sx9MbxNppqBtWrsv85fogmK4hHIM6QZLINCLtyqUWgP1b2kxoaVvVLBuOyYJnxjrmMGzR0T6i-F4bDDO5BIuA-AptRKmQEegAj2WVVTeTL42nFixXiNlLiq7rK9rQ0MoJssOe7qpqffDUev__g2TZdfYUbIBK-rinz8L0P6ptBDC9wWa6vDM_IjV3z3EtQTvVJERMAr-e1c5aGHdLDlmZG5Bp6CAthdjbaNs6bHE2E6yUCrqnOU8lXvtjrJnOpJK6Tuki6zu6nTYw"
API_URL = "https://chatgpt.com/backend-api/apps/content?detail=full&platform=chat&locale=en-US"
BATCH_FILES = [
    "/home/user/batch_1_data.json",
    "/home/user/batch_2_data.json",
    "/home/user/batch_3_data.json",
    "/home/user/batch_4_data.json"
]

def make_request(batch_num, app_ids):
    """Make API request for a batch of app IDs"""
    print(f"\n{'='*80}")
    print(f"BATCH {batch_num} - {len(app_ids)} IDs")
    print(f"{'='*80}")
    
    # Create payload
    payload = json.dumps({"app_ids": app_ids})
    
    # Build curl command
    curl_cmd = [
        'curl', '-s',
        '-X', 'POST',
        API_URL,
        '-H', 'accept: */*',
        '-H', 'accept-language: en-US,en;q=0.9',
        '-H', f'authorization: Bearer {TOKEN}',
        '-H', 'content-type: application/json',
        '-H', 'oai-client-build-number: 8370486',
        '-H', 'oai-client-version: prod-fb4a8a2a751dfec391053cfd7b01c52699ccf78c',
        '-H', 'oai-device-id: f41a8a64-bfa3-4106-b107-b8d89e9fe5c3',
        '-H', 'oai-language: en-US',
        '-H', 'oai-session-id: 09312c80-98bb-4122-bc11-2a13af711ab8',
        '-H', 'origin: https://chatgpt.com',
        '-H', 'referer: https://chatgpt.com/plugins?category=finance',
        '-H', 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0',
        '--data-raw', payload
    ]
    
    try:
        result = subprocess.run(curl_cmd, capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            try:
                response = json.loads(result.stdout)
                apps = response.get('apps', [])
                print(f"✅ SUCCESS - {len(apps)} apps returned")
                return apps
            except json.JSONDecodeError as e:
                print(f"❌ JSON Parse Error: {str(e)[:100]}")
                print(f"Response preview: {result.stdout[:200]}")
                return None
        else:
            print(f"❌ Curl Error: {result.stderr[:200]}")
            return None
    except subprocess.TimeoutExpired:
        print(f"❌ Request Timeout")
        return None
    except Exception as e:
        print(f"❌ Exception: {str(e)}")
        return None

def extract_registration_urls(apps):
    """Extract OAUTH registration URLs from apps"""
    urls = []
    
    for app in apps:
        app_id = app.get('id', 'N/A')
        app_name = app.get('name', 'N/A')
        
        supported_auth = app.get('supported_auth', [])
        for auth in supported_auth:
            if auth.get('type') == 'OAUTH':
                registration_url = auth.get('registration_url')
                if registration_url:
                    urls.append({
                        'app_id': app_id,
                        'app_name': app_name,
                        'registration_url': registration_url
                    })
                    print(f"  ✓ {app_name}: {registration_url}")
    
    return urls

def main():
    """Main function"""
    print("\n" + "="*80)
    print("ChatGPT Plugin Registration URLs Extractor")
    print("="*80)
    
    all_urls = []
    
    # Process each batch
    for batch_num in range(1, 5):
        batch_file = BATCH_FILES[batch_num - 1]
        
        try:
            with open(batch_file, 'r') as f:
                batch_data = json.load(f)
            
            app_ids = batch_data.get('app_ids', [])
            
            # Make request
            apps = make_request(batch_num, app_ids)
            
            if apps:
                # Extract URLs
                urls = extract_registration_urls(apps)
                all_urls.extend(urls)
                print(f"  Found {len(urls)} registration URLs")
            
            # Rate limiting
            if batch_num < 4:
                print(f"\n⏳ Waiting 3 seconds before next batch...")
                time.sleep(3)
        
        except FileNotFoundError:
            print(f"❌ File not found: {batch_file}")
        except Exception as e:
            print(f"❌ Error processing batch {batch_num}: {str(e)}")
    
    # Save results
    print(f"\n{'='*80}")
    print(f"FINAL RESULTS")
    print(f"{'='*80}")
    print(f"Total registration URLs found: {len(all_urls)}")
    
    # Save JSON
    with open('/home/user/all_registration_urls_final.json', 'w') as f:
        json.dump(all_urls, f, indent=2)
    print(f"✅ Saved to: /home/user/all_registration_urls_final.json")
    
    # Save CSV
    with open('/home/user/all_registration_urls_final.csv', 'w') as f:
        f.write("app_id,app_name,registration_url\n")
        for item in all_urls:
            app_name = item['app_name'].replace('"', '""')
            f.write(f"{item['app_id']},\"{app_name}\",{item['registration_url']}\n")
    print(f"✅ Saved to: /home/user/all_registration_urls_final.csv")
    
    # Print summary
    print(f"\n{'='*80}")
    print(f"REGISTRATION URLS BY APP:")
    print(f"{'='*80}")
    for i, item in enumerate(all_urls, 1):
        print(f"{i}. {item['app_name']}")
        print(f"   ID: {item['app_id']}")
        print(f"   URL: {item['registration_url']}\n")

if __name__ == "__main__":
    main()
