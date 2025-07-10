# 全域設定檔案

# 應用程式設定
APP_CONFIG = {
    "title": "Fiona 2025上半年工作成果展示",
    "page_title": "工作成果展示",
    "page_icon": "🎬",
    "layout": "wide",
    "initial_sidebar_state": "collapsed"
}

# 頁面設定
PAGE_CONFIG = {
    "total_pages": 8,
    "default_page": 1,
    "page_names": {
        1: "首頁",
        2: "作品總覽",
        3: "技術創新",
        4: "學術研究",
        5: "商業應用",
        6: "遺珠作品",
        7: "通勤人生",
        8: "結語"
    }
}

# 主題設定 - 科技感現代風格
THEME_CONFIG = {
    "primary_color": "#64ffda",  # 科技薄荷藍（強調色）
    "secondary_color": "#2a2a2a",  # 深灰（卡片背景）
    "accent_color": "#b3b3b3",  # 中性灰（次要文字）
    "background_color": "#1a1a1a",  # 深灰背景
    "text_color": "#f5f5f5",  # 柔白文字
    "card_background": "#2a2a2a",  # 深灰卡片背景
    "border_color": "#3a3a3a",  # 邊框色
    "success_color": "#4ade80",  # 科技綠
    "warning_color": "#ffb400",  # 金色高亮
    "error_color": "#ff6b6b"  # 科技紅
}

# 動畫設定
ANIMATION_CONFIG = {
    "fade_duration": "0.8s",
    "hover_scale": "1.05",
    "transition_duration": "0.3s",
    "slide_distance": "20px"
}

# 字體設定
FONT_CONFIG = {
    "title_size": "3rem",
    "subtitle_size": "1.5rem",
    "heading_size": "2rem",
    "body_size": "1rem",
    "small_size": "0.875rem"
}

# 間距設定
SPACING_CONFIG = {
    "section_margin": "2rem",
    "card_padding": "1rem",
    "button_padding": "0.5rem 1rem",
    "border_radius": "10px"
}

# 媒體設定
MEDIA_CONFIG = {
    "max_image_width": "800px",
    "max_video_width": "100%",
    "thumbnail_size": "150px"
}

# 導航設定
NAVIGATION_CONFIG = {
    "show_progress_bar": True,
    "show_page_numbers": True,
    "show_quick_navigation": True,
    "show_sidebar_navigation": False
}

# 開發設定
DEV_CONFIG = {
    "debug_mode": False,
    "show_dev_info": False,
    "enable_caching": True
}

# 內容設定
CONTENT_CONFIG = {
    "author_name": "Fiona",
    "author_email": "[您的Email]",
    "author_linkedin": "[您的LinkedIn]",
    "author_github": "[您的GitHub]",
    "company_name": "[公司名稱]",
    "period": "2025上半年"
}

# 統計設定
STATS_CONFIG = {
    "total_projects": 11,
    "completion_rate": 100,
    "commute_hours_daily": 3,
    "commute_hours_monthly": 60,
    "commute_hours_half_year": 360
}

# 外部連結
LINKS_CONFIG = {
    "arxiv_paper": "[arXiv連結]",
    "ai_journal": "[AI Journal連結]",
    "github_repo": "[GitHub連結]",
    "company_website": "[公司官網]"
}

# 隱藏元素設定
HIDE_CONFIG = {
    "streamlit_menu": True,
    "streamlit_footer": True,
    "streamlit_header": True,
    "deploy_button": True
}

# 頁面內容設定
CONTENT_PLACEHOLDERS = {
    "linkverse_content": "[需要提供LinkVerse的詳細內容]",
    "icon_rotation_story": "[需要提供icon旋轉的有趣故事]",
    "fried_food_theory": "[需要提供炸物理論的內容]",
    "deot_authors": "[需要提供DEoT論文的完整作者名單]",
    "contact_email": "[您的Email地址]",
    "contact_linkedin": "[您的LinkedIn]",
    "contact_github": "[您的GitHub]",
    "personal_website": "[您的個人網站]"
} 