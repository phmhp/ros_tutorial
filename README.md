# ROS1 스터디 & Loop 통신 과제

**기간:** 2024.01.18 ~ 2024.02.02  
**주제:** ROS1 기본 개념 학습 + rqt_graph 기반의 loop 통신 구조 구현

---

## 1. ROS1 기본 개념 정리

### Node
- **Node**는 ROS 시스템에서 실행되는 하나의 프로세스를 의미함.
- 여러 개의 노드들이 서로 통신하며 로봇의 전체 시스템을 구성함.

### Topic
- **Topic**은 노드 간 비동기적으로 메시지를 주고받는 통신 채널.
- 하나의 노드가 topic에 메시지를 publish하면, 다른 노드가 이를 subscribe하여 메시지를 수신함.

### Publisher & Subscriber
- **Publisher**: 특정 topic에 메시지를 발행(publish)하는 노드.
- **Subscriber**: 특정 topic을 구독(subscribe)하고 메시지를 수신하는 노드.

### Message
- ROS에서 주고받는 데이터 단위.
- 기본 메시지 타입: `std_msgs/String`, `std_msgs/Int32`, `geometry_msgs/Twist` 등.
- `.msg` 확장자 사용.

### Master
- 모든 노드의 등록과 통신을 중개하는 역할.
- 노드 간의 위치 정보(name, IP, port 등)를 관리함.

### rqt_graph
- 노드와 토픽 간의 관계를 시각적으로 보여주는 도구.
- 노드 간 통신 흐름을 직관적으로 파악 가능함.

---

## 2. Loop 통신 과제 설명

### 과제 목표
- ROS의 pub-sub 구조를 이해하고, 여러 노드 간 메시지를 주고받는 **loop 형태의 통신 구조** 구현.
- 아래와 같은 rqt_graph 형태를 구현하는 것이 목표:

![목표 구조](https://github.com/user-attachments/assets/6569578a-30e8-4cc1-855e-b72be6eead8f)

- 총 6개의 노드가 있으며, 메시지가 순환(loop) 구조로 전달됨.

### 주요 구성
| Node | 구독 토픽 | 발행 토픽 |
|------|------------|-------------|
| node0    | 없음       | `node0_msg`    |
| node1    | `node0_msg`,`node3_msg`   | `node1_msg`    |
| node2    | `node1_msg`   | `node2_msg`    |
| node3    | `node2_msg`   | `node3_msg`    |
| node4    | `node2_msg`   | 없음    |
| node5    | `node2_msg`   | 없음    |
- 루프 구조를 통해 메시지가 계속 순환하는 구조를 구현함.

---

## 3. 구현 결과

- 아래는 실제 구현 후 `rqt_graph`에서 확인된 결과:

![수행 결과](https://github.com/user-attachments/assets/872030e9-9c34-470b-986e-b67f9f0a3869)

- 순환형 구조가 정상적으로 구현된 것을 확인할 수 있음.

---

## 4. 학습 내용 요약

- `rospy`를 사용하여 Python으로 노드, Publisher, Subscriber 구현
- `roscore` 실행 후 각 노드를 별도 터미널에서 실행하여 통신 구성
- 메시지 처리 및 재전송 구조를 통해 Topic 간 순환 통신 학습
- 유용한 ROS 도구 학습:
  - `rqt_graph`: 노드 및 토픽 시각화
  - `rqt_console`: 메시지 로그 확인
  - `rosnode list/info`: 노드 상태 확인
  - `rostopic echo/info`: 토픽 상태 및 메시지 내용 확인

---

## 5. 실행 방법

```bash
# 터미널 1
roscore

# 터미널 2~4: 각각 노드 실행
rosrun ros_node0 node0.py
rosrun ros_node1 node1.py
rosrun ros_node2 node2.py

# 터미널 5: node3, node4, node5를 launch 파일로 실행
roslaunch ros_node3 launch345.launch

# 터미널 6: rqt_graph 실행
rqt_graph
