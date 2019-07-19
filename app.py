from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask import send_file
from PIL import Image
import requests
from io import BytesIO

app = Flask(__name__)
api = Api(app)

class getImage(Resource):
    def get(self, layers):
        layerList = layers.split(',')
        
        args = request.args

        print(request.headers)
        
        coords = args['coord'].split(',')
        Zarg = str(coords[0]) #.encode("ascii")
        Yarg = str(coords[1]) #.encode("ascii")
        Xarg = str(coords[2]) #.encode("ascii")
        
        outImg = Image.new('RGBA', (256, 256), (255, 0, 0, 0))

        #If there is only one layer selected no need to process the image....just pass the response content directly. May speed up service?
        if(len(layerList) == 1):
            url = 'http://'+layerList[0].replace(':','/')+'/{0}/{1}/{2}'.format(Zarg,Yarg,Xarg)
            print(url)
            response = requests.get(url)
            print(response)
            if(response):
                # if no response this return will not happen. return outside if statement will return stream of empty Out image instantiated above
                return send_file(BytesIO(response.content), mimetype='image/png')
        else:
            for layer in layerList:
                url = 'http://'+layer.replace(':','/')+'/{0}/{1}/{2}'.format(Zarg,Yarg,Xarg)
                print(url)
                response = requests.get(url)
                if(response):
                    # if there is not a response in this itteration of the loop this will not composite anything onto the current state of outImg.
                    newLayer = Image.open(BytesIO(response.content)).convert('RGBA')
                    outImg = Image.alpha_composite(newLayer,outImg)

        imgByteArr = BytesIO()
        outImg.save(imgByteArr, format='PNG')

        return send_file(BytesIO(imgByteArr.getvalue()), mimetype='image/png')

    def printAThing(thingToPrint):
        print(str(thingToPrint))


api.add_resource(getImage,"/getImage/<string:layers>")

if __name__ == "__main__":
    app.run(debug=True)