# 인공지능 음성을 인식하여 날씨 정보 알려주는 장치 만들기
## Development of an AI Voice Recognition Weather Information Device

한신대학교 AI·SW학전공 AIoT 설계입문 프로젝트

---

## 프로젝트 소개

본 프로젝트는 라즈베리파이와 음성 인식 기술을 활용하여 사용자의 음성을 인식하고 현재 날씨 정보를 음성으로 안내하는 시스템이다.  

사용자가 “날씨”라고 말하면 SpeechRecognition 라이브러리를 통해 음성을 텍스트로 변환하고, OpenWeatherMap API를 이용하여 서울의 현재 기온과 습도 정보를 받아온다. 이후 eSpeak를 사용하여 현재 날씨 정보를 음성으로 출력한다.

---

## 개발 환경

- Raspberry Pi
- Raspberry Pi OS
- Python 3.x

---

## 사용 기술

- SpeechRecognition
- OpenWeatherMap API
- eSpeak (Text To Speech)
- requests 라이브러리

---

## 주요 기능

- 사용자 음성 입력 인식
- “날씨” 키워드 인식
- 서울의 현재 기온 및 습도 정보 수집
- 현재 날씨 정보 음성 출력

---

## 시스템 동작 과정

1. 사용자가 마이크를 통해 “날씨”라고 말함
2. SpeechRecognition이 음성을 텍스트로 변환
3. OpenWeatherMap API를 통해 현재 날씨 데이터 요청
4. 현재 기온 및 습도 정보 수신
5. eSpeak를 통해 음성으로 결과 출력

---

## 실행 방법

```bash
python main32-2.py
