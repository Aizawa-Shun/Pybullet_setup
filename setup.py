### Pybullet 物理エンジン接続・環境設定 ###

import pybullet as p
import pybullet_data

## 物理エンジンに接続 ##
physicsClient = p.connect(p.GUI)

## pybullet_dataのパスを追加 ##
p.setAdditionalSearchPath(pybullet_data.getDataPath())

## 床を設定 ##
planeID = p.loadURDF("plane.urdf")

## 重力を設定 ##
p.setGravity(0, 0, -9.8)

## シミュレーションを実行 ##
while True:
    p.stepSimulation()
