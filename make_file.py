import os

def create_wikidocs_structure():
    # 지정된 베이스 경로
    base_dir = r"C:\MyData\05. GitHub\art_of_english"
    pages_dir = os.path.join(base_dir, "pages")

    # 디렉토리 생성 (존재하지 않으면 생성)
    os.makedirs(pages_dir, exist_ok=True)

    # 생성할 pages 내의 마크다운 파일 목록
    markdown_files = [
        "00_prologue.md",
        "part1_why_grammar_blueprint.md",
        "01_native_language_trap.md",
        "02_assembly_not_discovery.md",
        "03_preventing_fossilization.md",
        "part2_grammar_as_a_tool.md",
        "04_pareto_principle.md",
        "05_tense_and_voice.md",
        "06_verbals_and_clauses.md",
        "part3_input_reading_listening.md",
        "07_chunk_reading.md",
        "08_grammar_for_listening.md",
        "09_context_inference.md",
        "part4_output_writing_speaking.md",
        "10_three_step_translation.md",
        "11_pattern_practice.md",
        "12_toefl_speaking_writing.md",
        "part5_12_week_roadmap.md",
        "13_phase1_foundation.md",
        "14_phase2_framing.md",
        "15_phase3_finishing.md",      
        "epilogue.md"
    ]

    # pages 하위에 빈 .md 파일 생성
    print(f"[*] '{pages_dir}' 경로에 빈 마크다운 파일 생성을 시작합니다...")
    for filename in markdown_files:
        file_path = os.path.join(pages_dir, filename)
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as f:
                pass  # 빈 파일 생성
            print(f"  - 생성 완료: pages/{filename}")
        else:
            print(f"  - 이미 존재함: pages/{filename}")

    # 루트 경로에 TOC.md 파일 내용 작성
    toc_path = os.path.join(base_dir, "TOC.md")
    toc_content = """# 목차

- [-서문](pages/00_prologue.md)

- [1부. 왜 성인에게는 '문법 설계도'가 필요한가](pages/part1_why_grammar_blueprint.md)
  * [1장. 모국어 방식의 함정 - 5세 아이와 50세 성인의 뇌는 다르다](pages/01_native_language_trap.md)
  * [2장. 한국인에게 영어는 '발견'이 아니라 '조립'이다 - 어순 차이를 극복하는 논리](pages/02_assembly_not_discovery.md)
  * [3장. 화석화(Fossilization)를 막는 유일한 길 - 브로큰 잉글리시에서 벗어나는](pages/03_preventing_fossilization.md)

- [2부. 문법, 암기 대상이 아닌 '도구'로 재정의하기](pages/part2_grammar_as_a_tool.md)
  * [4장. 파레토 법칙 - 영어의 80%를 지배하는 핵심 문법 20가지](pages/04_pareto_principle.md)
  * [5장. 동사의 시제와 태 - 문장의 '시간'과 '입장'을 결정하는 엔진](pages/05_tense_and_voice.md)
  * [6장. 준동사와 절 - 단순한 문장을 고급스럽게 확장하는 연결 고리](pages/06_verbals_and_clauses.md)

- [3부. [Input] 설계도로 읽고 듣는 법 (Reading & Listening)](pages/part3_input_reading_listening.md)
  * [7장. 구문 독해의 마법 - 토플 긴 지문이 한눈에 들어오는 '청크(Chunk)' 읽기](pages/07_chunk_reading.md)
  * [8장. 문법이 들려야 귀가 트인다 - 리스닝의 병목 현상을 해결하는 문법 지식](pages/08_grammar_for_listening.md)
  * [9장. 문맥 추론의 기술 - 모르는 단어가 나와도 구조로 뚫고 나가는 법](pages/09_context_inference.md)

- [4부. [Output] 설계도로 쓰고 말하는 법 (Writing & Speaking)](pages/part4_output_writing_speaking.md)
  * [10장. 영작은 문법의 실전판이다 - 한국어 사고를 영어 구조로 치환하는 3단계 프](pages/10_three_step_translation.md)
  * [11장. 입 근육에 문법을 새기는 법 - 패턴 프랙티스를 통한 자동화 훈련](pages/11_pattern_practice.md)
  * [12장. 토플 스피킹, 라이팅 전략 - 감점 없는 정확한 문장으로 고득점 달성하기](pages/12_toefl_speaking_writing.md)

- [5부. 실전! 문법 기반 12주 완성 로드맵](pages/part5_12_week_roadmap.md)
  * [13장. (1~4주) 기초 공사 - 핵심 문법 개념 잡기와 기초 영작](pages/13_phase1_foundation.md)
  * [14장. (5~8주) 골조 올리기 - 토플 지문 분석과 쉐도잉 훈련](pages/14_phase2_framing.md)
  * [15장. (9~12주) 인테리어 완성 - 자유로운 비즈니스 회화와 에세이 작성](pages/15_phase3_finishing.md)

- [PBS News Hour](pages/pbs_news_hour.md)

- [맺음말](pages/epilogue.md)
"""

    with open(toc_path, 'w', encoding='utf-8') as f:
        f.write(toc_content)
    print(f"[*] 루트 경로에 'TOC.md' 파일이 성공적으로 생성되었습니다: {toc_path}")

if __name__ == "__main__":
    create_wikidocs_structure()