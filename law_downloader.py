import pandas as pd

def downloader(url):
    !wget url
    
    fname = url.split('/')[-1]
    print(f"Downloaded file name : {fname}")
    
    if "zip" in fname:
        !unzip "*.zip"
        !rm -rf *.zip"
    
