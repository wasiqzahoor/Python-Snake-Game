import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.width = 400
        self.height = 400
        self.cell_size = 20
        self.direction = 'Right'
        self.running = True
        self.score = 0
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.place_food()
        self.canvas = tk.Canvas(master, width=self.width, height=self.height, bg='black')
        self.canvas.pack()
        self.master.bind('<KeyPress>', self.change_direction)
        self.update()

    def place_food(self):
        while True:
            x = random.randrange(0, self.width, self.cell_size)
            y = random.randrange(0, self.height, self.cell_size)
            if (x, y) not in self.snake:
                return (x, y)

    def change_direction(self, event):
        key = event.keysym
        opposites = {'Up':'Down', 'Down':'Up', 'Left':'Right', 'Right':'Left'}
        if key in ['Up', 'Down', 'Left', 'Right'] and opposites.get(key) != self.direction:
            self.direction = key

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == 'Up':
            head_y -= self.cell_size
        elif self.direction == 'Down':
            head_y += self.cell_size
        elif self.direction == 'Left':
            head_x -= self.cell_size
        elif self.direction == 'Right':
            head_x += self.cell_size
        new_head = (head_x, head_y)
        if (new_head in self.snake or
            head_x < 0 or head_x >= self.width or
            head_y < 0 or head_y >= self.height):
            self.running = False
            return
        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            self.food = self.place_food()
        else:
            self.snake.pop()

    def draw(self):
        self.canvas.delete('all')
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+self.cell_size, y+self.cell_size, fill='green')
        fx, fy = self.food
        self.canvas.create_rectangle(fx, fy, fx+self.cell_size, fy+self.cell_size, fill='red')
        self.canvas.create_text(50, 10, fill='white', text=f'Score: {self.score}', anchor='nw')
        if not self.running:
            self.canvas.create_text(self.width//2, self.height//2, fill='white', text='Game Over', font=('Arial', 24))

    def update(self):
        if self.running:
            self.move_snake()
            self.draw()
            self.master.after(100, self.update)
        else:
            self.draw()

if __name__ == '__main__':
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()