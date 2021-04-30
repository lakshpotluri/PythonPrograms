import turtle;
f=turtle.Pen();
f.shape("turtle");
f.color("black");
f.speed(10)
a=300;
b=60;

f.forward(b);
f.left(90);
f.forward(b);
f.left(90);
f.forward(a);
f.left(90);
f.forward(b);
f.left(90);
f.forward(a);
f.right(90);
f.forward(b);
f.right(90);
f.forward(a);
f.right(90);
f.forward(b);
f.left(180);
f.forward(b*2);
f.left(90);
f.forward(a);
f.left(90);
f.forward(b);
f.left(90);
f.forward(a/2);
f.right(180);
f.color("blue");
f.circle(b/2);
f.left(90);
for i in range(24):
    f.forward(b/2)
    f.right(180)
    f.forward(b/2)
    f.up()
    f.left(90)
    f.circle(b/2,15)
    f.down()
    f.left(90)
f.right(90)
f.color("black");
f.forward(a/2)
f.right(90)
f.color("green");
for i in range(b):
    f.right(90)
    f.forward(a);
    f.left(90);
    f.forward(1)
    f.left(90);
    f.forward(a);
    f.right(90);
f.color("black");
f.right(180);
f.forward(b*3);
f.color("orange");
f.left(90);
for i in range(b//2):
    f.forward(a);
    f.left(90);
    f.forward(1);
    f.left(90);
    f.forward(a);
    f.right(90);
    f.forward(1);
    f.right(90);




