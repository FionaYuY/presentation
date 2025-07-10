import streamlit as st

def test_font_sizes():
    """測試不同的字體大小設定方法"""
    
    st.title("字體大小測試頁面")
    
    # 方法1：使用 st.title()
    st.markdown("## 方法1：使用 st.title()")
    st.title("這是 st.title() 的效果")
    
    # 方法2：使用 st.header()
    st.markdown("## 方法2：使用 st.header()")
    st.header("這是 st.header() 的效果")
    
    # 方法3：使用 st.markdown() 
    st.markdown("## 方法3：使用 st.markdown()")
    st.markdown("# 這是 # 標題")
    st.markdown("## 這是 ## 標題")
    st.markdown("### 這是 ### 標題")
    
    # 方法4：使用內聯 HTML 樣式
    st.markdown("## 方法4：使用內聯 HTML 樣式")
    st.markdown("""
    <h1 style="font-size: 4rem !important; font-weight: 700 !important; color: #ffffff !important;">
        這是內聯樣式的 H1 標題
    </h1>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <h2 style="font-size: 2.8rem !important; font-weight: 600 !important; color: #e0e0e0 !important;">
        這是內聯樣式的 H2 標題
    </h2>
    """, unsafe_allow_html=True)
    
    # 方法5：使用更強的 CSS 選擇器
    st.markdown("## 方法5：使用更強的 CSS 選擇器")
    st.markdown("""
    <style>
    .big-title {
        font-size: 4rem !important;
        font-weight: 700 !important;
        color: #ffffff !important;
        margin-bottom: 1rem !important;
        line-height: 1.2 !important;
    }
    
    .medium-title {
        font-size: 2.8rem !important;
        font-weight: 600 !important;
        color: #e0e0e0 !important;
        margin-bottom: 1rem !important;
        line-height: 1.3 !important;
    }
    
    /* 更強的選擇器 */
    .stApp .main .block-container div[data-testid="stMarkdownContainer"] h1 {
        font-size: 4rem !important;
        font-weight: 700 !important;
        color: #ffffff !important;
    }
    
    .stApp .main .block-container div[data-testid="stMarkdownContainer"] h2 {
        font-size: 2.8rem !important;
        font-weight: 600 !important;
        color: #e0e0e0 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="big-title">這是使用 CSS 類別的大標題</div>', unsafe_allow_html=True)
    st.markdown('<div class="medium-title">這是使用 CSS 類別的中標題</div>', unsafe_allow_html=True)
    
    # 方法6：使用 HTML 標籤 + CSS 類別
    st.markdown("## 方法6：使用 HTML 標籤 + CSS 類別")
    st.markdown('<h1 class="big-title">HTML H1 + CSS 類別</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="medium-title">HTML H2 + CSS 類別</h2>', unsafe_allow_html=True)
    
    # 測試一般文字大小
    st.markdown("## 一般文字大小測試")
    st.write("這是一般的文字大小")
    st.markdown("這是 markdown 文字大小")
    
    # 顯示當前的字體大小資訊
    st.markdown("## 除錯資訊")
    st.code("""
    預期效果：
    - 大標題 (H1): 4rem (約 64px)
    - 中標題 (H2): 2.8rem (約 44px)
    - 小標題 (H3): 1.5rem (約 24px)
    - 一般文字: 1rem (約 16px)
    """)

if __name__ == "__main__":
    test_font_sizes() 