import sys

if (len(sys.argv) > 1):
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    vertices = len([line for line in lines if line.startswith('v ')])
    faces = len([line for line in lines if line.startswith('f ')])

    print("NUMBER OF VERTICES: " + str(vertices))
    print("NUMBER OF FACES: " + str(faces))

else :
    print("usage is [objfilepath]")