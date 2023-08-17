import curses
from  curses import wrapper
def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    BLUE_AND_YELLOW= curses.color_pair(1)
    GREEN_AND_GREY= curses.color_pair(2)
    
    stdscr.clear()
    stdscr.addstr(1,1, "Hello WOrld")
    stdscr.addstr(4,4, "0. Have a Latte                   Go for the up button",BLUE_AND_YELLOW)
    stdscr.addstr(6,4, "1. Have a chocolate coffee        Go for down button button",GREEN_AND_GREY)
    stdscr.addstr(8,4, "2. Have some snacks               Go for the right button",GREEN_AND_GREY)
    stdscr.addstr(10,4,"3. Want the Wifi password         Go for the enter button",GREEN_AND_GREY)

    stdscr.addstr(16,1, "****--------*****")
    
    stdscr.refresh()
    z= True
    selected_option=0
    while(z==True):
        a= stdscr.getkey()
        if (a=="KEY_UP" or a=="KEY_DOWN"):
            
            if (a=="KEY_UP"):
                if (selected_option!=0):
                    selected_option-=1
                    if (selected_option==1):
                        stdscr.addstr(6,4, "1. Have a chocolate coffee        Go for down button button",BLUE_AND_YELLOW)
                        stdscr.addstr(4,4, "0. Have a Latte                   Go for the up button",GREEN_AND_GREY)
                        
                        stdscr.addstr(8,4, "2. Have some snacks               Go for the right button",GREEN_AND_GREY)
                        stdscr.addstr(10,4,"3. Want the Wifi password         Go for the enter button",GREEN_AND_GREY)
                    elif(selected_option==2):
                        stdscr.addstr(8,4, "2. Have some snacks               Go for the right button",BLUE_AND_YELLOW)
                        stdscr.addstr(4,4, "0. Have a Latte                   Go for the up button",GREEN_AND_GREY)
                        stdscr.addstr(6,4, "1. Have a chocolate coffee        Go for down button button",GREEN_AND_GREY)
                        stdscr.addstr(10,4,"3. Want the Wifi password         Go for the enter button",GREEN_AND_GREY)
                    elif(selected_option==3):
                        stdscr.addstr(10,4,"3. Want the Wifi password         Go for the enter button",BLUE_AND_YELLOW)
                        stdscr.addstr(8,4, "2. Have some snacks               Go for the right button",GREEN_AND_GREY)
                        stdscr.addstr(4,4, "0. Have a Latte                   Go for the up button",GREEN_AND_GREY)
                        stdscr.addstr(6,4, "1. Have a chocolate coffee        Go for down button button",GREEN_AND_GREY)

                else:
                    selected_option=0
                    stdscr.addstr(4,4, "0. Have a Latte                   Go for the up button",BLUE_AND_YELLOW)
                    stdscr.addstr(6,4, "1. Have a chocolate coffee        Go for down button button",GREEN_AND_GREY)
                    stdscr.addstr(8,4, "2. Have some snacks               Go for the right button",GREEN_AND_GREY)
                    stdscr.addstr(10,4,"3. Want the Wifi password         Go for the enter button",GREEN_AND_GREY)
            elif (a=="KEY_DOWN"):
                if (selected_option==3):
                    selected_option=3
                    stdscr.addstr(10,4,"3. Want the Wifi password         Go for the enter button",BLUE_AND_YELLOW)
                    stdscr.addstr(8,4, "2. Have some snacks               Go for the right button",GREEN_AND_GREY)
                    stdscr.addstr(4,4, "0. Have a Latte                   Go for the up button",GREEN_AND_GREY)
                    stdscr.addstr(6,4, "1. Have a chocolate coffee        Go for down button button",GREEN_AND_GREY)
                elif (selected_option<3):
                    selected_option+=1
                    if (selected_option==1):
                        stdscr.addstr(6,4, "1. Have a chocolate coffee        Go for down button button",BLUE_AND_YELLOW)
                        stdscr.addstr(4,4, "0. Have a Latte                   Go for the up button",GREEN_AND_GREY)                       
                        stdscr.addstr(8,4, "2. Have some snacks               Go for the right button",GREEN_AND_GREY)
                        stdscr.addstr(10,4,"3. Want the Wifi password         Go for the enter button",GREEN_AND_GREY)
                    elif(selected_option==2):
                        stdscr.addstr(8,4, "2. Have some snacks               Go for the right button",BLUE_AND_YELLOW)
                        stdscr.addstr(4,4, "0. Have a Latte                   Go for the up button",GREEN_AND_GREY)
                        stdscr.addstr(6,4, "1. Have a chocolate coffee        Go for down button button",GREEN_AND_GREY)
                        stdscr.addstr(10,4,"3. Want the Wifi password         Go for the enter button",GREEN_AND_GREY)
                    elif(selected_option==3):
                        stdscr.addstr(10,4,"3. Want the Wifi password         Go for the enter button",BLUE_AND_YELLOW)
                        stdscr.addstr(8,4, "2. Have some snacks               Go for the right button",GREEN_AND_GREY)
                        stdscr.addstr(4,4, "0. Have a Latte                   Go for the up button",GREEN_AND_GREY)
                        stdscr.addstr(6,4, "1. Have a chocolate coffee        Go for down button button",GREEN_AND_GREY)
        else:
            z=False
                
    
    stdscr.addstr(14,4,f"You have selected the option : {selected_option}", GREEN_AND_GREY)
    stdscr.addstr(15,4,"Press Enter ")
    b= stdscr.getkey()
    if (selected_option==0):
        print("Have your Latte")
    elif(selected_option==1):
        print("Have your chocolate coffee")
    elif(selected_option==2):
        print("Have some snacks it contains sandwiches and biscuits")
    else:        
        print("Here is the wifi password: 123456789")
   
wrapper(main)


# Try using __name__ == '__main__' as the main function, because every professional space looks for these
