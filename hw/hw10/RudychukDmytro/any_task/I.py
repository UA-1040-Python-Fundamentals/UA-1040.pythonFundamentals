# DESCRIPTION:
# Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.

# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

class Ball:
    def __init__(self, ballType="regular"):
        self.ballType = ballType

ball1 = Ball()
ball2 = Ball("super")

print(ball1.ballType)
print(ball2.ballType)  