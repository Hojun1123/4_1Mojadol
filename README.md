# KGU 4_1 캡스톤 프로젝트

---------------------------------------------------

# 제목 : 경기대학교 2023 캡스톤 프로젝트

## 개요
쓰레기 무단투기는 환경 오염의 주범이고, 마을 미관을 해치는 주요 요소이다.
특히 학교 주변 연무동은 쓰레기 무단 투기가 빈번하게 일어나지만 실제로 단속하기에는 시간과 비용이 부족하기 때문에 단속하지 못하는 실정이다.
AI 기술을 활용하여 무단 투기 행위를 탐지하고, 이를 관리하기 위한 시스템 개발을 목표로 하였다.


## 프로젝트 과정

### 프로그램 구성도
![image](https://github.com/Hojun1123/4_1Mojadol/assets/65999992/ffda7afc-46db-4b9d-a3bd-f27561c0fc35)


### 학습 데이터 수집 및 가공
1. AI허브, https://www.aihub.or.kr/
2. 직접 영상 수집 및 가공
.mp4 -> jpg -> 라벨링(https://github.com/ivangrov/ModifiedOpenLabelling)
![image](https://github.com/Hojun1123/4_1Mojadol/assets/65999992/cb60837e-8e7d-445e-b4aa-9464f21a7bdd)


### 데이터
배경 이미지 비율 5 ~ 10 %
YOLOv8 학습 시, 옵션으로 제공하는 Mosaicm, RandomHSV, RandomFlip 등 사용
Hard negative sample 포함, 탐지 해야하는 행위와 유사하여 인식이 어려운 예시(지갑을 줍는 행위/신발끈을 묶는 행위 등)


### 모델 파인 튜닝 & 결과 (YOLOv8)
- Google Colab 에서 학습 : https://colab.google/
- YOLOv8 모델 활용 : YOLOv8 : https://github.com/ultralytics

- Env.
Python : 3.10.11, Model : Ultralytics YOLO 8.0.112
Pytorch : 2.0.1, CUDA 11.8

- YOLOv8 Medium Model Summary
![image](https://github.com/Hojun1123/4_1Mojadol/assets/65999992/0bb6d29d-9c1c-4c40-b08c-e62ae769a2d3)
![image](https://github.com/Hojun1123/4_1Mojadol/assets/65999992/f1a04509-3cdf-45cf-b5ec-d30ef965f315)                            

- Confusion Matrix                                         
![image](https://github.com/Hojun1123/4_1Mojadol/assets/65999992/c09127ff-f8b7-4322-9d59-3462b05c9587)

- Detection Image
![image](https://github.com/Hojun1123/4_1Mojadol/assets/65999992/976b29fe-f0c3-463e-a707-f783b83676c9)


### OpenCV
투기 행위가 탐지된 시점의 영상을 서버에 저장하고, 해당 시점의 로그를 DB에 기록함
OpenCV 라이브러리를 활용하여, 탐지 시점으로부터 약 5s ~ 10s 간의 데이터 스트림을 영상으로 변환하여 저장

- 연속적인 탐지 이벤트 처리
투기 행위 탐지 시, 연속적으로 이벤트가 발생하기 때문에 다음과 같은 프로세스를 통해 처리
![image](https://github.com/Hojun1123/4_1Mojadol/assets/65999992/2c8c5670-3ab9-4509-b1e3-72f3b26d47dc)


### 웹 서비스 개발 (Spring)
사용자가 서버에 저장된 영상과 해당 로그를 확인할 수 있는 웹 서비스 개발
해당 시점의 로그 클릭 시, 탐지 시점의 짧은 영상을 확인 가능
- 로그 페이지
![image](https://github.com/Hojun1123/4_1Mojadol/assets/65999992/f2e11eea-4262-41b3-9d69-2bb0be4d3072)

----------------------------------------------------------------------------------------

