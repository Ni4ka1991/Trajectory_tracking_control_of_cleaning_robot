#!/usr/bin/env Python3

#DATA

#Robot paths

step_right_m = 5     #Meters
step_down_m  = 4
step_left_m  = 3
step_up_m    = 2


#LOGIC

all_path_m = step_right_m + step_down_m + step_left_m + step_up_m  #Calculale how many steps/meters the robot took
delta_right = step_right_m - step_left_m
delta_down  = step_down_m  - step_up_m


#VIEW

print ( "1. All steps taken by the cleaning robot is: ", all_path_m )
print ( "2. The delta of cleaning robot is: right -  %d m; down - %d m"%( delta_right, delta_down ))
