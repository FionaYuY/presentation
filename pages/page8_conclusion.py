import streamlit as st

def render():
    """渲染結語頁面"""
    st.title("謝謝觀賞")
    st.subheader("感謝您的時間和關注")
    
    st.markdown("---")
    
    # 感謝詞
    st.write("### 感謝詞")
    st.write("""
    感謝各位抽空觀看我的2025上半年工作成果展示。這半年來，從學術研究到商業應用，
    從技術創新到團隊協作，每一個項目都是我成長路上的重要里程碑。
    """)
    
    st.markdown("---")
    
    # 重點回顧
    st.write("### 重點回顧")
    key_highlights = [
        "DEoT論文：學術研究與商業應用的完美結合",
        "NeuroWatt News：技術創新的集大成者",
        "P1 Select：商業價值的最佳體現",
        "遺珠作品：創意與技術的有趣碰撞",
        "通勤時光：時間管理的另一種思考"
    ]
    
    for highlight in key_highlights:
        st.write(f"• {highlight}")
    
    st.markdown("---")
    
    # 展望下半年
    st.write("### 展望下半年")
    st.write("""
    下半年我將繼續專注於：
    """)
    
    future_focus = [
        "深化學術研究，推動更多創新技術",
        "提升產品體驗，創造更大商業價值",
        "加強團隊協作，共同成長",
        "平衡工作與生活，維持長期發展動力"
    ]
    
    for focus in future_focus:
        st.write(f"• {focus}")
    
    st.markdown("---")
    
    # 結尾
    st.success("再次感謝您的觀看！期待在下半年創造更多精彩成果！")
    
