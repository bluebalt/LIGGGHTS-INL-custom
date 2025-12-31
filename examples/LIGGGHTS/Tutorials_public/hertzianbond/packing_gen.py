# Preparation run: create bonded packing and save restart before indentation

units           micro
boundary        p p fm
atom_style      granular
newton          off
communicate     single vel yes

neighbor        6 bin
neigh_modify    delay 0

region          reg block -75 75 -75 75 0 7.6492e1 units box
create_box      6 reg

shell mkdir -p post
shell mkdir -p restart

variable        nstiffness equal 13.5e1
variable        tstiffness equal 13.5e1
variable        maxsigma   equal 30.75e3
variable        maxtange   equal 1.5e3

variable        dampingnormalForce   equal 0.96
variable        dampingtangentForce  equal 0.96
variable        dampingnormalTorque  equal 0.96
variable        dampingtangentTorque equal 0.96

fix m1 all property/global youngsModulus peratomtype 0.45e6 0.45e6 0.45e6 0.45e6 0.45e6 2e11
fix m2 all property/global poissonsRatio peratomtype 0.30 0.30 0.30 0.30 0.30 0.30
fix m3 all property/global coefficientRestitution peratomtypepair 6 & 
     0.25 0.25 0.25 0.25 0.25 0.25 &
     0.25 0.25 0.25 0.25 0.25 0.25 &
     0.25 0.25 0.25 0.25 0.25 0.25 &
     0.25 0.25 0.25 0.25 0.25 0.25 &
     0.25 0.25 0.25 0.25 0.25 0.25 &
     0.25 0.25 0.25 0.25 0.25 0.25
fix m4 all property/global coefficientFriction peratomtypepair 6 &
     0.1 0.1 0.1 0.1 0.1 0.1 &
     0.1 0.1 0.1 0.1 0.1 0.1 &
     0.1 0.1 0.1 0.1 0.1 0.1 &
     0.1 0.1 0.1 0.1 0.1 0.1 &
     0.1 0.1 0.1 0.1 0.1 0.1 &
     0.1 0.1 0.1 0.1 0.1 0.1

fix m05 all property/global Bondmultiplier peratomtypepair 6 &
     0.24 0.24 0.24 0.24 0.24 0.24 &
     0.24 0.24 0.24 0.24 0.24 0.24 &
     0.24 0.24 0.24 0.24 0.24 0.24 &
     0.24 0.24 0.24 0.24 0.24 0.24 &
     0.24 0.24 0.24 0.24 0.24 0.24 &
     0.24 0.24 0.24 0.24 0.24 0.24
fix m06 all property/global normalBondStiffnessPerUnitArea peratomtypepair 6 &
     ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} &
     ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} &
     ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} &
     ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} &
     ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} &
     ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness}
fix m07 all property/global tangentialBondStiffnessPerUnitArea peratomtypepair 6 &
     ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} &
     ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} &
     ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} &
     ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} &
     ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} &
     ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness}

fix m08a all property/global maxSigmaBond peratomtypepair 6 &
     ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} &
     ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} &
     ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} &
     ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} &
     ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} &
     ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma}
fix m08b all property/global maxTauBond peratomtypepair 6 &
     ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} &
     ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} &
     ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} &
     ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} &
     ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} &
     ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange}
fix m13 all property/global tsCreateBond      scalar 1e12
fix m09 all property/global dampingNormalForceBond peratomtypepair 6 &
     ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} &
     ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} &
     ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} &
     ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} &
     ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} &
     ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce}
fix m10 all property/global dampingTangentialForceBond peratomtypepair 6 &
     ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} &
     ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} &
     ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} &
     ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} &
     ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} &
     ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce}
fix m11 all property/global dampingNormalTorqueBond peratomtypepair 6 &
     ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} &
     ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} &
     ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} &
     ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} &
     ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} &
     ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque}
fix m12 all property/global dampingTangentialTorqueBond peratomtypepair 6 &
     ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} &
     ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} &
     ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} &
     ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} &
     ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} &
     ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque}

pair_style gran model hertz2 tangential history cohesion bond2 stressBreak on
pair_coeff * *

timestep 1.0e-4

fix zwalls1 all wall/gran model hertz2 tangential history primitive type 6 zplane 0.0
fix zwalls2 all wall/gran model hertz2 tangential history primitive type 1 zplane 76.492

variable r1_final equal 2.015
variable r2_final equal 2.4
variable r3_final equal 2.76
variable r4_final equal 4.0
variable r5_final equal 6.5

variable r1_init equal ${r1_final}*0.5
variable r2_init equal ${r2_final}*0.5
variable r3_init equal ${r3_final}*0.5
variable r4_init equal ${r4_final}*0.5
variable r5_init equal ${r5_final}*0.5

fix pts1 all particletemplate/sphere 15485863 atom_type 1 density constant 2.2 radius constant ${r1_init}
fix pts2 all particletemplate/sphere 15485867 atom_type 2 density constant 2.2 radius constant ${r2_init}
fix pts3 all particletemplate/sphere 32452843 atom_type 3 density constant 2.2 radius constant ${r3_init}
fix pts4 all particletemplate/sphere 32452867 atom_type 4 density constant 2.2 radius constant ${r4_init}
fix pts5 all particletemplate/sphere 49979687 atom_type 5 density constant 2.2 radius constant ${r5_init}
fix dist1 all particledistribution/discrete/numberbased 49979693 5 pts1 0.29 pts2 0.16 pts3 0.33 pts4 0.21 pts5 0.01

