# Units and basic settings 
units           micro
# dimension       3
boundary        p p fm                    # x,y periodic; z has a fixed wall (floor)
atom_style      granular                 # granular style (stores radius, etc.)
newton          off                      # use Newton's 3rd law off (common for granular with history)
# gravity         0.00 0.00 0.00             # no gravity during structure generation (no external load)
communicate	single vel yes

# Neighbor settings (small skin since high stiffness requires small timestep:contentReference[oaicite:0]{index=0})
neighbor        6 bin
neigh_modify	delay 0
 
# Define simulation region (150 µm × 150 µm cross-section, ~80 µm tall):contentReference[oaicite:1]{index=1}:contentReference[oaicite:2]{index=2}
region          reg block -75 75 -75 75 0 7.6492e1 units box
create_box      6 reg        # 5 particle types to approximate size distribution:contentReference[oaicite:3]{index=3}


variable nstiffness equal 13.5e1
variable tstiffness equal 13.5e1
variable maxsigma equal 30.75e3
variable maxtange equal 1.5e3

variable dampingnormalForce equal 0.95
variable dampingtangentForce equal	 0.96
variable dampingnormalTorque equal 0.96
variable dampingtangentTorque equal 0.96
#Material properties required for new pair styles

fix 		m1 all property/global youngsModulus peratomtype 0.45e6 0.45e6 0.45e6 0.45e6 0.45e6 2e11
fix 		m2 all property/global poissonsRatio peratomtype 0.30 0.30 0.30 0.30 0.30 0.30
fix 		m3 all property/global coefficientRestitution peratomtypepair 6 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25 0.25
fix 		m4 all property/global coefficientFriction peratomtypepair 6 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1
# 결합 강성·반지름
fix m05 all property/global Bondmultiplier peratomtypepair 6 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 0.24 #<f_b>
fix m06 all property/global normalBondStiffnessPerUnitArea    peratomtypepair 6 ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness} ${nstiffness}
fix m07 all property/global tangentialBondStiffnessPerUnitArea peratomtypepair 6 ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} ${tstiffness} # neigh_modify delay 0 contact_distance_factor 2
# # 파괴 기준(하나 선택)
# fix m08 all property/global maxDistanceBond peratomtypepair 5 1e12 1e12 1e12 1e12 1e12 1e12 1e12 1e12 1e12 1e12 1e12 1e12 1e12 1e12 1e12 1e12 1e12 1e12 1e12 1e12 1e12 1e12 1e12 1e12 1e12 #<r_break>      # stressBreak off
# fix zwalls1 all wall/gran model hertz2 tangential history cohesion bond2 primitive type 1 zplane  0.00
# unfix m08
# 또는s
fix m08a all property/global maxSigmaBond peratomtypepair 6 ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma} ${maxsigma}     #<σ_max>          # stressBreak on
fix m08b all property/global maxTauBond   peratomtypepair  6 ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange} ${maxtange}    #<τ_max>

# 결합 생성 시점/거리
fix m13 all property/global tsCreateBond      scalar 1e12
# fix m14 all property/global createDistanceBond peratomtypepair 6 1.0075 1.0954 1.165 1.34 1.538 1.0075 1.0954 1.2 1.284 1.5 1.753 1.2 1.165 1.284 1.38 1.633 1.937 1.38 1.34 1.5 1.1633 2 2.476 2 1.538 1.753 1.937 2.476 3.25 3.25 1.0075 1.2 1.38 2 3.25 10   #<r_create>
# fix m14 all property/global createDistanceBond peratomtypepair 6 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 선택 옵션: 댐핑 또는 시간소산
fix m09 all property/global dampingNormalForceBond       peratomtypepair 6 ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} ${dampingnormalForce} #<α_fn>
fix m10 all property/global dampingTangentialForceBond   peratomtypepair 6 ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce} ${dampingtangentForce}  #<α_ft>
fix m11 all property/global dampingNormalTorqueBond      peratomtypepair 6 ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque} ${dampingnormalTorque}  #<α_tn>
fix m12 all property/global dampingTangentialTorqueBond  peratomtypepair 6 ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} ${dampingtangentTorque} #<α_tt>
# (또는 dissipation*Bond 계열)


