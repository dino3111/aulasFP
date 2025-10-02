# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle

def main():
    screen = turtle.Screen()
    t = turtle.Turtle()

    # Use t.up(), t.down() and t.goto(x, y)
    def desenho(drawing):
        with open(drawing, "r") as file:
            for line in file:
                line = line.strip()
                if line == "UP":
                    t.up()
                elif line == "DOWN":
                    t.down()
                else:
                    cordenadas = line.split(" ")
                    x = int(cordenadas[0])
                    y = int(cordenadas[1])
                    t.goto(x,y)
    desenho("drawing.txt")
    
    
                    



    # Wait until window is closed
    screen.mainloop()


if __name__ == "__main__":
    main()

