import streamlit as st
import pandas as pd
import os

# 设置页面配置
st.set_page_config(
    page_title="排考系统",
    page_icon=":computer:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 自定义CSS样式
st.markdown("""
    <style>
    .big-font {
        font-size:24px !important;
        font-weight: bold;
        color: #1E88E5;
        margin-bottom: 20px;
    }
    .info-container {
        background: linear-gradient(135deg,#fce38a,#f38181);
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .metric-container {
        background: linear-gradient(135deg,#fce38a,#f38181);
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 标题
st.markdown('<p class="big-font">考试排考管理系统</p>', unsafe_allow_html=True)

# 文件上传
# with st.container():
#     st.markdown('<div class="info-container">', unsafe_allow_html=True)
#     data = st.file_uploader("📂 上传考试安排文件", type=["xlsx", "xls"])
#     st.markdown('</div>', unsafe_allow_html=True)

@st.cache_data
def load_data(file_name):
    file_path = os.path.join('data', file_name)  # 构建文件路径
    df = pd.read_excel(file_path)  # 读取数据
    return df


df = load_data('1213-1.xlsx')  # 直接读取 data 文件夹中的文件

# 创建选择器
col1, col2 = st.columns([1, 2])
with col1:
    option = st.selectbox('📊 选择查看类别', ['监考教师', '巡考', '考试班级'])

st.markdown('<div class="info-container">', unsafe_allow_html=True)

if option == '监考教师':
    df_unique_monitor = df['监考教师'].drop_duplicates()
    monitor = st.selectbox('👨‍🏫 选择监考教师', df_unique_monitor)
    selected_monitor = df[df['监考教师'] == monitor]
    
    # 显示基本统计信息
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric("监考场次", len(selected_monitor))
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric("考试地点数", len(selected_monitor['考试地点'].unique()))
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric("考试班级数", len(selected_monitor['考试班级'].unique()))
        st.markdown('</div>', unsafe_allow_html=True)
    
    # 显示详细信息
    st.markdown("### 📋 详细安排")
    columns_to_display = ['星期', '节次', '考试时间', '考试地点', '考试班级']
    st.dataframe(selected_monitor[columns_to_display], use_container_width=True)
    
elif option == '巡考':
    df_unique_inspector = df['巡考'].drop_duplicates()
    inspector = st.selectbox('👨‍💼 选择巡考教师', df_unique_inspector)
    selected_inspector = df[df['巡考'] == inspector]
    
    # 显示基本统计信息
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric("巡考场次", len(selected_inspector))
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric("考试地点数", len(selected_inspector['考试地点'].unique()))
        st.markdown('</div>', unsafe_allow_html=True)
        
    # 显示详细信息
    st.markdown("### 📋 详细安排")
    columns_to_display = ['星期', '节次', '考试时间', '考试地点', '考试班级']
    st.dataframe(selected_inspector[columns_to_display], use_container_width=True)
    
elif option == '考试班级':
    df_unique_class = df['考试班级'].drop_duplicates()
    class_name = st.selectbox('🏫 选择考试班级', df_unique_class)
    selected_class = df[df['考试班级'] == class_name]
    
    # 显示基本统计信息
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric("考试科目数", len(selected_class))
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric("考试地点数", len(selected_class['考试地点'].unique()))
        st.markdown('</div>', unsafe_allow_html=True)
        
    # 显示详细信息
    st.markdown("### 📋 考试安排详情")
    
    # 遍历每条考试记录
    for _, row in selected_class.iterrows():
        with st.container():
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg,#17ead9,#6078ea);
                padding: 15px;
                border-radius: 10px;
                margin: 10px 0;
            ">
                <h4>📅 {row['星期']}</h4>
                <p>⏰ 考试时间：{row['考试时间']}</p>
                <p>📍 考试地点：{row['考试地点']}</p>
            </div>
            """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)













