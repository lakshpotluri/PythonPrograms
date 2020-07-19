import turtle;
f = turtle.Pen();
f.shape("turtle");
f.color("blue");
f.circle(100);
f.left(90);
for i in range(24):
    f.forward(100)
    f.right(180)
    f.forward(100)
    f.up()
    f.left(90)
    f.circle(100,15)
    f.down()
    f.left(90)



