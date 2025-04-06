# MIT 18.06 Linear Algebra, Spring 2005

이 저장소는 MIT의 유명한 선형대수학 강의 "18.06 Linear Algebra, Spring 2005"의 스크립트와 한국어 번역, 그리고 SRT 자막 파일을 제공합니다.

## 프로젝트 개요

Gilbert Strang 교수의 선형대수학 강의는 전 세계적으로 가장 인기 있는 수학 강의 중 하나입니다. 이 프로젝트는 다음과 같은 목표를 가지고 있습니다:

1. YouTube에서 제공하는 원본 영어 스크립트 보존
2. GPT와 Claude를 활용한 한국어 번역본 제작
3. 번역된 내용을 기반으로 SRT 자막 파일 생성

영어 스크립트에서 섹션 구분이 있는 부분은 마크다운 형식의 `#` 헤더로 처리하여 가독성을 높였습니다.

## 저장소 구조

```
.
├── README.md
├── README.en.md          # 영어 버전 README
├── scripts
│   ├── original          # 원본 영어 스크립트
│   │   ├── lec01.txt
│   │   ├── lec02.txt
│   │   └── ...
│   └── translated        # 한국어 번역 스크립트
│       ├── lec01.txt
│       ├── lec02.txt
│       └── ...
├── srt
│   ├── en                # 영어 SRT 자막 파일
│   │   ├── lec01.srt
│   │   ├── lec02.srt
│   │   └── ...
│   └── ko                # 한국어 SRT 자막 파일
│       ├── lec01.srt
│       ├── lec02.srt
│       └── ...
└── tools                 # 변환 및 처리 도구
    ├── txt_to_srt.py     # 텍스트 스크립트를 SRT 파일로 변환
    └── ...
```

## 번역 과정

1. YouTube 스크립트를 수집하여 `scripts/original/` 폴더에 저장
2. 각 강의 스크립트의 섹션을 `#` 마크다운 헤더로 표시
3. GPT와 Claude를 활용하여 한국어로 번역
4. `tools/txt_to_srt.py`를 사용하여 SRT 자막 파일 생성
5. 번역된 내용 검토 및 수정

## 기여 방법

이 프로젝트에 기여하고 싶으시다면 다음과 같은 방법으로 참여하실 수 있습니다:

1. 번역 오류 수정
2. 번역 품질 개선
3. SRT 변환 도구 개선
4. 누락된 강의 스크립트 추가

## 라이센스 정보

원본 강의는 MIT OpenCourseWare에서 제공하며, [Creative Commons License](https://ocw.mit.edu/terms/) 하에 공개되어 있습니다.

## 감사의 말

- Gilbert Strang 교수님과 MIT OpenCourseWare 팀에게 훌륭한 강의를 공개해주신 것에 감사드립니다.
- 번역 및 검토에 도움을 주신 모든 분들께 감사드립니다.

---

**참고**: 이 프로젝트는 개인 학습 및 교육 목적으로 만들어졌으며, 상업적인 목적으로 사용되지 않습니다.
