import picamera,time
camera = picamera.PiCamera()
camera.resolution = (1440, 1080)
#camera.hflip = True
#camera.vflip = True

#camera.sharpness = 0
#camera.contrast = 0
#camera.brightness = 50
#camera.saturation = 0
#camera.ISO = 0
#camera.video_stabilization = False
#camera.exposure_compensation = 0
#camera.exposure_mode = 'auto'
#camera.meter_mode = 'average'
#camera.awb_mode = 'auto'
#camera.image_effect = 'none'
#camera.color_effects = None
#camera.rotation = 180
#camera.hflip = False
#camera.vflip = False
#camera.crop = (0.0, 0.0, 1.0, 1.0)



camera.start_preview()
time.sleep(5)
camera.capture('image.jpg')
camera.stop_preview()
