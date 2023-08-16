from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import StreamingResponse
import base64, io, uvicorn
from app import process_api
import os, cv2, shutil

async def save_input_files(inputs, source):
    try:
        with open(inputs.filename, 'wb') as f:
            shutil.copyfileobj(inputs.file, f)
    
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        inputs.file.close()

    try:
        with open(source.filename, 'wb') as f:
            shutil.copyfileobj(source.file, f)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        source.file.close()
        
app = FastAPI()

@app.post('/faceswap/v1/img-img')
async def img_img(
    input_type: str = Form(...),
    image: UploadFile = File(...),
    source: UploadFile = File(...), 
):
    
    print(input_type)
    save_input_files(image, source)
    image_path, source_path = image.filename, source.filename
    mask_includes = [
        "Skin",
        "R-Eyebrow",
        "L-Eyebrow",
        "L-Eye",
        "R-Eye",
        "Nose",
        "Mouth",
        "L-Lip",
        "U-Lip"
    ]
    specifics = (None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
    
    output_file = process_api(
        input_type,
        image_path,
        None,
        None,
        source_path,
        None,
        'Result',
        False,
        'All Face',
        25,
        0.6,
        'NONE',
        False,
        mask_includes,
        17,
        10,
        0.1,
        0.15,
        1,
        True,
        0,
        511,
        0,
        511,
        *specifics,
    )
    img = open(output_file, 'rb')
    return StreamingResponse(io.BytesIO(img.read()), media_type="image/png")

@app.post('/faceswap/v1/img-img/hq')
def img_img_hq(
    input_type: str = Form(...),
    image_path: str = Form(...),
    source_path: str = Form(...),
):
    mask_includes = [
        "Skin",
        "R-Eyebrow",
        "L-Eyebrow",
        "L-Eye",
        "R-Eye",
        "Nose",
        "Mouth",
        "L-Lip",
        "U-Lip"
    ]
    specifics = (None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
    
    output_file = process_api(
        input_type,
        image_path,
        None,
        None,
        source_path,
        None,
        'Result',
        False,
        'All Face',
        25,
        0.6,
        'GFPGAN',
        True,
        mask_includes,
        17,
        10,
        0.1,
        0.15,
        1,
        True,
        0,
        511,
        0,
        511,
        *specifics,
    )
    img = open(output_file, 'rb')
    return StreamingResponse(io.BytesIO(img.read()), media_type="image/png")


@app.post('/faceswap/v1/img-vid')
def img_vid(
    input_type: str = Form(...),
    video_path: str = Form(...),
    source_path: str = Form(...),
):
    mask_includes = [
        "Skin",
        "R-Eyebrow",
        "L-Eyebrow",
        "L-Eye",
        "R-Eye",
        "Nose",
        "Mouth",
        "L-Lip",
        "U-Lip"
    ]
    specifics = (None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
    
    output_file = process_api(
        input_type,
        None,
        video_path,
        None,
        source_path,
        None,
        'Result',
        False,
        'All Face',
        25,
        0.6,
        'NONE',
        False,
        mask_includes,
        17,
        10,
        0.1,
        0.15,
        1,
        True,
        0,
        511,
        0,
        511,
        *specifics,
    )
    vid = open(output_file, 'rb')
    return StreamingResponse(io.BytesIO(vid.read()), media_type="image/mp4")
@app.post('/faceswap/v1/img-vid/hq')
def img_vid_hq(
    input_type: str = Form(...),
    video_path: str = Form(...),
    source_path: str = Form(...),
):
    mask_includes = [
        "Skin",
        "R-Eyebrow",
        "L-Eyebrow",
        "L-Eye",
        "R-Eye",
        "Nose",
        "Mouth",
        "L-Lip",
        "U-Lip"
    ]
    specifics = (None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
    
    output_file = process_api(
        input_type,
        None,
        video_path,
        None,
        source_path,
        None,
        'Result',
        False,
        'All Face',
        25,
        0.6,
        'GFPGAN',
        True,
        mask_includes,
        17,
        10,
        0.1,
        0.15,
        1,
        True,
        0,
        511,
        0,
        511,
        *specifics,
    )
    vid = open(output_file, 'rb')
    return StreamingResponse(io.BytesIO(vid.read()), media_type="image/mp4")



if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.1", port=7000)
    