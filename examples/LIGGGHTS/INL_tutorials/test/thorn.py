# --- General settings ---
atom_style      sphere
atom_modify     map array
boundary        f f f
newton          off
communicate     single vel yes
units           si
processors      * * *

# --- Define simulation box ---
region simbox block 0 0.0003 0 0.0003 0 0.0004 units box
create_box 1 simbox

# --- Create random particles ---
create_atoms 1 random 1000 12345 simbox
set type 1 diameter 1.5e-5

# --- Pair and material properties ---
pair_style gran model thornton_ning tangential history cohesion off rolling_friction off
pair_coeff * *

neighbor 2e-5 bin
neigh_modify delay 0

fix m1 all property/global youngsModulus peratomtype 1 1.42e11
fix m2 all property/global poissonsRatio peratomtype 1 0.3
fix m3 all property/global coefficientRestitution peratomtypepair 1 0.1
fix m4 all property/global coefficientFriction peratomtypepair 1 0.3
fix m5 all property/global density peratomtype 1 2300

# --- Gravity and timestep ---
variable dt equal 1e-7
timestep ${dt}
fix grav all gravity 9.81 vector 0.0 0.0 -1.0

# --- Wall definition ---
fix wall_bottom all wall/gran model thornton_ning tangential history primitive type 1 zplane 0.0
fix wall_top all wall/gran model thornton_ning tangential history primitive type 1 zplane 0.0004

# --- Piston compression ---
fix piston all wall/gran model thornton_ning tangential history primitive type 1 zplane 0.0004 move linear 0.0 0.0 -0.001

# --- Integration and output ---
fix integr all nve/sphere
dump dmp all custom/vtk 100 post/compress_*.vtk id type x y z vx vy vz fx fy fz omegax omegay omegaz radius
thermo 500

# --- Run simulation ---
run 50000