#New pair style
pair_style gran model hertz2 tangential history cohesion bond2 stressBreak on #Hertzian without cohesion
pair_coeff	* *

#마이크로단위라 수정 (1e-10 [s])
timestep	1.0e-4 

# fix xwalls1 all wall/gran model hertz tangential history primitive type 1 xplane -92
# fix xwalls2 all wall/gran model hertz tangential history primitive type 1 xplane 92
# fix ywalls1 all wall/gran model hertz tangential history primitive type 1 yplane -92
# fix ywalls2 all wall/gran model hertz tangential history primitive type 1 yplane 92
fix zwalls1 all wall/gran model hertz2 tangential history primitive type 6 zplane  0.0000
fix zwalls2 all wall/gran model hertz2 tangential history primitive type 1 zplane  76.492
# fix zwalls2 all wall/reflect zhi 76.5   # z=76.5 평면에서 위쪽으로 나가는 입자 반사

# Particle size distribution (C1 structure: x10=4.03µm, x50=5.99µm, x90=8.94µm:contentReference[oaicite:4]{index=4})
# Use 5 discrete radii corresponding to range ~4–8.24 µm 

variable        r1_final equal 2.015    # 4.03 µm diameter / 2
variable        r2_final equal 2.4   # ~4.8 µm diameter / 2
variable        r3_final equal 2.76   # 5.52 µm diameter / 2
variable        r4_final equal 4   # ~8.0 µm diameter / 2
variable        r5_final equal 6.5     # 1.30 2m diameter / 2
#Initial radii are half of real size:contentReference[oaicite:5]{index=5}:분포랑공극률계산해서나온거 

# variable        r1_final equal 2.25    # 4.03 µm diameter / 2 
# variable        r2_final equal 3   # ~5.0 µm diameter / 2
# variable        r3_final equal 4    # 6.0 µm diameter / 2
# variable        r4_final equal 5   # ~7.4 µm diameter / 2
# variable        r5_final equal 6.5     # 8.24 µm diameter / 2

variable        r1_init  equal ${r1_final}*0.5
variable        r2_init  equal ${r2_final}*0.5
variable        r3_init  equal ${r3_final}*0.5
variable        r4_init  equal ${r4_final}*0.5
variable        r5_init  equal ${r5_final}*0.5

#distributions for insertion
fix pts1 all particletemplate/sphere 15485863 atom_type 1 density constant 2.2 radius constant ${r1_init}
fix pts2 all particletemplate/sphere 15485867 atom_type 2 density constant 2.2 radius constant ${r2_init}
fix pts3 all particletemplate/sphere 32452843 atom_type 3 density constant 2.2 radius constant ${r3_init}
fix pts4 all particletemplate/sphere 32452867 atom_type 4 density constant 2.2 radius constant ${r4_init}
fix pts5 all particletemplate/sphere 49979687 atom_type 5 density constant 2.2 radius constant ${r5_init}
fix dist1 all particledistribution/discrete/numberbased 49979693 5 pts1 0.29 pts2 0.16 pts3 0.33 pts4 0.21 pts5 0.01 #공극률 대략0.44
# fix dist1 all particledistribution/discrete/numberbased 49979693 5 pts1 0.3 pts2 0.3 pts3 0.32 pts4 0.04 pts5 0.04
# fix dist1 all particledistribution/discrete/numberbased 49979693 5 pts1 0.1 pts2 0.17 pts3 0.58 pts4 0.14 pts5 0.01


#parameters for gradually growing particle diameter
# variable	alphastart equal 0.5
# variable	alphatarget equal 1
# variable	growts equal 50000
# variable	growevery equal 40
# variable	relaxts equal 100000

#region and insertion
group		reg_group region reg

#particle insertion

fix ins reg_group insert/pack seed 67867967 distributiontemplate dist1 insert_every once overlapcheck yes all_in yes vel constant 0. 0. 0. particles_in_region 8251 region reg