group reg_group region reg
fix ins reg_group insert/pack seed 67867967 distributiontemplate dist1 insert_every once overlapcheck yes all_in yes vel constant 0 0 0 particles_in_region 8251 region reg

fix integr all nve/sphere

compute 1 all erotate/sphere
compute bc all bond/counter
compute cp all pair/gran/local delta
compute sumov all reduce sum c_cp[1]

variable zpoint equal 76.6
fix piston_m all mesh/surface/stress file nanoindentormicro.stl type 6 move 0 0 ${zpoint}
fix piston all wall/gran model hertz2 tangential history mesh n_meshes 1 meshes piston_m
fix piston_force all ave/time 1 1 100 f_piston_m[1] f_piston_m[2] f_piston_m[3] file post/piston_force_restart.txt
dump		dmp2 all mesh/vtk 2500 post/H-B_packing_mesh*.vtk id stress stresscomponents vel


run 1
dump		dmp all custom/vtk 2500 post/H-B_packing_*.vtk id type type x y z ix iy iz vx vy vz fx fy fz omegax omegay omegaz radius 
unfix ins

variable	growts equal 1000000

group ptctype1 type 1
group ptctype2 type 2
group ptctype3 type 3
group ptctype4 type 4
group ptctype5 type 5

variable growscalar equal 5.28e-6
variable growrate atom ${growscalar}

variable curr_r1 equal ${r1_init}+step*${growscalar}*0.5 #fix제어용 지름정보 
variable curr_r2 equal ${r2_init}+step*${growscalar}*0.5
variable curr_r3 equal ${r3_init}+step*${growscalar}*0.5 
variable curr_r4 equal ${r4_init}+step*${growscalar}*0.5 
variable curr_r5 equal ${r5_init}+step*${growscalar}*0.5 

compute dia1 ptctype1 property/atom diameter
compute dia2 ptctype2 property/atom diameter
compute dia3 ptctype3 property/atom diameter
compute dia4 ptctype4 property/atom diameter
compute dia5 ptctype5 property/atom diameter

compute dia1_avg ptctype1 reduce ave c_dia1
compute dia2_avg ptctype2 reduce ave c_dia2
compute dia3_avg ptctype3 reduce ave c_dia3
compute dia4_avg ptctype4 reduce ave c_dia4
compute dia5_avg ptctype5 reduce ave c_dia5

variable newdia1 atom c_dia1+v_growrate
variable newdia2 atom c_dia2+v_growrate
variable newdia3 atom c_dia3+v_growrate
variable newdia4 atom c_dia4+v_growrate
variable newdia5 atom c_dia5+v_growrate

fix ptc1_grow ptctype1 adapt 1 atom diameter v_newdia1
fix ptc2_grow ptctype2 adapt 1 atom diameter v_newdia2
fix ptc3_grow ptctype3 adapt 1 atom diameter v_newdia3
fix ptc4_grow ptctype4 adapt 1 atom diameter v_newdia4
fix ptc5_grow ptctype5 adapt 1 atom diameter v_newdia5

run 1
thermo_style custom step atoms ke vol c_dia1_avg c_dia2_avg c_dia3_avg c_dia4_avg c_dia5_avg c_bc[1] c_bc[2] c_bc[3] c_sumov
thermo 1000

variable r_1step equal (${r1_final}-${r1_init})/${growscalar}*2
variable r_2step equal (${r2_final}-${r2_init})/${growscalar}*2-${r_1step}
variable r_3step equal (${r3_final}-${r3_init})/${growscalar}*2-${r_1step}-${r_2step}
variable r_4step equal (${r4_final}-${r4_init})/${growscalar}*2-${r_1step}-${r_2step}-${r_3step}
variable r_5step equal (${r5_final}-${r5_init})/${growscalar}*2-${r_1step}-${r_2step}-${r_3step}-${r_4step}

run ${r_1step}
unfix ptc1_grow
run ${r_2step}
unfix ptc2_grow
run ${r_3step}
unfix ptc3_grow
run ${r_4step}
unfix ptc4_grow
run ${r_5step}
unfix ptc5_grow

variable relaxts equal 500000
run ${relaxts}

fix zero all freeze
velocity all set 0 0 0
fix noforce all setforce 0 0 0
unfix zwalls2
print		"remove wall"
run 10000
unfix zero
unfix noforce
run 100000
run 100000
# print		"bond create"
# variable bondtime equal ${r_1step}+2+${r_2step}+${r_3step}+${r_4step}+${r_5step}+${relaxts}+10000+100000*2+1
# fix m13 all property/global tsCreateBond scalar ${bondtime}
# run 100000

# Save restart for indentation stage

write_restart restart/packing_ready.restart