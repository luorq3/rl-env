# Reinforcement Learning Environment

Size:

- Map:  (896, 896)

  防守方陆地为一个半圆，圆心位于 (448, 0)，半径为224

  $(x-448)^2 + y^2 = 224^2$

- fort: (20, 20)

  炮台分布于防守半圆的边缘，由于炮台自身有半径`10`，定义炮台分布于

  $(x-448)^2 + y^2 = 210^2, r=210$

  的半圆

- ship: (40, 99)
- ship_missile: (5, 8)
- fort_missile: (5, 8)