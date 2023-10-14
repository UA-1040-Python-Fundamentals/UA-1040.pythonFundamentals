class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

# Test
if __name__ == "__main__":
    ball1 = Ball()
    print(f"Ball 1 Type: {ball1.ball_type}")

    ball2 = Ball("super")
    print(f"Ball 2 Type: {ball2.ball_type}")

