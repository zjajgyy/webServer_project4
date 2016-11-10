from flask import Flask, request, Response
import os
import imghdr
from PIL import Image
from io import BytesIO

app = Flask(__name__)
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpeg', 'bmp', 'gif'])

def isnum(num):
  try:
    if(float(num) > 0):
      return True
    else:
      return False
  except ValueError:
    return False

@app.route('/resize', methods=['POST', 'GET'])
def resize():
  upload_file = request.files['media']
  scale = request.args.get('scale')
  if (scale == "" or scale == None):
    scale = "1"
  elif (isnum(scale)):
    scale = scale
  else:
    scale = "fail"
  
  if (isnum(scale)):
    scale = float(scale)
    if scale!=0 and upload_file:
      try:
        im = Image.open(upload_file)
      except OSError:
        return Response(status=400)
      (width, height) = im.size
      imageType = im.format
      print(width*scale, height*scale)
      out = im.resize((int(width*scale), int(height*scale)), Image.ANTIALIAS)
      #im.thumbnail((int(width*scale), int(height*scale)))
      byte_io = BytesIO()
      out.save(byte_io, imageType)
      byte_io.seek(0)
      return Response(byte_io, mimetype="image/"+imageType)
    else:
      return Response(status=400)
  else :
    return Response(status=400)

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8889)

