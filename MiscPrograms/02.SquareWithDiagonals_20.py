import turtle;
import math;
f=turtle.Pen();
f.shape("turtle");
f.color("blue");
for i in range(4):
    f.forward(100);
    f.left(90);
f.left(45);
f.forward(math.sqrt(math.pow(100,2)+math.pow(100,2)));
f.left(135);
f.forward(100);
f.left(135);
f.forward(math.sqrt(math.pow(100,2)+math.pow(100,2)));
