# Units and basic settings 
units           si
# dimension       3
boundary        p p fm                    # x,y periodic; z has a fixed wall (floor)
atom_style      granular                 # granular style (stores radius, etc.)
newton          off                      
# gravity         0.00 0.00 0.00             # no gravity during structure generation 
communicate	single vel yes

# Neighbor settings 
neighbor        6 bin
neigh_modify	delay 0
 
# Define simulation region (150 µm × 150 µm cross-section, ~80 µm tall)
region          reg block -75e-6 75e-6 -75e-6 75e-6 0 7.6492e-5 units box
create_box      5 reg        # 5 particle types


variable nstiffness equal 13.5e10
variable tstiffness equal 13.5e10
variable maxsigma equal 25.75e12
variable maxtange equal 1.2e12

#Material properties required for new pair styles

fix 		m1 all property/global youngsModulus peratomtype 0.45e9 0.45e9 0.45e9 0.45e9 0.45e9
fix 		m2 all property/global poissonsRatio peratomtype 0.30 0.30 0.30 0.30 0.30
fix 		m3 all property/global coefficientRestitution peratomtypepair 5 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25
fix 		m4 all property/global coefficientFriction peratomtypepair 5 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
# 
fix m05 all property/global Bondmultiplier peratomtypepair 5 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24  #<f_b>
fix m06 all property/global normalBondStiffnessPerUnitArea    peratomtypepair 5 ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness}
fix m07 all property/global tangentialBondStiffnessPerUnitArea peratomtypepair 5 ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} # neigh_modify delay 0 contact_distance_factor 2

# # 


# 
fix m08a all property/global maxSigmaBond peratomtypepair 5 ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma}     #<σ_max>          # stressBreak on
fix m08b all property/global maxTauBond   peratomtypepair  5 ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange}    #<τ_max>

# not to make error 
fix m13 all property/global tsCreateBond      scalar 1e12

 
# damping option
fix m09 all property/global dampingNormalForceBond       peratomtypepair 5 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95  #<α_fn>
fix m10 all property/global dampingTangentialForceBond   peratomtypepair 5 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95  #<α_ft>
fix m11 all property/global dampingNormalTorqueBond      peratomtypepair 5 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95  #<α_tn>
fix m12 all property/global dampingTangentialTorqueBond  peratomtypepair 5 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95 0.95  #<α_tt>



#New pair style(hertz2 is custom model  modifiying elastic stiffness of hertz model )
pair_style gran model hertz2 tangential history cohesion bond2 stressBreak on 
pair_coeff	* *

#convert to micro unit
timestep	1.0e-10 

#bottom wall and top wall to prevent particle loss
fix zwalls1 all wall/gran model hertz2 tangential history primitive type 1 zplane  0.0000e-6
fix zwalls2 all wall/gran model hertz2 tangential history primitive type 1 zplane  76.492e-6


# Particle size distribution (C1 structure: x10=4.03µm, x50=5.99µm, x90=8.94µm:contentReference[oaicite:4]{index=4})

variable        r1_final equal 2.015e-6    # 4.03 µm diameter / 2
variable        r2_final equal 2.4e-6   # ~4.8 µm diameter / 2
variable        r3_final equal 2.76e-6   # 5.52 µm diameter / 2
variable        r4_final equal 4e-6   # ~8.0 µm diameter / 2
variable        r5_final equal 6.5e-6     # 13 µm diameter / 2



variable        r1_init  equal ${r1_final}*0.5
variable        r2_init  equal ${r2_final}*0.5
variable        r3_init  equal ${r3_final}*0.5
variable        r4_init  equal ${r4_final}*0.5
variable        r5_init  equal ${r5_final}*0.5

#distributions for insertion
fix pts1 all particletemplate/sphere 15485863 atom_type 1 density constant 2.2e3 radius constant ${r1_init}
fix pts2 all particletemplate/sphere 15485867 atom_type 2 density constant 2.2e3 radius constant ${r2_init}
fix pts3 all particletemplate/sphere 32452843 atom_type 3 density constant 2.2e3 radius constant ${r3_init}
fix pts4 all particletemplate/sphere 32452867 atom_type 4 density constant 2.2e3 radius constant ${r4_init}
fix pts5 all particletemplate/sphere 49979687 atom_type 5 density constant 2.2e3 radius constant ${r5_init}
fix dist1 all particledistribution/discrete/numberbased 49979693 5 pts1 0.29 pts2 0.16 pts3 0.33 pts4 0.21 pts5 0.01 #porosity=0.44




group		reg_group region reg

#particle insertion

