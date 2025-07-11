import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def render():
    """渲染幕後花絮页面"""
    st.title("🎬 幕後花絮：通勤戰士的血淚史")
    st.subheader("當別人在環遊世界，我在環遊大台北...")
    
    st.markdown("---")
    
    # 血淚數據
    st.write("### 😭 血淚數據大公開")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="每日通勤時間",
            value="3小時",
            delta="來回地獄"
        )
    
    with col2:
        st.metric(
            label="每月通勤時間",
            value="60小時",
            delta="😵 快死了"
        )
    
    with col3:
        st.metric(
            label="半年通勤時間",
            value="360小時",
            delta="💀 已死"
        )
    
    with col4:
        st.metric(
            label="等於連續坐車",
            value="15天",
            delta="😱 崩潰"
        )
    
    st.markdown("---")
    
    # 飛行時間對比
    st.write("### ✈️ 我的通勤時間 vs 飛行時間")
    st.write("**殘酷的現實：每天通勤3小時，我可以...**")
    
    # 創建飛行時間對比表
    flight_data = {
        "目的地": ["香港", "馬尼拉", "宿霧", "漢城", "東京", "大阪"],
        "飛行時間": ["1小時40分", "2小時00分", "2小時30分", "2小時20分", "2小時50分", "2小時15分"],
        "剩餘時間": ["1小時20分", "1小時00分", "30分鐘", "40分鐘", "10分鐘", "45分鐘"],
        "可以做什麼": ["喝咖啡放空", "逛免稅店", "小憩一下", "吃個飯", "緊急登機", "悠閒散步"]
    }
    
    df = pd.DataFrame(flight_data)
    
    # 使用 st.dataframe 显示表格
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )
    
    st.markdown("---")
    
    # 心酸對比
    st.write("### 💔 心酸對比時刻")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**🚇 我的現實**")
        reality_items = [
            "每天3小時困在車廂裡",
            "聞著各種「香味」",
            "被人群擠到變形",
            "看著窗外一樣的風景",
            "在心裡默默倒數站數"
        ]
        
        for item in reality_items:
            st.write(f"• {item}")
    
    with col2:
        st.write("**✈️ 朋友們的日常**")
        friends_items = [
            "飛到大阪吃道地拉麵",
            "在馬尼拉海灘曬太陽",
            "香港血拼買到手軟",
            "韓國首爾吃烤肉配燒酒",
            "東京迪士尼樂園尖叫"
        ]
        
        for item in friends_items:
            st.write(f"• {item}")
    
    st.markdown("---")
    
    # 通勤時間可以做的事
    st.write("### 🤔 360小時通勤時間可以...")
    
    tab1, tab2, tab3 = st.tabs(["旅遊篇", "學習篇", "娛樂篇"])
    
    with tab1:
        st.write("**🌍 環遊世界計畫**")
        travel_plans = [
            "🇯🇵 東京來回 63趟（每趟2小時50分）",
            "🇰🇷 首爾來回 77趟（每趟2小時20分）",
            "🇭🇰 香港來回 108趟（每趟1小時40分）",
            "🇵🇭 馬尼拉來回 90趟（每趟2小時）",
            "🏝️ 宿霧來回 72趟（每趟2小時30分）"
        ]
        
        for plan in travel_plans:
            st.write(f"• {plan}")
    
    with tab2:
        st.write("**📚 學習成長計畫**")
        learning_plans = [
            "📖 讀完 120本書（每本3小時）",
            "🎓 完成 12個線上課程（每個30小時）",
            "🗣️ 學會 3種語言（每種120小時）",
            "💻 精通 18個程式語言（每個20小時）",
            "🎨 成為設計大師（360小時練習）"
        ]
        
        for plan in learning_plans:
            st.write(f"• {plan}")
    
    with tab3:
        st.write("**🎮 娛樂放鬆計畫**")
        entertainment_plans = [
            "🎬 看完 180部電影（每部2小時）",
            "🎮 破關 36款遊戲（每款10小時）",
            "☕ 喝掉 1080杯咖啡（每杯20分鐘）",
            "😴 睡覺 15個整天（每天24小時）",
            "🧘 冥想 720次（每次30分鐘）"
        ]
        
        for plan in entertainment_plans:
            st.write(f"• {plan}")
    
    st.markdown("---")
    
    # 通勤時間圖表 - 更加戲劇性
    st.write("### 📊 血淚累積圖表")
    
    # 創建更戲劇性的圖表
    months = ['1月', '2月', '3月', '4月', '5月', '6月']
    cumulative_hours = [60, 120, 180, 240, 300, 360]
    
    # 對應的可以飛行的次數（以大阪為例，2小時15分）
    osaka_trips = [h // 2.25 for h in cumulative_hours]
    
    fig = go.Figure()
    
    # 添加通勤時間線
    fig.add_trace(go.Scatter(
        x=months,
        y=cumulative_hours,
        mode='lines+markers',
        name='累積通勤時間',
        line=dict(color='#ff5722', width=4),
        marker=dict(size=12, color='#d32f2f', line=dict(color='#ff5722', width=2))
    ))
    
    # 添加可飛大阪次數（右軸）
    fig.add_trace(go.Scatter(
        x=months,
        y=[t * 16 for t in osaka_trips],  # 放大以便在同一圖表顯示
        mode='lines+markers',
        name='可飛大阪次數 (x16)',
        line=dict(color='#2196f3', width=3, dash='dash'),
        marker=dict(size=10, color='#1976d2'),
        yaxis='y2'
    ))
    
    fig.update_layout(
        title="2025上半年通勤血淚史",
        xaxis_title="月份",
        yaxis_title="累積通勤時間（小時）",
        yaxis2=dict(
            title="可飛大阪次數（趟）",
            overlaying='y',
            side='right'
        ),
        template="plotly_dark",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#f5f5f5")
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # 心靈雞湯時刻
    st.write("### 💪 通勤戰士的正能量")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("🧠 **意外收穫**")
        st.write("• 在捷運上想出了最佳的系統架構")
        st.write("• 通勤時間成為思考的黃金時段")
        st.write("• 練就了在任何環境都能專注的能力")
    
    with col2:
        st.success("🎯 **未來目標**")
        st.write("• 遠端工作，把通勤時間拿來旅遊")
        st.write("• 用節省的時間真正飛到這些地方")
        st.write("• 把通勤經驗寫成勵志書籍")
    
    st.markdown("---")
    
    st.error("😤 **總結**: 雖然通勤很辛苦，但我用這些時間完成了 14 個項目，證明時間管理就是一切！") 