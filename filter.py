class Filter:

    @staticmethod
    def bonjour(text):
        content = ""
        b = False
        n_space = 0
        for i in text:
            if i != "\n":
                b = True
                n_space = 0
            if i == "\n" and b:
                n_space += 1
            if b and n_space < 2:
                content += i
        return content