fix ins reg_group insert/pack seed 67867967 distributiontemplate dist1 insert_every once overlapcheck yes all_in yes vel constant 0. 0. 0. particles_in_region 8251 region reg


fix		integr all nve/sphere



#output settings, include total thermal energy
compute		1 all erotate/sphere
compute bc all bond/counter
compute cp all pair/gran/local delta
compute sumov all reduce sum c_cp[1]


#indentor setting
# variable zpoint equal 76.6e-6
# fix piston_m    all mesh/surface/stress file nanoindentormicro.stl type 2 move 0. 0. ${zpoint}
# fix piston      all wall/gran model hertz2 tangential history mesh   n_meshes 1   meshes piston_m
# fix piston_force all ave/time 1 100 100 f_piston_m[1] f_piston_m[2] f_piston_m[3] file post/piston_force_default.txt
# dump		dmp2 all mesh/vtk 2500 post/H-B_packing_mesh*.vtk id stress stresscomponents vel

# variable startZ    equal ${zpoint}
# variable endZ      equal 76.5e-6-7.65e-6
# variable dz        equal ${startZ}-${endZ} 
# variable cvel      equal 0.15e-6
# variable rvel      equal -1*${cvel}
# variable ts_move   equal (${dz}/${cvel})/1e-4
#---------------------



run		1
dump		dmp all custom/vtk 2500 post/H-B_packing_*.vtk id type type x y z ix iy iz vx vy vz fx fy fz omegax omegay omegaz radius 

unfix		ins


variable	growts equal 1000000


#do the diameter grow

group ptctype1 type 1
group ptctype2 type 2
group ptctype3 type 3
group ptctype4 type 4
group ptctype5 type 5


variable growscalar equal 0.0528e-6

variable growrate atom ${growscalar}

variable curr_r1 equal ${r1_init}+step*${growscalar}*0.5 #fix control diameter information 
variable curr_r2 equal ${r2_init}+step*${growscalar}*0.5
variable curr_r3 equal ${r3_init}+step*${growscalar}*0.5 
variable curr_r4 equal ${r4_init}+step*${growscalar}*0.5 
variable curr_r5 equal ${r5_init}+step*${growscalar}*0.5 

compute dia1 ptctype1 property/atom diameter   # collecting present diameter value  by atom style
compute dia2 ptctype2 property/atom diameter 
compute dia3 ptctype3 property/atom diameter 
compute dia4 ptctype4 property/atom diameter 
compute dia5 ptctype5 property/atom diameter 

compute dia1_avg ptctype1 reduce ave c_dia1   # collecting diameter value by scalar type
compute dia2_avg ptctype2 reduce ave c_dia2
compute dia3_avg ptctype3 reduce ave c_dia3
compute dia4_avg ptctype4 reduce ave c_dia4
compute dia5_avg ptctype5 reduce ave c_dia5
 
variable newdia1 atom c_dia1+v_growrate   # update diameter value 
variable newdia2 atom c_dia2+v_growrate
variable newdia3 atom c_dia3+v_growrate
variable newdia4 atom c_dia4+v_growrate
variable newdia5 atom c_dia5+v_growrate

fix ptc1_grow ptctype1 adapt 1 atom diameter v_newdia1 # adapt updated diameter
fix ptc2_grow ptctype2 adapt 1 atom diameter v_newdia2
fix ptc3_grow ptctype3 adapt 1 atom diameter v_newdia3
fix ptc4_grow ptctype4 adapt 1 atom diameter v_newdia4
fix ptc5_grow ptctype5 adapt 1 atom diameter v_newdia5


run 1

thermo_style custom step atoms ke vol c_dia1_avg c_dia2_avg c_dia3_avg c_dia4_avg c_dia5_avg c_bc[1] c_bc[2] c_bc[3] c_sumov #c_cpair
thermo		1000


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


# run ${relaxts}
# fix zero all freeze
# velocity all set 0.00 0.00 0.00
# fix noforce all setforce 0.00 0.00 0.00

# # remove wall
# unfix zwalls2 

# print		"remove wall"
# run 10000

# unfix zero
# unfix noforce

# run 100000
# run 100000

# print		"creation of bond"
# variable bondtime equal ${r_1step}+2+${r_2step}+${r_3step}+${r_4step}+${r_5step}+${relaxts}+10000+100000*2+1
# fix m13 all property/global tsCreateBond scalar ${bondtime}

# run 100000

# #indentor velocity setting
# fix piston_move all move/mesh mesh piston_m linear 0. 0. -0.15
# print		"start loading"
# run         ${ts_move}
# print		"start unloading" 
# unfix piston_move
# fix piston_move all move/mesh mesh piston_m linear 0. 0. 0.15
# run         ${ts_move}