#fix		ins nve_group insert/pack seed 32452867 distributiontemplate pdd1 &
			# maxattempt 200 insert_every once overlapcheck yes all_in yes vel constant 0. 0. 0. &
			# region reg volumefraction_region ${alphastart}

#apply nve integration to all particles that are inserted as single particles
fix		integr all nve/sphere



#output settings, include total thermal energy
compute		1 all erotate/sphere
compute bc all bond/counter
compute cp all pair/gran/local delta
compute sumov all reduce sum c_cp[1]
# thermo_style	custom step atoms ke c_1 vol c_bc[1]
# thermo		1000
# thermo_modify	lost ignore norm no

#insert the first particles

#인덴터 설정정
variable zpoint equal 76.6
fix piston_m    all mesh/surface/stress file nanoindentormicro.stl type 6 move 0. 0. ${zpoint}
fix piston      all wall/gran model hertz2 tangential history mesh   n_meshes 1   meshes piston_m
fix piston_force all ave/time 1 1 100 f_piston_m[1] f_piston_m[2] f_piston_m[3] file post/piston_force_default.txt
dump		dmp2 all mesh/vtk 2500 post/H-B_packing_mesh*.vtk id stress stresscomponents vel

variable startZ    equal ${zpoint}
variable endZ      equal 76.5-7.65
variable dz        equal ${startZ}-${endZ} 
variable cvel      equal 0.15e-6
variable rvel      equal -1*${cvel}
variable ts_move   equal (${dz}/${cvel})/(1e-4)
variable ts_move1   equal (${ts_move}/1000)
#---------------------
print		" ---------------------"
print		" N step:${ts_move1}"
print		" ---------------------"




run		1
# run ${ts_move1}
dump		dmp all custom/vtk 2500 post/H-B_packing_*.vtk id type type x y z ix iy iz vx vy vz fx fy fz omegax omegay omegaz radius 

unfix		ins

#calculate grow rate

variable	growts equal 1000000

# print		"The radius grow rate is ${Rgrowrate}"

#do the diameter grow
# compute 	rad all property/atom radius
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

compute dia1 ptctype1 property/atom diameter   # 현재 지름 값 원자형 데이터로 수집
compute dia2 ptctype2 property/atom diameter 
compute dia3 ptctype3 property/atom diameter 
compute dia4 ptctype4 property/atom diameter 
compute dia5 ptctype5 property/atom diameter 

compute dia1_avg ptctype1 reduce ave c_dia1   # 현재 지름 값 스칼라로수집(thermo표시용 )
compute dia2_avg ptctype2 reduce ave c_dia2
compute dia3_avg ptctype3 reduce ave c_dia3
compute dia4_avg ptctype4 reduce ave c_dia4
compute dia5_avg ptctype5 reduce ave c_dia5
 
variable newdia1 atom c_dia1+v_growrate   # 지름 값 업데이트 
variable newdia2 atom c_dia2+v_growrate
variable newdia3 atom c_dia3+v_growrate
variable newdia4 atom c_dia4+v_growrate
variable newdia5 atom c_dia5+v_growrate

fix ptc1_grow ptctype1 adapt 1 atom diameter v_newdia1 # 업데이트한 지름값 입자에 적용 
fix ptc2_grow ptctype2 adapt 1 atom diameter v_newdia2
fix ptc3_grow ptctype3 adapt 1 atom diameter v_newdia3
fix ptc4_grow ptctype4 adapt 1 atom diameter v_newdia4
fix ptc5_grow ptctype5 adapt 1 atom diameter v_newdia5

# compute cpair all pair/local dist
# fix chk all check/timestep/gran 100 0.1 error

run 1

thermo_style custom step atoms ke vol c_dia1_avg c_dia2_avg c_dia3_avg c_dia4_avg c_dia5_avg c_bc[1] c_bc[2] c_bc[3] c_sumov #c_cpair
thermo		1000
# thermo_modify	lost ignore norm no


