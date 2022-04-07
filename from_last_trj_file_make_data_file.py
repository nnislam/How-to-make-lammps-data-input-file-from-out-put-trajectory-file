file_lamps_trj = open('peptoid1.lammpstrj','r')
file_atom = open('peptoid_just_Atom_2.data','r') #just_atom_section_from_data_file
file_Vel = open('peptoid_just_Velocity_2.data','r') #just_velocity_section_from_data_file

output_trj = open('out_Final_trj','w')
output_ATOM = open('output_Atom','w')
output_VEL = open('output_Vel','w')

file_lamps_trj_read = file_lamps_trj.readlines()
file_atom_read =file_atom.readlines()
file_Vel_read =file_Vel.readlines()

for line in range(len(file_lamps_trj_read)):
    if file_lamps_trj_read[line] == 'ITEM: TIMESTEP\n':
        if file_lamps_trj_read[line+1] == '2481000\n': #last_step_number_intrj_file
            line9 = file_lamps_trj_read[line+9:]
            for i in line9:
                i_split = i.split()
                output_trj.write(str(i_split[2]) + ' ' + str(i_split[3]) + ' ' + str(i_split[4]) + ' ' + str(i_split[5]) + ' ' + str(i_split[6]) + ' ' +str(i_split[7]) +  '\n')

file_lamps_trj.close()
output_trj.close()

output_trj_again = open('out_Final_trj','r')
output_trj_read = output_trj_again.readlines()
for line in range(len(file_atom_read)):
    file_atom_read_line_split = (file_atom_read[line]).split()
    file_Vel_read_line_split = (file_Vel_read[line]).split()
    output_trj_read_split = (output_trj_read[line]).split()
    vel_str = str(file_Vel_read_line_split[0]) + " " + str(output_trj_read_split[3]) +' ' + str(output_trj_read_split[4]) +' ' + str(output_trj_read_split[5]) +'\n'
    atom_str = str(file_atom_read_line_split[0]) +  " " + str(file_atom_read_line_split[1]) + " " + str(file_atom_read_line_split[2]) + " " + str(file_atom_read_line_split[3]) + " " +str(output_trj_read_split[0]) + ' ' + str(output_trj_read_split[1]) + ' ' + str(output_trj_read_split[2]) + '\n'
    output_ATOM.write(atom_str)
    output_VEL.write(vel_str)
output_trj_again.close()  
file_atom.close()
file_Vel.close()
output_ATOM.close()
output_VEL.close()
