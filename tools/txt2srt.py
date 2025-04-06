#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys
import os
import argparse

def format_srt_time(seconds):
    """초를 SRT 시간 형식(HH:MM:SS,mmm)으로 변환"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    msecs = int((seconds - int(seconds)) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{msecs:03d}"

def detect_language(text):
    """텍스트에서 한글 비율을 기반으로 언어 자동 감지"""
    hangul_chars = re.findall(r'[\uAC00-\uD7A3]', text)
    total_chars = len(re.sub(r'\s+', '', text))
    if total_chars == 0:
        return 'en'
    ratio = len(hangul_chars) / total_chars
    return 'ko' if ratio > 0.2 else 'en'

def estimate_duration(text, lang='ko', wpm=150, cps=10.0):
    """언어 기반 텍스트 길이로 발화 시간 추정"""
    if lang == 'ko':
        chars = len(re.sub(r'\s+', '', text))
        return max(chars / cps, 1.5)
    else:
        words = len(text.split())
        return max(words * 60 / wpm, 1.5)

def script2srt(input_file, output_file=None, lang=None, wpm=150, cps=10.0, time_factor=2.0, max_time=10.0):
    """스크립트 파일을 SRT 자막으로 변환"""
    if output_file is None:
        base_name = os.path.splitext(input_file)[0]
        output_file = f"{base_name}.srt"

    # 파일 읽기
    content = None
    encodings = ['utf-8', 'cp1252', 'latin-1']
    for encoding in encodings:
        try:
            with open(input_file, 'r', encoding=encoding) as f:
                content = f.read()
            break
        except (UnicodeDecodeError, IOError):
            continue
    if content is None:
        raise Exception(f"파일을 읽을 수 없습니다: {input_file}")

    # 언어 자동 감지
    if lang is None:
        lang = detect_language(content)
        print(f"언어 자동 감지 결과: {lang.upper()}")

    # 세그먼트 분리
    segments = []
    current_time = None
    current_text = ""

    lines = content.split('\n')
    skip_first_line = True
    for line in lines:
        line = line.strip()
        if skip_first_line:
            skip_first_line = False
            continue

        if not line or line.startswith('#'):
            continue

        timestamp_match = re.match(r'^(\d+):(\d+)', line)
        if timestamp_match:
            minutes = int(timestamp_match.group(1))
            seconds = int(timestamp_match.group(2))
            timestamp = minutes * 60 + seconds

            if current_time is not None and current_text:
                segments.append((current_time, current_text))

            current_time = timestamp
            remaining_text = line[timestamp_match.end():].strip()
            current_text = remaining_text or ""

        elif current_time is not None:
            current_text += (" " if current_text else "") + line

    if current_time is not None and current_text:
        segments.append((current_time, current_text))

    if not segments:
        raise Exception("타임스탬프를 찾을 수 없습니다.")

    # SRT 생성
    srt_content = ""
    for i in range(len(segments)):
        start_time = segments[i][0]
        text = segments[i][1]

        if i < len(segments) - 1:
            next_start = segments[i+1][0]
            speech_seconds = estimate_duration(text, lang, wpm, cps)
            time_gap = next_start - start_time

            if speech_seconds * time_factor < time_gap:
                end_time = min(start_time + speech_seconds, next_start, start_time + max_time)
            else:
                end_time = next_start
        else:
            speech_seconds = estimate_duration(text, lang, wpm, cps)
            end_time = min(start_time + speech_seconds, start_time + max_time)

        srt_content += f"{i+1}\n"
        srt_content += f"{format_srt_time(start_time)} --> {format_srt_time(end_time)}\n"
        srt_content += f"{text}\n\n"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(srt_content)
    return len(segments)

def main():
    parser = argparse.ArgumentParser(description="스크립트 파일을 SRT 자막으로 변환합니다.")
    parser.add_argument("input", help="입력 텍스트 파일 (타임스탬프 포함)")
    parser.add_argument("output", nargs="?", help="출력 SRT 파일명 (지정하지 않으면 입력파일명 기반)")
    parser.add_argument("--lang", choices=['ko', 'en'], help="언어 설정 (ko 또는 en). 생략하면 자동 감지")
    parser.add_argument("--wpm", type=float, default=150, help="영어 기준 분당 단어 수 (기본값: 150)")
    parser.add_argument("--cps", type=float, default=10.0, help="한국어 기준 초당 글자 수 (기본값: 10.0)")
    parser.add_argument("--factor", type=float, default=2.0, help="발화시간과 다음 자막 사이 비교 계수 (기본값: 2.0)")
    parser.add_argument("--max-time", type=float, default=10.0, help="자막 한 줄 최대 지속 시간 (기본값: 10.0초)")

    args = parser.parse_args()

    try:
        count = script2srt(
            input_file=args.input,
            output_file=args.output,
            lang=args.lang,
            wpm=args.wpm,
            cps=args.cps,
            time_factor=args.factor,
            max_time=args.max_time
        )
        output_path = args.output if args.output else os.path.splitext(args.input)[0] + ".srt"
        print(f"변환 완료: {output_path} ({count}개 자막)")
    except Exception as e:
        print(f"오류 발생: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
