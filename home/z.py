import os
import json
c = 'dishes'
def get_media_type(file_extension):
    image_extensions = ['.jpg', '.jpeg', '.png', '.webp', '.gif' , '.jfif']
    video_extensions = ['.mp4', '.webm', '.avi', '.mov']
    
    if file_extension.lower() in image_extensions:
        return 'image'
    elif file_extension.lower() in video_extensions:
        return 'video'
    else:
        return None

def create_media_array(root_dir):
    media_array = []

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, root_dir)
            file_extension = os.path.splitext(file)[1]
            
            media_type = get_media_type(file_extension)
            
            if media_type:
                media_item = { 'type': media_type, 'src': ""+c+"\\"+relative_path.replace('\\', '\\\\')}
                media_array.append(media_item)

    return media_array

def main():
    root_directory = 'D:\VS Code\Web Dev\love\ChetnaMoksh06042022.github.io\home\\'+c
    
    if not os.path.isdir(root_directory):
        print("The specified directory does not exist.")
        return

    media_array = create_media_array(root_directory)

    # Print the array
    print(json.dumps(media_array, indent=4))

    # Optionally, save to a JSON file
    with open('media_array.json', 'w') as f:
        json.dump(media_array, f, indent=4)
    
    print(f"\nMedia array has been saved to 'media_array.json'")
    print(f"Total items: {len(media_array)}")

if __name__ == "__main__":
    main()