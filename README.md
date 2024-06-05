# OSS Project : EZ2OSS

## 구현 목표
본 프로젝트는 노트낙하형 리듬게임, 특히 DJMAX RESPECT V와 EZ2ON REBOOT : R 게임을 목표로 제작했습니다. 노트 낙하 / 키 입력 시 처리 / 판정 발생 3단계 과정을 이용해 계속 떨어지는 노트를 정확히 처리하는 것이 목표인 게임입니다. 게임 종료 조건은 노트를 계속 정확히 처리해 콤보가 50을 달성하면 클리어되며 종료됩니다.

## 구현 기능
+ pygame 기반 2d 게임 환경 구현
+ 랜덤하게 내려오는 노트를 4개 키 입력으로 처리 (S, D, L, ;)
+ 노트 타이밍에 맞춰 키 입력 시 정확히 쳤는 지 판정 발생 (KOOL, COOL, GOOD, MISS, FAIL)

## Reference
[1] https://github.com/pygame/pygame "pygame"

[2] https://youtu.be/GhoQwKBRxSg?si=2szb1icWphpQWvVn "파이썬으로 리듬게임을 만들어보자!"

## 실행 예시
https://cdn.discordapp.com/attachments/945690809880154233/1247927532687462471/oss_silhaeng.gif?ex=6661ce95&is=66607d15&hm=5a32a53be65887b5d045d30c9fc529121accd92d8ea03b3dd83fc71bc883f176&

## 코드 설명
### main.py
초기 세팅은 ingame 루프 밖, 게임 실행은 ingame 루프 안에서 이루어진다.

ingame 루프 안에서는 우선 노트가 이전에 나왔던 노트와 겹치지 않도록 랜덤하게 계속 배치된다.
이때 배치되는 노트는 deploy_note 함수를 통해 실제로 배치되고 draw.rect 함수를 통해 실제로 그려진다.

또 유저가 실제로 키 입력을 할 경우, 판정선 위에 이펙트가 뜨며 노트가 있을 때 입력했을 경우 judge_note 함수가 호출되어 판정이 이루어진다.
판정은 KOOL, COOL, GOOD, MISS, FAIL의 5단계가 있다.

judge_note 함수 내부에서는 global 변수 combo의 값도 계속 조정하는데, MISS or FAIL이 발생하면 0으로 되돌려지고 나머지 판정 시에는 1이 증가한다.
이렇게 50콤보를 모으면 게임 클리어 문구와 함께 종료된다.

## TODO list
1. 콤보 숫자 디스플레이
2. 노래를 불러와 재생하기
3. 노트를 랜덤하게 낙하시키는 것이 아닌 txt에 저장된 패턴을 불러와 낙하시키기
4. hp 시스템을 구현해 일정 이상 fail 판정 발생 시 게임 오버
5. 배경에 이미지 삽입 (곡과 어울리는)
6. 시작 시 속도, 판정선 위치 등 (초기 변수에 있음) 유저가 설정할 수 있도록 인풋 받기
