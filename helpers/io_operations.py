""" Functions relating to data reading and writing """
import json
import os
import pickle as pkl
import yaml
import csv

def save_eye_images_as_png(all_eye_images: list[dict]) -> None:
    for image_data in all_eye_images:
        timestamp, byte_string = image_data['device_time_stamp'], image_data['image_data']
        with open(f"images/{timestamp}.png", "wb") as image_file:
            image_file.write(byte_string)

def write_file(data, filepath: str):
    file_format = filepath.split('.')[-1]
    legal_formats = ['json', 'csv', 'pkl', 'psydat', 'yaml']
    if file_format not in legal_formats:
        raise ValueError(f"Invalid format. Must be {', '.join(legal_formats[:-1])} or {legal_formats[-1]}")

    folder_path = os.path.dirname(filepath)
    if folder_path and not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    if file_format in ['pkl', 'psydat']: 
        with open(filepath, 'wb') as file:
            pkl.dump(data, file)

    elif file_format == 'json':
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=2)

    elif file_format == 'yaml':
        with open(filepath, 'w') as file:
            yaml.dump(data, file)

    elif file_format == 'csv':
        with open(filepath, 'w', newline='') as f:
            # Use dictwriter if list of dicts
            if data and isinstance(data[0], dict):
                fieldnames = data[0].keys()
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
            # Else use normal writer
            else: 
                writer = csv.writer(f)
            writer.writerows(data)