# Units and basic settings 
units           micro
# dimension       3
boundary        p p fm                    # x,y periodic; z has a fixed wall (floor)
atom_style      granular                 # granular style (stores radius, etc.)
newton          off                      # use Newton's 3rd law off (common for granular with history)
# gravity         0.0 0.0 0.0             # no gravity during structure generation (no external load)
communicate	single vel yes

# Neighbor settings (small skin since high stiffness requires small timestep:contentReference[oaicite:0]{index=0})
neighbor        6 bin
neigh_modify	delay 0
 
# Define simulation region (150 µm × 150 µm cross-section, ~80 µm tall):contentReference[oaicite:1]{index=1}:contentReference[oaicite:2]{index=2}
region          reg block 0 1.5e2 0 1.5e2 0 8e1 units box
create_box      1 reg        # 5 particle types to approximate size distribution:contentReference[oaicite:3]{index=3}


#Material properties required for new pair styles

fix 		m1 all property/global youngsModulus peratomtype 0.45e6
fix 		m2 all property/global poissonsRatio peratomtype 0.3
fix 		m3 all property/global coefficientRestitution peratomtypepair 1 0.25
fix 		m4 all property/global coefficientFriction peratomtypepair 1 0.1
# 결합 강성·반지름
fix m05 all property/global Bondmultiplier peratomtypepair 1 0.24   #<f_b>
fix m06 all property/global normalBondStiffnessPerUnitArea    peratomtypepair 1 13.5e1 #<Sn>
fix m07 all property/global tangentialBondStiffnessPerUnitArea peratomtypepair 1 13.5e1 #<St>

# 파괴 기준(하나 선택)
# fix m08 all property/global maxDistanceBond peratomtypepair 1 <r_break>      # stressBreak off
# 또는s
fix m08a all property/global maxSigmaBond peratomtypepair 1 28e3     #<σ_max>          # stressBreak on
fix m08b all property/global maxTauBond   peratomtypepair  1 0.8e3    #<τ_max>

# 결합 생성 시점/거리
fix m13 all property/global tsCreateBond      scalar 1e12
# fix m14 all property/global createDistanceBond peratomtypepair 1 8  #<r_create>

# 선택 옵션: 댐핑 또는 시간소산
fix m09 all property/global dampingNormalForceBond       peratomtypepair 1 0.95  #<α_fn>
fix m10 all property/global dampingTangentialForceBond   peratomtypepair 1 0.95  #<α_ft>
fix m11 all property/global dampingNormalTorqueBond      peratomtypepair 1 0.95  #<α_tn>
fix m12 all property/global dampingTangentialTorqueBond  peratomtypepair 1 0.95  #<α_tt>
# (또는 dissipation*Bond 계열)


#New pair style
pair_style gran model hertz tangential history cohesion bond2 stressBreak on #Hertzian without cohesion
pair_coeff	* *

#마이크로단위라 수정 (1e-10 [s])
timestep	1.0e-4 

# fix xwalls1 all wall/gran model hertz tangential history primitive type 1 xplane 0
# fix xwalls2 all wall/gran model hertz tangential history primitive type 1 xplane 1.5e2
# fix ywalls1 all wall/gran model hertz tangential history primitive type 1 yplane 0
# fix ywalls2 all wall/gran model hertz tangential history primitive type 1 yplane 1.5e2
fix zwalls1 all wall/gran model hertz tangential history primitive type 1 zplane  0.00
fix zwalls2 all wall/gran model hertz tangential history primitive type 1 zplane  80

# Particle size distribution (C1 structure: x10=4.03µm, x50=5.99µm, x90=8.94µm:contentReference[oaicite:4]{index=4})
# Use 5 discrete radii corresponding to range ~4–8.94 µm 
variable        r1_final equal 2.015    # 4.03 µm diameter / 2
variable        r2_final equal 2.50   # ~5.0 µm diameter / 2
variable        r3_final equal 3.00    # 6.0 µm diameter / 2
variable        r4_final equal 4.2   # ~7.4 µm diameter / 2
variable        r5_final equal 6.5     # 8.94 µm diameter / 2
# Initial radii are half of real size:contentReference[oaicite:5]{index=5}:
variable        r1_init  equal ${r1_final}*0.5
variable        r2_init  equal ${r2_final}*0.5
variable        r3_init  equal ${r3_final}*0.5
variable        r4_init  equal ${r4_final}*0.5
variable        r5_init  equal ${r5_final}*0.5

#distributions for insertion
fix pts1 all particletemplate/sphere 15485863 atom_type 1 density constant 2.2 radius constant ${r1_init}
fix pts2 all particletemplate/sphere 15485867 atom_type 1 density constant 2.2 radius constant ${r2_init}
fix pts3 all particletemplate/sphere 32452843 atom_type 1 density constant 2.2 radius constant ${r3_init}
fix pts4 all particletemplate/sphere 32452867 atom_type 1 density constant 2.2 radius constant ${r4_init}
fix pts5 all particletemplate/sphere 49979687 atom_type 1 density constant 2.2 radius constant ${r5_init}
fix dist1 all particledistribution/discrete/numberbased 49979693 5 pts1 0.35 pts2 0.25 pts3 0.20 pts4 0.15 pts5 0.05



