
import os

# image data with PILLOW
from PIL import Image
from PIL.ExifTags import TAGS

def main() -> None:
    
    folder: str = os.getcwd()
    
    # print(f"\nFolder: {folder} \nFiles:")
    # listOfFiles: list[str] = os.listdir(folder)
    # for files in listOfFiles:
    #     print(files)
    
    filepath = folder + '\\' + '20250202_113750.jpg'
    #print (filepath)

    file_data = FileData(filepath)
    
    for label, value in file_data.items():
        print(f"{label:25} {value}")
    

def FileData(_filepath : str):# -> dict[str, Any] | None:
    
    readImageData = Image.open(_filepath)
    dataDict = {
        "filename": readImageData.filename,
        "size": readImageData.size,
        "width": readImageData.width,
        "height": readImageData.height,
        "format": readImageData.format,
        "mode": readImageData.mode,
        "gps": readImageData.info.get("gps"),
    }
    # for label,value in datadict.items():
    #     print(f"{label:25} {value}")
    
    # extract EXIF data
    exifData = readImageData.getexif()
    
    for tag_id in exifData:
        # get the tag name, instead of unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        data = exifData.get(tag_id)
        # decode bytes
        if isinstance(data, bytes):
            data = data.decode()
        #print(f"{tag:25} {data}")
        # add to dictionary
        new_key = str(tag)
        new_value = data
        dataDict[new_key] = new_value
    
    # return dataDict
    return dataDict
        

if __name__ == "__main__":
    main()
    
    
