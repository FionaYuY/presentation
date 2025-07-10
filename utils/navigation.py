import streamlit as st

def init_navigation():
    """初始化導航狀態"""
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 1
    if 'total_pages' not in st.session_state:
        st.session_state.total_pages = 8

def render_navigation():
    """渲染導航控制"""
    col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])
    
    with col1:
        if st.button("⏮️ 第一頁"):
            st.session_state.current_page = 1
            st.rerun()
    
    with col2:
        if st.button("⬅️ 上一頁"):
            if st.session_state.current_page > 1:
                st.session_state.current_page -= 1
                st.rerun()
    
    with col3:
        # 頁面指示器
        st.markdown(f"<div style='text-align: center; font-size: 18px; font-weight: bold;'>"
                   f"第 {st.session_state.current_page} 頁 / 共 {st.session_state.total_pages} 頁"
                   f"</div>", unsafe_allow_html=True)
    
    with col4:
        if st.button("➡️ 下一頁"):
            if st.session_state.current_page < st.session_state.total_pages:
                st.session_state.current_page += 1
                st.rerun()
    
    with col5:
        if st.button("⏭️ 最後頁"):
            st.session_state.current_page = st.session_state.total_pages
            st.rerun()

def render_page_selector():
    """渲染頁面選擇器"""
    page_options = {
        1: "🎬 首頁",
        2: "🏆 作品總覽",
        3: "🥇 技術創新",
        4: "🎓 學術研究",
        5: "💼 商業應用",
        6: "🎭 遺珠作品",
        7: "😢 通勤人生",
        8: "🎉 結語"
    }
    
    selected_page = st.selectbox(
        "快速導航",
        options=list(page_options.keys()),
        format_func=lambda x: page_options[x],
        index=st.session_state.current_page - 1
    )
    
    if selected_page != st.session_state.current_page:
        st.session_state.current_page = selected_page
        st.rerun()

def render_progress_bar():
    """渲染進度條"""
    progress = st.session_state.current_page / st.session_state.total_pages
    st.progress(progress)
    
def get_current_page():
    """獲取當前頁面"""
    return st.session_state.current_page

def get_page_title():
    """獲取當前頁面標題"""
    page_titles = {
        1: "首頁",
        2: "作品總覽",
        3: "技術創新",
        4: "學術研究",
        5: "商業應用",
        6: "遺珠作品",
        7: "通勤人生",
        8: "結語"
    }
    return page_titles.get(st.session_state.current_page, "未知頁面") 