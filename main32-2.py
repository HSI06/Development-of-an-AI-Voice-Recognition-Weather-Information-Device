# main32-2.py

# 음성 인식 라이브러리 불러오기
import speech_recognition as sr

# 인터넷 API 요청을 위한 requests 라이브러리 불러오기
import requests

# 운영체제 명령어 실행을 위한 os 라이브러리 불러오기
import os


# OpenWeatherMap API Key 입력
API_KEY = "YOUR_API_KEY"


# 서울의 현재 날씨 정보를 가져오는 함수
def get_weather():

    # 도시 이름 설정
    city = "Seoul"

    # OpenWeatherMap API 요청 주소
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    # API 요청 보내기
    response = requests.get(url)

    # JSON 형식 데이터 저장
    data = response.json()

    # 현재 기온 정보 저장
    temp = data["main"]["temp"]

    # 현재 습도 정보 저장
    humidity = data["main"]["humidity"]

    # 출력할 문장 생성
    result = f"현재 서울의 기온은 {temp}도 이고 습도는 {humidity}퍼센트 입니다."

    # 결과 반환
    return result


# 텍스트를 음성으로 출력하는 함수
def speak(text):

    # 터미널에 출력
    print(text)

    # eSpeak를 이용하여 음성 출력
    os.system(f'espeak -v ko "{text}"')


# 음성을 인식하는 함수
def recognize_voice():

    # 음성 인식 객체 생성
    recognizer = sr.Recognizer()

    # 마이크 입력 받기
    with sr.Microphone() as source:

        print("음성을 입력하세요.")

        # 사용자의 음성 듣기
        audio = recognizer.listen(source)

    try:
        # Google 음성 인식 API를 이용하여 음성을 텍스트로 변환
        text = recognizer.recognize_google(audio, language="ko-KR")

        # 인식된 텍스트 출력
        print("인식된 음성:", text)

        # 인식된 텍스트 반환
        return text

    # 음성 인식 실패 시 예외 처리
    except sr.UnknownValueError:

        print("음성을 인식하지 못했습니다.")

        return ""

    # 음성 인식 서버 연결 실패 시 예외 처리
    except sr.RequestError:

        print("음성 인식 서비스에 연결할 수 없습니다.")

        return ""


# 메인 실행 부분
if __name__ == "__main__":

    # 사용자 음성 인식
    voice_text = recognize_voice()

    # 음성 안에 "날씨"라는 단어가 포함되어 있는지 확인
    if "날씨" in voice_text:

        # 현재 날씨 정보 가져오기
        weather_info = get_weather()

        # 날씨 정보 음성 출력
        speak(weather_info)

    else:
        # "날씨" 단어가 없을 경우 출력
        speak("날씨라는 단어를 인식하지 못했습니다.")
