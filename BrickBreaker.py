# NAMES: ANJANA GIRIDHAR
#        EVEY KRITER
# 
# DATE: 4/12/2019
# 
# ASSIGNMENT: HOMEWORK 10
# 
# CHALLENGES DONE: Restart on 'r' key
#                  Celebratory message when board clears
#                  Score-keeper in left corner
#                  Special orange bricks that need 2 hits to break


import turtle  # Using Turtle and Screen classes
import random  # Using randint

class Ball:
    """
    A class representing a ball on the screen
    
    Attributes
    ----------
    turtle : Turtle 
        A Turtle type object from the module turtle
    x : float
        The x coordinate of the ball
    y : float
        The y coordinate of the ball
    radius : float
        The radius of the ball
    velocity : list
        The x and y components of the velocity of the ball
    color : string
        The color of the ball
    
    Methods
    -------
    update()
        Update the ball location and exploding status each time it is called
    draw()
        Draw the ball on the screen
    
    collide_with_rect()
        Returns a string with the sides of the rectangle the ball hit
    """
    
    def __init__(self, t, x , y , radius, vx, vy, color):
        """
        Parameters
        ----------
        t : turtle
            A turtle type object from the module turtle
        radius : float
            The radius of the ball
        x : float
            The x coordinate of the ball
        y : float
            The y coordinate of the ball
        vx : float
            The x component of the ball velocity
        vy : float
            The y component of the ball velocity
        velocity : list
            The x and y components of the velocity of the ball
        color : string
            The color of the ball
        """
        # Store the parameters in the new object atributes
        self.turtle = t
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = [vx, vy]
        self.color = color
        
        
    def update(self, paddle, bricks):
        """
        Update the ball status:
        - Check if the ball should bounce off the window edges
        - Update position using the velocity
        """
        # Acquire the screen instance from the turtle
        screen = turtle.Screen()
        
        # Store current screen properties
        width = screen.window_width() 
        height = screen.window_height()
        
        # Check for boundaries
        if (self.x - self.radius <= -width//2) or (self.x + self.radius >= width//2):
            self.velocity[0] *= -1
        if (self.y + self.radius >= height//2):
            self.velocity[1] *= -1
        
        # Update position with velocity
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        
        # Check if we hit a paddle
        p = self.collide_with_rect(paddle)
        if len(p) > 0:
            if 't' in p:
                self.velocity[1] *= -1
            elif 'l' or 'r' in p:
                self.velocity[0] *= -1
            elif ('t') and ('l' or 'r') in p:
                self.velocity[1] *= -1
                
             
        # Check if we hit a brick
        for c in range(-1, (len(bricks) - 1)):
            b = self.collide_with_rect(bricks[c])
            if (len(b) - 1) >= 0:
                if 't' or 'b' in b:
                    #self.velocity[1] *= -1
                    if bricks[c].color == "brown":
                        bricks.remove(bricks[c])
                    elif bricks[c].color == "orange":
                        bricks[c].color = "brown"
                    self.velocity[1] *= -1

                elif 'l' or 'r' in b:
                    #self.velocity[0] *= -1
                    if bricks[c].color == "brown":
                        bricks.remove(bricks[c])
                    elif bricks[c].color == "orange":
                        bricks[c].color = "brown"
                    self.velocity[0] *= -1
                
                elif ('t') and ('l' or 'r') in b:
                    #self.velocity[0] *= -1
                    if bricks[c].color == "brown":
                        bricks.remove(bricks[c])
                    elif bricks[c].color == "orange":
                        bricks[c].color = "brown"
                    self.velocity[0] *= -1
                    
                elif ('b') and ('l' or 'r') in b:
                    #self.velocity[0] *= -1
                    if bricks[c].color == "brown":
                        bricks.remove(bricks[c])
                    elif bricks[c].color == "orange":
                        bricks[c].color = "brown"
                    self.velocity[0] *= -1
        
        
    def draw(self):
        """
        Draw the ball on the screen
        """
        self.turtle.penup()
        self.turtle.goto(self.x, self.y)
        self.turtle.pendown()
        self.turtle.dot(self.radius * 2, self.color)
    
    def collide_with_rect(self, rect):
        """
        Check if this ball is colliding with paddle/brick
        
        Parameters
        ----------
        rect : rectangle
            Another object to be checked for collision
        """
        faces = []
        
        # columns
        top = (rect.y + rect.height//2) <= (self.y - self.radius) <= (rect.y + rect.height)
        bottom = (rect.y) <= (self.y + self.radius) <= (rect.y + rect.height//2)
        right = (rect.x + rect.width//2) <= (self.x - self.radius) <= (rect.x + rect.width)
        left = (rect.x) <= (self.x + self.radius) <= (rect.x + rect.width//2)

        # Check for collision
        if top and (rect.x) <= self.x <= (rect.x + rect.width + self.radius): #top
            faces.append("t")
        
        elif bottom and (rect.x) <= self.x <= (rect.x + rect.width + self.radius): #bottom
            faces.append("b")

        elif right and (rect.y) <= self.y <= (rect.y + rect.height + self.radius): #right
            faces.append("r")
        
        elif left and (rect.y) <= self.y <= (rect.y + rect.height + self.radius): #left
            faces.append("l")
            
        return faces
    

class Game:
    """
    A class implementing the multiple ball scene
    
    Attributes
    ----------
    screen : Screen
        A Screen type object from the module turtle
    turtle : Turtle
        A Turtle type object from the module turtle
        
    
    Methods
    -------
    initialize_objs()
        Create the gamefield by adding the balls
    run()
        Determines the game dynamic frame by frame (one frame for each call)
    done()
        Exit the program
    """
    def __init__(self):
        # Create a screen object (singleton) and set it up
        self.screen = turtle.Screen()
        self.screen.setup(0.5, 0.5)  # Use half with and half height of your current screen
        self.screen.tracer(False)
        self.screen.colormode(255)
        
        # Create an invisible turtle object
        self.turtle = turtle.Turtle(visible=False)
        
        # Initialize the scene
        self.initialize_objs()
    
        # Defines users' interactions we should listen for
        self.screen.onkey(self.done, 'q')  # Check if user pushed 'q'
        self.screen.onkey(self.restart, 'r') # Check if user pushed 'r'
        #self.screen.onclick(self.add_ball) # Check if the user added a ball
        
        # As soon as the event loop is running, set up to call the self.run() method
        self.screen.ontimer(self.run, 0)
    
        # Tell the turtle screen to listen to the users' interactions
        self.screen.listen()
        
        # Start the event loop
        self.screen.mainloop()
        
    def initialize_objs(self):
        """
        Initializes the scene
        """
        # Defines the size of the game field       
        width = self.screen.window_width() - 20
        height = self.screen.window_height() - 20
        
        # Add inital ball to the game field       
        self.ball  = Ball(self.turtle,
                    0,                                      # X-location 
                    height//2 - 50,                         # Y-location
                    10,                                     # radius
                    4,                                    # velocity: x-component
                    4,                                    # velocity: y-component
                    (random.randint(0, 255),                # color: red
                     random.randint(0, 255),                # color: green
                     random.randint(0, 255)))               # color: blue
        
        # Add paddle to the game field
        self.paddle = Paddle(self.turtle, 100, 15, "blue")
        self.bricks = []
        for a in range(1, 3):
            for b in range(-3, 2):
                bricky = Brick(self.turtle,
                           b * 100,                         # X-location
                           a * 85,                          # Y-location
                           100,                             # width
                           50,                              # height
                           "brown")                         # color
                self.bricks.append(bricky)
            for c in range(2, 3):
                special = Brick(self.turtle,
                           c * 100,                         # X-location
                           a * 85,                          # Y-location
                           100,                             # width
                           50,                              # height
                           "orange")                         # color
                self.bricks.append(special)
        
        
    def run(self):
        """
        Determines the game dynamic frame by frame (one frame for each call)
        """
        # Clear the screen
        self.turtle.clear()
        
        #Update and draw current paddle
        self.paddle.update()
        self.paddle.draw()
        
        #Update and draw current bricks
        for i in range(len(self.bricks)):
            self.bricks[i].draw()
            
        # Update and draw current ball
        self.ball.update(self.paddle, self.bricks)
        self.ball.draw()
            
        # Update the overall screen
        self.screen.update()
        
        # Keep score
        score = (12 - len(self.bricks))
        turtle.clear()
        turtle.penup()
        turtle.goto(-550, 350)
        turtle.pendown()
        turtle.write("Score: " + str(score))
        turtle.update()
        turtle.hideturtle()
        
        # Call the self.run() method
        if len(self.bricks) == 0:
            turtle.color('green')
            style = ('Courier', 20, 'bold')
            turtle.penup()
            turtle.goto(-500, 250)
            turtle.pendown()
            turtle.write('You won! You hit all ' + str(score) + '/12' + ' bricks.', font=style)
            turtle.hideturtle()
            
        elif (self.ball.y - self.ball.radius <= (-self.screen.window_height()//2) - 11):
            turtle.color('black')
            style = ('Arial', 20, 'italic')
            turtle.penup()
            turtle.goto(-350, 300)
            turtle.pendown()
            turtle.write('Game over! You hit ' + str(score) + '/12' + ' bricks.', font=style)
            turtle.hideturtle()
        else:
            self.screen.ontimer(self.run, 0)

    def restart(self):
        self.screen.clear()
        game = Game()
        
    def done(self):
        """
        Exit the program
        """
        self.screen.bye()
        
        

class Paddle:
    """
    A class representing the paddle/rectangle.
    
    Attributes:
    -----------
    t : turtle
    width : width of paddle
    height : height of paddle
    color : color of paddle
    x : x-coordinate of paddle's lower left corner
    y : y-coordinate of paddle's lower left corner
    
    Methods:
    --------
    update() : sets position of the paddle based on mouse location
    draw() : draws the paddle on the screen
    
    """
    
    def __init__(self, t, width, height, color):
        self.turtle = t
        self.width = width
        self.height = height
        self.color = color
    
    def update(self):
        self.x = turtle.getcanvas().winfo_pointerx() - 2*turtle.getcanvas().winfo_rootx() - (self.width//2)
        self.y = -250
        
    def draw(self):
        self.turtle.pencolor(self.color)
        self.turtle.fillcolor(self.color)
        self.turtle.penup()
        self.turtle.goto(self.x, self.y)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.goto(self.x, self.y + self.height)
        self.turtle.goto(self.x + self.width, self.y + self.height)
        self.turtle.goto(self.x + self.width, self.y)
        self.turtle.goto(self.x , self.y)
        self.turtle.end_fill()
        
   
class Brick:
    '''
    A class representing the Bricks.
    
    Attributes:
    -----------
    t : turtle
    width : width of brick
    height : height of brick
    color : color of brick
    x : x-coordinate of upper left corner of brick
    y : y-coordinate of upper left corner of brick
    
    Methods:
    --------
    draw()
        draws the bricks
    
    '''
    
    def __init__(self, t, x, y, width, height, color):
        self.turtle = t
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    
    def draw(self):
        self.turtle.pencolor("black")
        self.turtle.fillcolor(self.color)
        self.turtle.penup()
        self.turtle.goto(self.x, self.y)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.goto(self.x, self.y + self.height)
        self.turtle.goto(self.x + self.width, self.y + self.height)
        self.turtle.goto(self.x + self.width, self.y)
        self.turtle.goto(self.x , self.y)
        self.turtle.end_fill()
        
    

# Draw the scene
game = Game()


