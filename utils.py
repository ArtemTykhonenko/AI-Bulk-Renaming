import os
import json
import time
import random
import google.generativeai as genai
from pathlib import Path

def analyze_images(image_paths, prompt, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('models/gemini-2.0-flash-exp')

    results = {}
    total = len(image_paths)
    
    for idx, path in enumerate(image_paths, 1):
        filename = Path(path).name
        print(f"Processing {idx}/{total}: {filename}")
        
        try:
            # Upload single image
            img = genai.upload_file(path)
        except Exception as e:
            print(f"Error uploading {filename}: {e}")
            continue

        # Single image prompt - no JSON needed
        full_prompt = f"{prompt} Provide only the description text, no JSON, no formatting."
        
        max_retries = 5
        for attempt in range(max_retries):
            try:
                response = model.generate_content([full_prompt, img])
                text = response.text.strip()
                
                if not text:
                    print(f"DEBUG: Empty response for {filename}")
                    break
                
                # Store the description directly
                results[filename] = text
                print(f"Success: {filename} -> {text[:50]}...")
                
                # Success, break retry loop
                break
            except Exception as e:
                if "429" in str(e):
                    wait_time = (2 ** (attempt + 1)) + random.uniform(0, 1)
                    print(f"Rate limit hit for {filename}. Retrying in {wait_time:.2f}s...")
                    time.sleep(wait_time)
                else:
                    print(f"Error analyzing {filename}: {e}")
                    break
        
        # Delay between images to avoid rate limits
        if idx < total:  # Don't delay after the last image
            time.sleep(5)

    return results

def rename_images(folder_path, name_dict):
    folder = Path(folder_path)
    for old_name, new_desc in name_dict.items():
        old_path = folder / old_name
        if old_path.exists():
            # Sanitize new name: remove invalid chars, limit length
            new_name = "".join(c for c in new_desc if c.isalnum() or c in (' ', '-', '_')).rstrip()
            new_name = new_name[:50]  # limit length
            ext = old_path.suffix
            new_path = folder / (new_name + ext)
            counter = 1
            while new_path.exists():
                new_path = folder / f"{new_name}_{counter}{ext}"
                counter += 1
            try:
                old_path.rename(new_path)
                print(f"Renamed {old_name} to {new_path.name}")
            except Exception as e:
                print(f"Error renaming {old_name}: {e}")