"""
Bouncing Logo		
		
The original  code is available at https://nostarch.com/big-book-small-python-programming		

"""		
        
import sys, random, time		
import bext       
import os

#cmd = 'mode 50,20'
cmd = 'mode 12,6'
os.system(cmd)
        
# Set up the constants:		
WIDTH, HEIGHT = bext.size()		
# We can't print to the last column on Windows without it adding a		
# newline automatically, so reduce the width by one:		
WIDTH -= 1		
        
		
#COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']		
        
UP_RIGHT   = 'ur'		
UP_LEFT    = 'ul'		
DOWN_RIGHT = 'dr'		
DOWN_LEFT  = 'dl'		
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)		
        
# Key names for logo dictionaries:		
COLOR = 'color'		
X = 'x'		
Y = 'y'		
DIR = 'direction'		
        
        
def main():		
    bext.clear()       		
        
    cornerBounces = 0  # Count how many times a logo hits a corner.	
    nonCornerBounces = 0

    logo = {X: random.randint(1, WIDTH - 2),		
            Y: random.randint(1, HEIGHT - 2),		
            DIR: random.choice(DIRECTIONS)}
    if logo[X] % 2 == 1:		
    # Make sure X is even so it can hit the corner.		
        logo[X] -= 1
    while True:  # Main program loop.		
        # for logo in logos:  # Handle each logo in the logos list.		
        #     # Erase the logo's current location:		
        bext.goto(logo[X], logo[Y])		
        print('   ', end='')  # (!) Try commenting this line out.		
    
        # See if the logo bounces off the corners:		
        if logo[X] == 0 and logo[Y] == 0:		
            logo[DIR] = DOWN_RIGHT		
            cornerBounces += 1		
        elif logo[X] == 0 and logo[Y] == HEIGHT - 1:		
            logo[DIR] = UP_RIGHT		
            cornerBounces += 1		
        elif logo[X] == WIDTH - 1 and logo[Y] == 0:		
            logo[DIR] = DOWN_LEFT		
            cornerBounces += 1		
        elif logo[X] == WIDTH - 1 and logo[Y] == HEIGHT - 1:		
            logo[DIR] = UP_LEFT		
            cornerBounces += 1		
    
        # See if the logo bounces off the left edge:		
        elif logo[X] == 0 and logo[DIR] == UP_LEFT:		
            logo[DIR] = UP_RIGHT	
            nonCornerBounces +=1	
        elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:		
            logo[DIR] = DOWN_RIGHT	
            nonCornerBounces +=1	
    
        # See if the logo bounces off the right edge:		
        # (WIDTH - 1 because the logo takes up 1 char)		
        elif logo[X] == WIDTH - 1 and logo[DIR] == UP_RIGHT:		
            logo[DIR] = UP_LEFT	
            nonCornerBounces +=1	
        elif logo[X] == WIDTH - 1 and logo[DIR] == DOWN_RIGHT:		
            logo[DIR] = DOWN_LEFT	
            nonCornerBounces +=1	
    
        # See if the logo bounces off the top edge:		
        elif logo[Y] == 0 and logo[DIR] == UP_LEFT:		
            logo[DIR] = DOWN_LEFT
            nonCornerBounces +=1		
        elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:		
            logo[DIR] = DOWN_RIGHT	
            nonCornerBounces +=1	
    
        # See if the logo bounces off the bottom edge:		
        elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:		
            logo[DIR] = UP_LEFT	
            nonCornerBounces +=1	
        elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:		
            logo[DIR] = UP_RIGHT
            nonCornerBounces +=1		

         
        # Move the logo. (X moves by 2 because the terminal		
        # characters are twice as tall as they are wide.)		
        if logo[DIR] == UP_RIGHT:		
            logo[X] += 1		
            logo[Y] -= 1		
        elif logo[DIR] == UP_LEFT:		
            logo[X] -= 1		
            logo[Y] -= 1		
        elif logo[DIR] == DOWN_RIGHT:		
            logo[X] += 1		
            logo[Y] += 1		
        elif logo[DIR] == DOWN_LEFT:		
            logo[X] -= 1		
            logo[Y] += 1		
        
        # # Display number of corner bounces:		
        # bext.goto(5, 0)		
        # bext.fg('white')		
        # print('Corner bounces:', cornerBounces, end='')		
        
        # bext.goto(5, 1)		
        # bext.fg('white')		
        # print('Bounces:', nonCornerBounces, end='')	
        
        if cornerBounces > 0:
            bext.goto(5, 0)		
            bext.fg('white')		
            print('Ratio:', round(nonCornerBounces/cornerBounces, 2), end='')	        

        # for logo in logos:		
            # Draw the logos at their new location:		
        bext.goto(logo[X], logo[Y])		
        print('■', end='')		
            
        bext.goto(0, 0)		
        
        sys.stdout.flush()  # (Required for bext-using programs.)		
        time.sleep(.01)		
        
        
# If this program was run (instead of imported), run the game:		
if __name__ == '__main__':		
    try:		
        main()		
    except KeyboardInterrupt:		
        print()		
        print('Bouncing DVD Logo, by Al Sweigart and modified by Eric Kleppen')		
        sys.exit()  # When Ctrl-C is pressed, end the program.	
