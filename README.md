#AI文本生成器

##项目背景
很多人在写作时面临“开头难”或创意枯竭的问题，我开发了这个工具，让用户输入开头文字，AI就能智能续写，支持中英文。

##核心功能
-输入提示词自动生成多版本续写 
-可调节生成长度和温度（创造性）
-Streamlit网页界面，一键使用
-基于Hugging Face开源模型

##我的贡献
-独立完成产品从0到1：需求分析 → prompt设计 → 模型集成 → 前端界面
-设计了用户交互流程，优化prompt模型以减少幻觉和重复内容
-迭代了两次版本
-解决了本地部署问题，让非技术用户也能快速运用

##技术栈
Python + Hugging Face + Streamlit

#如何运行
1. 克隆仓库  
   `git clone https://github.com/Eliot954/ai-text-generator-demo.git`
2. 进入文件夹  
   `cd ai-text-genetator-demo`
3. 创建并激活虚拟环境  
   `python -m venv venv` 
   `venv\Scripts\activate`
4. 安装依赖  
   `pip install -r requirements.txt`
5. 启动  
   `streamlit run text_generator_app.py`
6. 界面预览
   ![AI 文本生成演示](demo(2).png)
打开浏览器访问 http://localhost:8501 即可使用！

## 用户流程图
<img width="1964" height="1273" alt="b3ebf21c514c119f1c3455efed7bf210" src="https://github.com/user-attachments/assets/fdd9008e-4592-4673-a0d2-874b334a782f" />
[![用户流程图](user_flow.png)](user_flow.png)

# ai-text-genetator-demo
AI文本生成小工具，使用Hugging Face和Streamlit
