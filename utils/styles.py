import streamlit as st

def apply_custom_css():
    """應用自定義CSS樣式"""
    # 引入Google Fonts
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <style>
    /* 主題色彩 - 科技感現代風格 */
    :root {
        --primary-color: #64ffda;
        --secondary-color: #2a2a2a;
        --accent-color: #e0e0e0;
        --background-color: #1a1a1a;
        --text-color: #ffffff;
        --card-background: #2a2a2a;
        --border-color: #3a3a3a;
        --success-color: #4ade80;
        --warning-color: #ffb400;
        --error-color: #ff6b6b;
        --hover-color: #00bcd4;
    }
    
    /* 全局樣式 */
    .stApp {
        background: var(--background-color);
        color: var(--text-color);
        scroll-behavior: smooth;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        font-size: 1rem;
    }
    
    /* 基本文字樣式 - 保持層次結構 */
    .stApp p {
        color: var(--text-color) !important;
        font-size: 18px !important;
        line-height: 1.6 !important;
    }
    
    .stApp li {
        color: var(--text-color) !important;
        font-size: 17px !important;
        line-height: 1.6 !important;
    }
    
    .stApp span {
        color: var(--text-color) !important;
        font-size: 17px !important;
        line-height: 1.6 !important;
    }
    
    /* 移除過度廣泛的選擇器，保持特定組件的顏色 */
    
    /* 標題樣式 - 更強的選擇器優先級 */
    .main .block-container .stApp h1,
    .stApp .main .block-container h1,
    div[data-testid="block-container"] h1,
    .stApp h1 {
        color: var(--text-color) !important;
        font-size: 4rem !important;
        font-weight: 700 !important;
        margin-bottom: 1rem !important;
        line-height: 1.2 !important;
    }
    
    .main .block-container .stApp h2,
    .stApp .main .block-container h2,
    div[data-testid="block-container"] h2,
    .stApp h2 {
        color: var(--text-color) !important;
        font-size: 2.8rem !important;
        font-weight: 600 !important;
        margin-bottom: 0.8rem !important;
        line-height: 1.3 !important;
    }
    
    .stApp h3 {
        color: var(--text-color) !important;
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        margin-bottom: 0.6rem !important;
    }
    
    .stApp h4 {
        color: var(--text-color) !important;
        font-size: 1.3rem !important;
        font-weight: 600 !important;
        margin-bottom: 0.5rem !important;
    }
    
    .stApp h5 {
        color: var(--text-color) !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        margin-bottom: 0.4rem !important;
    }
    
    .stApp h6 {
        color: var(--text-color) !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        margin-bottom: 0.3rem !important;
    }
    
    /* 移除滾動吸附效果，使用平滑滾動 */
    html, body {
        scroll-behavior: smooth;
        scrollbar-width: thin;
        scrollbar-color: var(--primary-color) transparent;
    }
    
    .main .block-container {
        scroll-behavior: smooth;
        scrollbar-width: thin;
        scrollbar-color: var(--primary-color) transparent;
    }
    
    /* 自定義滾動條 */
    html::-webkit-scrollbar, body::-webkit-scrollbar, .main .block-container::-webkit-scrollbar {
        width: 8px;
    }
    
    html::-webkit-scrollbar-track, body::-webkit-scrollbar-track, .main .block-container::-webkit-scrollbar-track {
        background: transparent;
    }
    
    html::-webkit-scrollbar-thumb, body::-webkit-scrollbar-thumb, .main .block-container::-webkit-scrollbar-thumb {
        background: var(--primary-color);
        border-radius: 4px;
    }
    
    html::-webkit-scrollbar-thumb:hover, body::-webkit-scrollbar-thumb:hover, .main .block-container::-webkit-scrollbar-thumb:hover {
        background: var(--hover-color);
    }
    
    /* 頁面區塊樣式 - 移除滾動吸附 */
    .page-section {
        min-height: 100vh;
        padding: 2rem;
        background: linear-gradient(135deg, rgba(42, 42, 42, 0.8) 0%, rgba(26, 26, 26, 0.9) 100%);
        border-radius: 16px;
        border: 1px solid var(--border-color);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        margin-bottom: 2rem;
        position: relative;
    }
    
    .page-section:nth-child(even) {
        background: linear-gradient(135deg, rgba(26, 26, 26, 0.9) 0%, rgba(42, 42, 42, 0.8) 100%);
    }
    
    /* 主標題樣式 */
    .main-title {
        font-size: 4.5rem;
        font-weight: 700;
        text-align: center;
        color: var(--text-color);
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--hover-color) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1.5rem;
        letter-spacing: -0.02em;
        font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    
    /* 副標題樣式 */
    .sub-title {
        font-size: 1.8rem;
        text-align: center;
        color: var(--accent-color);
        margin-bottom: 3rem;
        font-weight: 400;
        opacity: 0.9;
        letter-spacing: 0.01em;
    }
    
    /* 卡片樣式 */
    .achievement-card {
        background: var(--card-background);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 4px 24px rgba(0, 0, 0, 0.3);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .achievement-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, var(--primary-color), var(--hover-color));
        transform: scaleX(0);
        transition: transform 0.3s ease;
    }
    
    .achievement-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 48px rgba(100, 255, 218, 0.1);
        border-color: var(--primary-color);
    }
    
    .achievement-card:hover::before {
        transform: scaleX(1);
    }
    
    /* 按鈕樣式 */
    .stButton > button {
        background: linear-gradient(135deg, var(--card-background) 0%, var(--secondary-color) 100%);
        color: var(--text-color);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 500;
        font-size: 16px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--hover-color) 100%);
        border-color: var(--primary-color);
        transform: translateY(-2px);
        box-shadow: 0 8px 32px rgba(100, 255, 218, 0.2);
        color: var(--background-color);
    }
    
    /* 進度條樣式 */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, var(--primary-color), var(--hover-color));
    }
    
    /* 選擇框樣式 */
    .stSelectbox > div > div {
        background-color: var(--card-background);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div:hover {
        border-color: var(--primary-color);
        box-shadow: 0 0 0 2px rgba(100, 255, 218, 0.1);
    }
    
    /* 導航錨點樣式 */
    .nav-anchor {
        display: block;
        position: relative;
        top: -80px;
        visibility: hidden;
    }
    
    /* 成功訊息樣式 */
    .stSuccess {
        background: linear-gradient(135deg, var(--card-background) 0%, rgba(74, 222, 128, 0.1) 100%);
        border: 1px solid var(--success-color);
        border-radius: 8px;
        color: var(--success-color);
        box-shadow: 0 2px 8px rgba(74, 222, 128, 0.1);
    }
    
    /* Metric組件樣式 */
    .stMetric {
        background: var(--card-background);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 24px rgba(0, 0, 0, 0.3);
    }
    
    .stMetric label {
        color: var(--text-color) !important;
        font-size: 18px !important;
        font-weight: 600 !important;
    }
    
    .stMetric [data-testid="metric-value"] {
        color: var(--primary-color) !important;
        font-size: 2.2rem !important;
        font-weight: 700 !important;
    }
    
    .stMetric [data-testid="metric-delta"] {
        color: var(--success-color) !important;
        font-size: 1.1rem !important;
        font-weight: 500 !important;
    }
    
    /* Info組件樣式 */
    .stInfo {
        background: var(--card-background) !important;
        border: 1px solid var(--primary-color) !important;
        border-radius: 8px !important;
        padding: 1rem !important;
        margin: 1rem 0 !important;
        box-shadow: 0 2px 8px rgba(100, 255, 218, 0.1) !important;
    }
    
    .stInfo p {
        color: var(--text-color) !important;
        font-size: 17px !important;
        margin: 0 !important;
    }
    
    /* 警告組件樣式 */
    .stWarning {
        background: var(--card-background) !important;
        border: 1px solid var(--warning-color) !important;
        border-radius: 8px !important;
        padding: 1rem !important;
        margin: 1rem 0 !important;
        box-shadow: 0 2px 8px rgba(255, 180, 0, 0.1) !important;
    }
    
    .stWarning p {
        color: var(--warning-color) !important;
        font-size: 17px !important;
        margin: 0 !important;
    }
    
    /* 錯誤組件樣式 */
    .stError {
        background: var(--card-background) !important;
        border: 1px solid var(--error-color) !important;
        border-radius: 8px !important;
        padding: 1rem !important;
        margin: 1rem 0 !important;
        box-shadow: 0 2px 8px rgba(255, 107, 107, 0.1) !important;
    }
    
    .stError p {
        color: var(--error-color) !important;
        font-size: 17px !important;
        margin: 0 !important;
    }
    
    /* Markdown文字樣式 */
    .stMarkdown {
        color: var(--text-color) !important;
    }
    
    .stMarkdown p {
        color: var(--text-color) !important;
        font-size: 18px !important;
        line-height: 1.6 !important;
    }
    
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
        color: var(--text-color) !important;
    }
    
    /* 表格樣式 */
    .stDataFrame {
        background: var(--card-background) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 8px !important;
    }
    
    .stDataFrame th {
        background: var(--secondary-color) !important;
        color: var(--text-color) !important;
        font-weight: 600 !important;
    }
    
    .stDataFrame td {
        color: var(--text-color) !important;
        font-size: 16px !important;
    }
    
    /* 側邊欄樣式 */
    .stSidebar {
        background: var(--card-background) !important;
        border-right: 1px solid var(--border-color) !important;
    }
    
    .stSidebar .stMarkdown h1, .stSidebar .stMarkdown h2, .stSidebar .stMarkdown h3 {
        color: var(--text-color) !important;
    }
    
    .stSidebar .stMarkdown p {
        color: var(--text-color) !important;
        font-size: 15px !important;
    }
    
    /* 文字輸入框樣式 */
    .stTextInput > div > div > input {
        background: var(--card-background) !important;
        border: 1px solid var(--border-color) !important;
        color: var(--text-color) !important;
        border-radius: 6px !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: var(--primary-color) !important;
        box-shadow: 0 0 0 2px rgba(100, 255, 218, 0.2) !important;
    }
    
    /* 標籤樣式 */
    .stTextInput > label {
        color: var(--text-color) !important;
        font-weight: 500 !important;
    }
    
    /* 改善分隔線樣式 */
    hr {
        border-color: var(--border-color) !important;
        margin: 2rem 0 !important;
    }
    
    /* Markdown容器的段落文字 */
    .stApp [data-testid="stMarkdownContainer"] p {
        font-size: 1.1rem !important;
        color: var(--text-color) !important;
    }
    

    
    /* 確保所有按鈕的文字大小 */
    .stButton button {
        font-size: 1rem !important;
        color: var(--text-color) !important;
    }
    
    /* 移除重複的Metric規則，已在上面定義 */
    
    /* 確保表格元素的文字顏色和大小 */
    .stApp td, .stApp th {
        color: var(--text-color) !important;
        font-size: 0.95rem !important;
    }
    
    /* 確保label元素的文字顏色 */
    .stApp label {
        color: var(--text-color) !important;
        font-size: 1rem !important;
    }
    
    /* 確保成功訊息的文字顏色 */
    .stSuccess > div {
        color: var(--success-color) !important;
        font-size: 1.1rem !important;
    }
    
    /* 確保資訊訊息的文字顏色 */
    .stInfo > div {
        color: var(--primary-color) !important;
        font-size: 1.1rem !important;
    }
    
    /* 確保警告訊息的文字顏色 */
    .stWarning > div {
        color: var(--warning-color) !important;
        font-size: 1.1rem !important;
    }
    
    /* 確保錯誤訊息的文字顏色 */
    .stError > div {
        color: var(--error-color) !important;
        font-size: 1.1rem !important;
    }
    
    /* 資訊訊息樣式 */
    .stInfo {
        background: linear-gradient(135deg, var(--card-background) 0%, rgba(100, 255, 218, 0.1) 100%);
        border: 1px solid var(--primary-color);
        border-radius: 8px;
        color: var(--primary-color);
        box-shadow: 0 2px 8px rgba(100, 255, 218, 0.1);
    }
    
    /* 警告訊息樣式 */
    .stWarning {
        background: linear-gradient(135deg, var(--card-background) 0%, rgba(255, 180, 0, 0.1) 100%);
        border: 1px solid var(--warning-color);
        border-radius: 8px;
        color: var(--warning-color);
        box-shadow: 0 2px 8px rgba(255, 180, 0, 0.1);
    }
    
    /* 隱藏Streamlit預設元素 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 側邊欄樣式 */
    .css-1d391kg, [data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--secondary-color) 0%, var(--background-color) 100%);
        border-right: 1px solid var(--border-color);
    }
    
    /* 側邊欄標題樣式 */
    [data-testid="stSidebar"] h1 {
        color: var(--primary-color);
        font-weight: 600;
        text-shadow: 0 0 10px rgba(100, 255, 218, 0.3);
    }
    
    /* 側邊欄文字樣式 */
    [data-testid="stSidebar"] .stMarkdown {
        color: var(--accent-color);
    }
    
    /* Metric 元件樣式 */
    [data-testid="metric-container"] {
        background: var(--card-background);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 1rem;
        transition: all 0.3s ease;
    }
    
    [data-testid="metric-container"]:hover {
        border-color: var(--primary-color);
        box-shadow: 0 4px 16px rgba(100, 255, 218, 0.1);
    }
    
    /* 標題漸層效果 - 簡化版 */
    .stApp h1, .stApp h2, .stApp h3 {
        color: var(--primary-color);
    }
    
    /* 列表項目動畫 */
    .stMarkdown li {
        transition: all 0.3s ease;
        padding: 0.3rem 0;
    }
    
    .stMarkdown li:hover {
        transform: translateX(5px);
        color: var(--primary-color);
    }
    
    /* 頁面淡入動畫 */
    .main .block-container {
        animation: fadeIn 0.6s ease-in-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* 滾動條樣式 */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--background-color);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, var(--primary-color), var(--hover-color));
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, var(--hover-color), var(--primary-color));
    }
    
    /* 發光效果 */
    .glow-text {
        text-shadow: 0 0 20px rgba(100, 255, 218, 0.5);
    }
    
    /* 呼吸動畫 */
    @keyframes breathe {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    
    .breathe {
        animation: breathe 3s ease-in-out infinite;
    }
    
    /* 浮動導航按鈕 */
    .floating-nav {
        position: fixed;
        right: 2rem;
        top: 50%;
        transform: translateY(-50%);
        z-index: 1000;
        background: var(--card-background);
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        border: 1px solid var(--border-color);
    }
    
    .floating-nav button {
        background: transparent !important;
        border: none !important;
        color: var(--text-light) !important;
        padding: 0.5rem !important;
        margin: 0.2rem 0 !important;
        border-radius: 6px !important;
        transition: all 0.2s ease !important;
    }
    
    .floating-nav button:hover {
        background: var(--accent-teal) !important;
        color: white !important;
    }
    
    /* 動畫效果 */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in {
        animation: fadeIn 0.8s ease-out;
    }
    
    /* 閃光效果 */
    @keyframes shine {
        0% { background-position: -100px; }
        100% { background-position: 100px; }
    }
    
    .shine {
        background: linear-gradient(90deg, transparent, rgba(44, 122, 123, 0.4), transparent);
        background-size: 200px 100%;
        animation: shine 2s infinite;
    }
    
    /* 平滑滾動 */
    html {
        scroll-behavior: smooth;
    }
    
    /* 電影片尾名單滾動效果 */
    .credits-container {
        height: 60vh;
        overflow: hidden;
        position: relative;
        background: linear-gradient(135deg, rgba(26, 26, 26, 0.9) 0%, rgba(42, 42, 42, 0.8) 100%);
        border-radius: 12px;
        border: 1px solid var(--border-color);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        margin: 2rem 0;
    }
    
    .credits-scroll {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        animation: creditsScroll 60s linear infinite;
        padding: 2rem;
        text-align: center;
    }
    
    @keyframes creditsScroll {
        0% {
            transform: translateY(100%);
        }
        100% {
            transform: translateY(-100%);
        }
    }
    
    .credits-item {
        margin: 2rem 0;
        padding: 1.5rem;
        background: rgba(100, 255, 218, 0.1);
        border-radius: 8px;
        border: 1px solid rgba(100, 255, 218, 0.2);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .credits-item:hover {
        background: rgba(100, 255, 218, 0.2);
        transform: scale(1.02);
        box-shadow: 0 4px 16px rgba(100, 255, 218, 0.1);
    }
    
    .credits-title {
        color: var(--primary-color);
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .credits-status {
        color: var(--success-color);
        font-size: 0.9rem;
        font-weight: 500;
    }
    
    /* 控制按鈕 */
    .credits-controls {
        position: absolute;
        bottom: 1rem;
        right: 1rem;
        z-index: 100;
    }
    
    .credits-controls button {
        background: rgba(100, 255, 218, 0.2);
        border: 1px solid var(--primary-color);
        color: var(--primary-color);
        border-radius: 6px;
        padding: 0.5rem 1rem;
        margin: 0 0.25rem;
        cursor: pointer;
        transition: all 0.3s ease;
        font-size: 0.8rem;
    }
    
    .credits-controls button:hover {
        background: var(--primary-color);
        color: var(--background-color);
    }
    
    .paused {
        animation-play-state: paused !important;
    }
    
    /* 區段標題樣式 */
    .section-title {
        font-size: 2.5rem;
        font-weight: 600;
        color: var(--primary-teal);
        margin: 3rem 0 2rem 0;
        text-align: center;
        position: relative;
    }
    
    .section-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 80px;
        height: 3px;
        background: linear-gradient(90deg, var(--primary-teal), var(--accent-teal));
        border-radius: 2px;
    }
    
    /* 最高優先級標題覆蓋 - 確保生效 */
    h1[data-testid] {
        font-size: 4rem !important;
        font-weight: 700 !important;
        color: var(--text-color) !important;
    }
    
    h2[data-testid] {
        font-size: 2.8rem !important;
        font-weight: 600 !important;
        color: var(--text-color) !important;
    }
    
    .stMarkdown h1,
    .element-container h1 {
        font-size: 4rem !important;
        font-weight: 700 !important;
        color: var(--text-color) !important;
    }
    
    .stMarkdown h2,
    .element-container h2 {
        font-size: 2.8rem !important;
        font-weight: 600 !important;
        color: var(--text-color) !important;
    }
    
    /* 强制覆盖所有可能的h1和h2 */
    * h1 {
        font-size: 4rem !important;
        font-weight: 700 !important;
        color: var(--text-color) !important;
    }
    
    * h2 {
        font-size: 2.8rem !important;
        font-weight: 600 !important;
        color: var(--text-color) !important;
    }
    </style>
    """, unsafe_allow_html=True)

def render_page_header(title, subtitle=""):
    """渲染頁面標題"""
    st.markdown(f"""
    <div class="main-title fade-in">{title}</div>
    <div class="sub-title fade-in">{subtitle}</div>
    """, unsafe_allow_html=True)

def render_achievement_card(title, content, icon="🏆"):
    """渲染成就卡片"""
    st.markdown(f"""
    <div class="achievement-card fade-in">
        <h3>{icon} {title}</h3>
        <p>{content}</p>
    </div>
    """, unsafe_allow_html=True)

def render_section_divider():
    """渲染區段分隔線"""
    st.markdown("""
    <div style="
        height: 3px;
        background: linear-gradient(90deg, transparent, var(--primary-teal), transparent);
        margin: 2rem 0;
        border-radius: 2px;
    "></div>
    """, unsafe_allow_html=True)

def render_page_section(section_id, content_func):
    """渲染帶錨點的頁面區塊 - 簡化版"""
    # 使用 Streamlit 原生容器，避免 HTML 干擾
    with st.container():
        # 添加錨點
        st.markdown(f'<div id="{section_id}"></div>', unsafe_allow_html=True)
        
        # 添加頁面頂部裝飾線
        st.markdown("""
        <div style="
            height: 3px;
            background: linear-gradient(90deg, #64ffda 0%, #00bcd4 100%);
            opacity: 0.8;
            margin: 2rem 0;
            border-radius: 2px;
        "></div>
        """, unsafe_allow_html=True)
        
        # 渲染實際內容
        content_func()
        
        # 添加頁面底部分隔線
        st.markdown("""
        <div style="
            height: 1px;
            background: linear-gradient(90deg, transparent 0%, #3a3a3a 50%, transparent 100%);
            margin: 3rem 0;
        "></div>
        """, unsafe_allow_html=True)

def render_floating_navigation():
    """渲染浮動導航提示"""
    st.markdown("""
    <div style="
        position: fixed;
        right: 2rem;
        top: 50%;
        transform: translateY(-50%);
        z-index: 1000;
        background: var(--card-background);
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        border: 1px solid var(--border-color);
        font-size: 0.8rem;
        color: var(--text-light);
        max-width: 120px;
        text-align: center;
    ">
        <div style="margin-bottom: 0.5rem; font-weight: bold; color: var(--primary-teal);">
            🧭 導航提示
        </div>
        <div style="font-size: 0.7rem; opacity: 0.8;">
            向下滾動瀏覽<br/>
            或使用側邊欄<br/>
            快速跳轉
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_highlight_text(text, color="var(--primary-teal)"):
    """渲染高亮文字"""
    st.markdown(f"""
    <span style="color: {color}; font-weight: bold; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">
        {text}
    </span>
    """, unsafe_allow_html=True)

def render_floating_particles():
    """渲染漂浮粒子效果（進階功能）"""
    # 這裡可以添加JavaScript來創建粒子效果
    # 暫時留空，可以後續添加
    pass 

 