import streamlit as st
st.title('나의 첫번째 웹앱(by남중근)')
st.write('이게 된다고?!')
import streamlit as st

# MBTI별 추천 직업 데이터
mbti_jobs = {
    "INTJ": ["전략 컨설턴트", "데이터 과학자", "정책 분석가"],
    "INTP": ["연구원", "소프트웨어 엔지니어", "이론 물리학자"],
    "ENTJ": ["CEO", "프로젝트 매니저", "변호사"],
    "ENTP": ["기업가", "마케팅 디렉터", "발명가"],
    "INFJ": ["상담사", "작가", "사회운동가"],
    "INFP": ["예술가", "심리학자", "인권 활동가"],
    "ENFJ": ["교사", "HR 매니저", "공공연설가"],
    "ENFP": ["기획자", "홍보 전문가", "스타트업 창업가"],
    "ISTJ": ["회계사", "군인", "행정 공무원"],
    "ISFJ": ["간호사", "초등 교사", "사서"],
    "ESTJ": ["경영 관리자", "감독관", "보험 심사관"],
    "ESFJ": ["고객 서비스 매니저", "이벤트 플래너", "간호 관리자"],
    "ISTP": ["기계공", "파일럿", "응급구조사"],
    "ISFP": ["패션 디자이너", "사진작가", "물리치료사"],
    "ESTP": ["영업 담당자", "구조대원", "스턴트 배우"],
    "ESFP": ["배우", "MC", "여행 가이드"]
}

# 앱 제목
st.title("MBTI 기반 직업 추천기")

# 설명
st.write("당신의 MBTI 유형을 선택하면, 해당 유형에 적합한 직업 3가지를 추천해드립니다.")

# MBTI 선택 위젯
mbti_list = list(mbti_jobs.keys())
selected_mbti = st.selectbox("당신의 MBTI는 무엇인가요?", mbti_list)

# 결과 출력
if selected_mbti:
    st.subheader(f"🧠 {selected_mbti} 유형에게 어울리는 직업:")
    for i, job in enumerate(mbti_jobs[selected_mbti], start=1):
        st.write(f"{i}. {job}")
