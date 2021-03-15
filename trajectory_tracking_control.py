#!/usr/bin/env Python3




#DATA
 
  #Initial robot position

coordinate_x0_m = 0 #Meters 
coordinate_y0_m = 0 
 
  #Robot paths

step_right_m = 6     #Meters
step_down_m  = 7
step_left_m  = 3
step_up_m    = 2


#LOGIC

all_path_m = step_right_m + step_down_m + step_left_m + step_up_m  #Calculale how many steps/meters the robot took

  #New position calculate

coordinate_x4_m = ( coordinate_x0_m + step_right_m - step_left_m ) #Meters
coordinate_y4_m = ( coordinate_y0_m - step_down_m + step_up_m )

  #Calculate displacement of cleaning robot 

delta_right = abs( coordinate_x4_m - coordinate_x0_m )  #Meters
delta_down = abs ( coordinate_y4_m - coordinate_y0_m )


#VIEW

print ( "1. All steps taken by the cleaning robot is: ", all_path_m )
print ( "2. The delta of cleaning robot is: right -  %d m; down - %d m"%( delta_right, delta_down ))
