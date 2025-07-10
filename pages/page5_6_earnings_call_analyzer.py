import streamlit as st
import os
import base64

def show_pdf(file_path):
    """显示PDF文件的函数"""
    try:
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        
        # 使用 iframe 预览，增加高度
        pdf_display_iframe = f'''
        <iframe src="data:application/pdf;base64,{base64_pdf}" 
                width="100%" 
                height="800px" 
                type="application/pdf"
                style="border: 2px solid #4CAF50; border-radius: 8px;">
        </iframe>
        '''
        st.markdown(pdf_display_iframe, unsafe_allow_html=True)
        
        return True
    except Exception as e:
        st.error(f"PDF 显示失败: {str(e)}")
        return False

def render():
    """渲染法說會簡報分析系統页面"""
    st.title("📊 法說會簡報分析系統")
    st.subheader("深度分析法說會簡報的智能系統")
    
    st.markdown("---")
    
    # 系统功能简介
    st.write("### 🎯 系統功能")
    st.write("法說會簡報分析系統能夠自動分析企業法說會簡報內容，提取關鍵財務數據和市場洞察。")
    
    features = [
        "📈 **財務數據提取**: 自動識別並提取損益表、資產負債表關鍵數字",
        "🔍 **製程分析**: 深度分析不同製程技術的營收占比和趨勢",
        "📊 **視覺化報告**: 自動生成圖表和結構化分析報告",
        "🎯 **市場策略解析**: 提取企業未來展望和戰略重點"
    ]
    
    for feature in features:
        st.write(feature)
    
    st.markdown("---")
    
    # PDF 预览功能
    st.write("### 📑 PDF 簡報預覽")
    st.write("系統支援 PDF 簡報預覽功能，方便對照原始資料進行分析。")
    
    # 检查 PDF 文件是否存在
    pdf_path = "assets/files/earnings_call.pdf"
    
    if os.path.exists(pdf_path):
        st.write("**📄 原始法說會簡報**:")
        
        # 直接显示 PDF 预览
        if show_pdf(pdf_path):
            st.success("✅ PDF 預覽載入成功！")
        else:
            st.error("⚠️ PDF 預覽載入失敗")
            
    else:
        st.error(f"PDF 文件不存在: {pdf_path}")
        st.info("請確認文件路徑正確")
    
    st.markdown("---")
    
    # 技术特色
    st.write("### 💡 技術特色")
    
    tech_features = [
        "🧠 **OCR 文字識別**: 準確提取 PDF 中的文字和數字",
        "📊 **表格解析**: 自動識別和分析財務報表結構",
        "🎯 **關鍵詞提取**: 智能識別重要財務指標和業務重點",
        "📈 **趨勢分析**: 比較歷史數據，識別變化趨勢"
    ]
    
    for feature in tech_features:
        st.write(feature)
    
    st.markdown("---")
    
    # 未来发展
    st.write("### 🔮 未來發展方向")
    st.write("**重點改進**: 提升數字提取的準確性")
    
    future_improvements = [
        "🎯 **更精準的數字提取**: 尋找更好的 Model 或技術確保數字準確性",
        "📊 **表格結構識別**: 改進財務報表的自動化解析能力",
        "🔍 **多語言支援**: 支援中英文混合的法說會簡報",
        "⚡ **即時分析**: 加快分析速度，支援即時產出報告"
    ]
    
    for improvement in future_improvements:
        st.write(improvement)
    
    st.success("🎯 **法說會簡報分析系統**: 讓財務分析更智能，讓投資決策更精準！") 