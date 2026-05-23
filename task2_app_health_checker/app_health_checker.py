import requests
import time
import logging

# Setup log file
logging.basicConfig(
    filename='app_health.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

print("="*40)
print("  Application Health Checker Report")
print("="*40)

# List of websites to check
urls = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.facebook.com"
]

# Check each website
for url in urls:
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    response_time = round(end_time - start_time, 2)
    
    
    print(f"Checking: {url}")
    logging.info(f"Checking: {url}")

    print(f"Status Code: {response.status_code}")
    logging.info(f"Status Code: {response.status_code}")

    print(f"Response Time: {response_time} seconds")
    logging.info(f"Response Time: {response_time} seconds")

    if response.status_code == 200:
        print(f"Status: UP ✅")
        logging.info(f"Status: UP")
    else:
        print(f"Status: DOWN ❌")
        logging.warning(f"Status: Down")
    

    if response_time > 3:
       print(f"⚠️ WARNING: Slow response time!")
       logging.warning(f"WARNING SLOW RESPONSE TIME")
    else:
       print(f"Response time is good ✅")
       logging.info(f"Response time is good ")
    print("-" * 40)

print("="*40)
print("  Check complete! See app_health.log")
print("="*40)