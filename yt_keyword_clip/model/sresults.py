class SResults:
    def __init__(self, ytvideo, cap_content, cap_time):
        self.ytvideo = ytvideo
        self.cap_content = cap_content
        self.cap_time = cap_time

    def __str__(self):
        return f"<Found at: {self.ytvideo}>"

    def __repr__(self):
        content = " | ".join([
            "caption = " + str(self.cap_content),
            "timestamp = " + str(self.cap_time)
        ])
        return f"<Found at: {self.ytvideo} : {content}>"

