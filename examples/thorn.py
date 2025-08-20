# ---------- 초기 설정 ---------- 
units           si                     # SI 단위계 사용
atom_style      granular               # 입자(구) 전용 원자 스타일 (반지름, 각속도 등 속성 포함)
dimension       3                      # 3차원 시뮬레이션
boundary        f f f                  # 경계 조건 (여기서는 x,y,z 모두 고정 경계 예시)

# ---------- 영역 및 입자 생성 ---------- 
region simbox block 0 0.1  0 0.1  0 0.1  units m   # 0.1 m 정육면체 영역 정의 (예시)
create_box 1 simbox                           # 1가지 입자 타입으로 박스 생성
create_atoms 1 random 10000 12345 NULL        # 임의로 10,000개의 입자를 생성 (랜덤 위치, 시드 12345)
set group all diameter 0.005                  # 모든 입자 지름 5 mm로 설정 (예시)
set group all density 2500                    # 입자 밀도 2500 kg/m^3 (예시)

# ---------- 물성치 및 접촉 모델 설정 ---------- 
fix prop1 all property/global youngsModulus peratomtype 1 7.0e10      # 영률 7e10 Pa
fix prop2 all property/global poissonRatio peratomtype 1 0.30        # 포아송비 0.30 
fix prop3 all property/global coefficientFriction peratomtypepair 1 1 0.5   # 마찰계수 0.5 
fix prop4 all property/global coefficientRollingFriction peratomtypepair 1 1 0.0 # 구름마찰 0 (없음)
fix prop5 all property/global coefficientRestitution peratomtypepair 1 1 0.9   # 탄성복원계수 0.9 
fix prop6 all property/global yieldRatio peratomtypepair 1 1 0.10    # Yield ratio 0.10 (탄성-소성 전이 비율)
fix prop7 all property/global cohesionEnergyDensity peratomtypepair 1 1 0.50   # 표면에너지 밀도 0.50 J/m^2 (접착력 파라미터)

pair_style      gran model thornton/ning tangential history           # Thornton–Ning 탄성-소성 + 접착 모델, 탄젠셜 히스토리 마찰 사용
pair_coeff      * *                                                   # 정의한 모델을 모든 입자-입자 쌍에 적용

# ---------- 경계(벽) 조건 설정 (압축을 위한 상하 플레이트) ----------
fix bottomWall all wall/gran model thornton/ning tangential history plane 0 0 0   0 0 1   # 바닥 평면벽 (z=0, 위쪽 향한 법선)
fix topWall    all wall/gran model thornton/ning tangential history plane 0 0 0.1 0 0 -1  # 상단 평면벽 (z=0.1m, 아래로 향한 법선)
fix moveTop    all move/mesh linear 0.0 0.0 -0.001 units m/s          # 상단벽을 -z 방향으로 0.001 m/s 속도로 이동 (압축)
# (참고: fix move/mesh는 mesh로 정의된 벽체 이동용. 평면벽에는 fix wall/gran 자체에 움직임 옵션이 없으므로, 
# 여기서는 상단벽을 움직이는 예를 위한 mesh 이동 방법을 가정)

# ---------- 시뮬레이션 제어 및 통계 출력 ----------
compute 1 all temp/sphere
thermo_style custom step time atoms temp press
thermo          1000                   # 1000 스텝마다 thermo 출력
timestep        1.0e-5                 # 타임스텝 1e-5 초 (안정성 고려 작은 값)
fix integrator all nve/sphere          # 입자 운동방정식 적분 (엔케이지 유지)
run             100000                 # 100000 스텝 실행 (압축 진행)