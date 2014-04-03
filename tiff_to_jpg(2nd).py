for f in [file for file in files if file.lower().endswith('.tif')]:
# If a jpeg is already present. Don't do anything.
filename, extension=f.split('.')
jpgfile="%s.jpg" % filename
jpgpath=os.path.join(root, jpgfile)
# If a jpeg is *NOT* present, create one from the tiff.
if not os.path.isfile(jpgpath):
try:
im = Image.open(os.path.join(root,f))
print "Generating jpeg for %s" % f
im.thumbnail(im.size)
im.save(jpgpath, "JPEG", quality=100)
except Exception, e:
print e

continue

print "A jpeg file already exists for %s" % f