# thermo_style custom step atoms ke c_1 vol c_bc[1] c_rmax1 c_rmax2 c_rmax3 c_rmax4 c_rmax5
# run 0

# variable check1 equal c_ rmax1 < ${r1_final}
# variable check2 equal c_rmax2 < ${r2_final}
# variable check3 equal c_rmax3 < ${r3_final}
# variable check4 equal c_rmax4 < ${r4_final}
# variable check5 equal c_rmax5 < ${r5_final}
# if '${curr_r1}>=${r1_final}' then 'unfix ptc1_grow'
# run 1   # 변수 정의 후 다시 갱신
# if "${curr_r1} >= ${r1_final}" then "unfix ptc1_grow"

variable r_1step equal (${r1_final}-${r1_init})/${growscalar}*2
variable r_2step equal (${r2_final}-${r2_init})/${growscalar}*2-${r_1step}
variable r_3step equal (${r3_final}-${r3_init})/${growscalar}*2-${r_1step}-${r_2step}
variable r_4step equal (${r4_final}-${r4_init})/${growscalar}*2-${r_1step}-${r_2step}-${r_3step}
variable r_5step equal (${r5_final}-${r5_init})/${growscalar}*2-${r_1step}-${r_2step}-${r_3step}-${r_4step}

# fix stop all halt 1 "ke < 1.0e-2"
# variable totalstep equal
# unfix stop



run ${r_1step}
unfix ptc1_grow

# unfix ptc2_grow
# unfix ptc3_grow
# unfix ptc4_grow
# unfix ptc5_grow
# unfix m13
# unfix integer
# velocity all set 0.00 0.00 0.00
# set     group all omega 0.00 0.00 0.00 
# fix zero all freeze    
# fix noforce all setforce 0.00 0.00 0.00
# run 1
# variable bondtime equal ${r_1step}+2+1
# fix m13 all property/global tsCreateBond scalar ${bondtime}
# thermo 1
# # unfix noforce
# # unfix zero 
# run 100
# unfix ptc2_grow #임시용용
run ${r_2step}
unfix ptc2_grow
 
run ${r_3step}
unfix ptc3_grow

run ${r_4step}
unfix ptc4_grow

run ${r_5step}
unfix ptc5_grow

variable relaxts equal 500000

# # fix stop3
run ${relaxts}
fix zero all freeze
velocity all set 0.00 0.00 0.00
fix noforce all setforce 0.00 0.00 0.00

unfix zwalls2 #뚝빼기 제거거

print		"remove wall"
run 10000

unfix zero
unfix noforce
# fix damping all viscous 0.6
run 100000
# unfix damping


#본드생성성
variable bondtime equal ${r_1step}+2+${r_2step}+${r_3step}+${r_4step}+${r_5step}+${relaxts}+10000+100000*2+1
fix m13 all property/global tsCreateBond scalar ${bondtime}
# fix m14 all property/global createDistanceBond peratomtypepair 6 1.0075 1.0954 1.165 1.34 1.538 1.0075 1.0954 1.2 1.284 1.5 1.753 1.2 1.165 1.284 1.38 1.633 1.937 1.38 1.34 1.5 1.1633 2 2.476 2 1.538 1.753 1.937 2.476 3.25 3.25 1.0075 1.2 1.38 2 3.25 10   #<r_create>
run 100000


# variable i loop 1000
# label loop
# run 1000000
# next i
# print "${i}"
# jump SELF loop


fix piston_move all move/mesh mesh piston_m linear 0. 0. -${cvel}
print		"start loading"
variable i loop 1000
label loop
run         ${ts_move1}
next i
print "loop ${i}"
jump SELF loop


unfix piston_move
fix piston_move all move/mesh mesh piston_m linear 0. 0. 0.0
run         1

print		"start unloading" 
unfix piston_move
fix piston_move all move/mesh mesh piston_m linear 0. 0. ${cvel}
variable j loop 1000
label loop
run         ${ts_move}
next i
print "loop ${i}"
jump SELF loop