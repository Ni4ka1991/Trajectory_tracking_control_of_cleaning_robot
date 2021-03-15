#!/usr/bin/env Python3



#DATA

step_right_m = 5
step_down_m  = 4
step_left_m  = 3
step_up_m    = 2

coordinate_x0_m = 12
coordinate_y0_m = 8

#LOGIC

all_path_m = step_right_m + step_down_m + step_left_m + step_up_m  #Calculale how many steps the robot took

coordinate_x4_m = ( coordinate_x0_m + step_right_m - step_left_m )
coordinete_y4_m = ( coordinate_y0_m - step_down_m + step_up_m )

delta_right = abs( coordinate_x4_m - coordinate_x0_m )
delta_down  = abs ( coordinate_y4_m - coordinate_y0_m )


#VIEW

print ( "1. All steps taken by the cleaning robot is: \n", all_path_m )
print ( "2. New coordinates of cleaning robot is: " )
print ( "3. The delta of cleaning robot is: "  )
