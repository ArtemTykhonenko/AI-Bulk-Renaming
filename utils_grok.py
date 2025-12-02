import os
import time
import base64
import requests
from pathlib import Path

def analyze_images_grok(image_paths, prompt, api_key):
    """
    Analyze images using Grok Vision API from X.AI
    Uncensored, supports explicit content
    """
    results = {}
    total = len(image_paths)
    
    for idx, path in enumerate(image_paths, 1):
        filename = Path(path).name
        print(f"Processing {idx}/{total}: {filename}")
        
        try:
            # Read and encode image to base64
            with open(path, 'rb') as f:
                image_data = base64.b64encode(f.read()).decode('utf-8')
            
            # Determine image format
            ext = Path(path).suffix.lower()
            mime_type = {
                '.jpg': 'image/jpeg',
                '.jpeg': 'image/jpeg',
                '.png': 'image/png',
                '.webp': 'image/webp'
            }.get(ext, 'image/jpeg')
            
        except Exception as e:
            print(f"Error reading {filename}: {e}")
            continue

        # Call Grok Vision API
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = requests.post(
                    'https://api.x.ai/v1/chat/completions',
                    headers={
                        'Content-Type': 'application/json',
                        'Authorization': f'Bearer {api_key}'
                    },
                    json={
                        'messages': [
                            {
                                'role': 'user',
                                'content': [
                                    {
                                        'type': 'text',
                                        'text': prompt
                                    },
                                    {
                                        'type': 'image_url',
                                        'image_url': {
                                            'url': f'data:{mime_type};base64,{image_data}'
                                        }
                                    }
                                ]
                            }
                        ],
                        'model': 'grok-2-vision-1212',
                        'temperature': 0.7,
                        'max_tokens': 1000,  # Allow longer descriptions
                        'stream': False
                    },
                    timeout=120
                )
                
                if response.status_code == 200:
                    result = response.json()
                    text = result['choices'][0]['message']['content'].strip()
                    
                    if text:
                        results[filename] = text
                        print(f"Success: {filename} -> {text[:50]}...")
                        break
                    else:
                        print(f"Empty response for {filename}")
                        break
                else:
                    error_msg = response.text
                    print(f"Error {response.status_code} for {filename}: {error_msg}")
                    
                    # Retry on rate limit
                    if response.status_code == 429:
                        wait_time = (2 ** attempt) + 1
                        print(f"Rate limit. Retrying in {wait_time}s...")
                        time.sleep(wait_time)
                    else:
                        break
                    
            except Exception as e:
                print(f"Error analyzing {filename}: {e}")
                break
        
        # Small delay between images
        if idx < total:
            time.sleep(1)

    return results

def rename_images(folder_path, name_dict):
    folder = Path(folder_path)
    
    # Calculate max filename length based on folder path
    # Windows max path = 260 chars total
    folder_path_length = len(str(folder))
    max_extension_length = 10  # .jpeg is longest common extension
    max_filename_length = 260 - folder_path_length - max_extension_length - 2  # -2 for path separator and safety
    
    print(f"Max filename length for this folder: {max_filename_length} chars")
    
    for old_name, new_desc in name_dict.items():
        old_path = folder / old_name
        if old_path.exists():
            # Sanitize new name: remove invalid chars
            new_name = "".join(c for c in new_desc if c.isalnum() or c in (' ', '-', '_')).rstrip()
            
            # Limit to calculated max length
            if len(new_name) > max_filename_length:
                new_name = new_name[:max_filename_length]
                print(f"Truncated filename to {max_filename_length} chars")
            
            ext = old_path.suffix
            new_path = folder / (new_name + ext)
            counter = 1
            while new_path.exists():
                # Handle duplicates
                suffix = f"_{counter}"
                max_name_with_suffix = max_filename_length - len(suffix)
                new_path = folder / f"{new_name[:max_name_with_suffix]}{suffix}{ext}"
                counter += 1
            try:
                old_path.rename(new_path)
                print(f"Renamed {old_name} to {new_path.name}")
            except Exception as e:
                print(f"Error renaming {old_name}: {e}")