#parameters for gradually growing particle diameter
variable	alphastart equal 0.5
variable	alphatarget equal 1
variable	growts equal 50000
variable	growevery equal 40
variable	relaxts equal 100000

#region and insertion
group		nve_group region reg

#particle insertion

fix ins nve_group insert/pack seed 67867967 distributiontemplate dist1 insert_every once overlapcheck yes all_in yes vel constant 0. 0. 0. particles_in_region 8251 region reg

#fix		ins nve_group insert/pack seed 32452867 distributiontemplate pdd1 &
			# maxattempt 200 insert_every once overlapcheck yes all_in yes vel constant 0. 0. 0. &
			# region reg volumefraction_region ${alphastart}

#apply nve integration to all particles that are inserted as single particles
fix		integr nve_group nve/sphere

#output settings, include total thermal energy
compute		1 all erotate/sphere
compute bc all bond/counter
thermo_style	custom step atoms ke c_1 vol c_bc[1]
thermo		1000
thermo_modify	lost ignore norm no

#insert the first particles
run		1
dump		dmp all custom/vtk 100 post/H-B_packing_*.vtk id type type x y z ix iy iz vx vy vz fx fy fz omegax omegay omegaz radius 
unfix		ins

#calculate grow rate

variable growts equal 1e5

# print		"The radius grow rate is ${Rgrowrate}"

#do the diameter grow 
compute 	rad all property/atom radius

variable v1 atom "c_rad <= 2.015"
variable v2 atom "c_rad > 2.015 && c_rad <= 2.5"
variable v3 atom "c_rad > 2.5 && c_rad <= 3"
variable v4 atom "c_rad > 3 && c_rad <= 4.2"
variable v5 atom "c_rad > 4.2"


# group ptc1 variable v1
# group ptc2 variable v2
# group ptc3 variable v3
# group ptc4 variable v4
# group ptc5 variable v5


variable growdia atom 2*(c_rad+5.28e-6)
variable scalargrow equal 2*(c_rad+5.28e-12)

# variable currentr1 equal ${r1_init}+step*(5.28e-6)*0.5
# variable currentr2 equal ${r2_init}+step*growdia*0.5
# variable currentr3 equal ${r3_init}+step*growdia*0.5
# variable currentr4 equal ${r4_init}+step*growdia*0.5
# variable currentr5 equal ${r5_init}+step*growdia*0.5


# fix ptc1_grow ptc1 adapt 1 atom diameter v_growdia
# fix ptc2_grow ptc2 adapt 1 atom diameter v_growdia
# fix ptc3_grow ptc3 adapt 1 atom diameter v_growdia
# fix ptc4_grow ptc4 adapt 1 atom diameter v_growdia
# fix ptc5_grow ptc5 adapt 1 atom diameter v_growrad


#run


# compute rmax1 ptc1 reduce max c_rad update_on_run_end yes
# compute rmax2 ptc2 reduce max c_rad update_on_run_end yes
# compute rmax3 ptc3 reduce max c_rad update_on_run_end yes
# compute rmax4 ptc4 reduce max c_rad update_on_run_end yes
# compute rmax5 ptc5 reduce max c_rad update_on_run_end yes

# thermo_style custom step atoms ke c_1 vol c_bc[1] c_rmax1 c_rmax2 c_rmax3 c_rmax4 c_rmax5
# run 0

# compute_modify rmax1 dynamic yes
# compute_modify rmax2 dynamic yes
# compute_modify rmax3 dynamic yes
# compute_modify rmax4 dynamic yes
# compute_modify rmax5 dynamic yes

# thermo_style custom step atoms ke c_1 vol c_bc[1] c_rmax1 c_rmax2 c_rmax3 c_rmax4 c_rmax5
# run 0

# variable check1 equal c_rmax1 < ${r1_final}
# variable check2 equal c_rmax2 < ${r2_final}
# variable check3 equal c_rmax3 < ${r3_final}
# variable check4 equal c_rmax4 < ${r4_final}
# variable check5 equal c_rmax5 < ${r5_final}

# run 0;   # 변수 정의 후 다시 갱신
# print 'current value is ${currentr1}'
run ${growts} #every 1 "if 'currentr1 >= ${r1_final}' then 'unfix ptc1_grow' &
# if 'currentr2 >= ${r2_final}' then 'unfix ptc2_grow'&
# if 'currentr3 >= ${r3_final}' then 'unfix ptc3_grow'&
# if 'currentr4 >= ${r4_final}' then 'unfix ptc4_grow'&
# if 'currentr5 >= ${r5_final}' then 'unfix ptc5_grow' "

#let the packing relax
# unfix	grow
run		${relaxts}




