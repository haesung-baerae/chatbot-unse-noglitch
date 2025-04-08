from streamlit.components.v1 import html

kakao_app_key = "e81bbaa2211fcf6024940d3cac85cc5b"
share_text = "🌟 오늘의 운세를 확인해보세요!\nhttps://chatbot-unse-noglitch.streamlit.app/"

html(f"""
<!-- Kakao SDK 로드 -->
<script src="https://developers.kakao.com/sdk/js/kakao.min.js"></script>
<script>
  Kakao.init("{kakao_app_key}");

  function sendKakao() {{
    Kakao.Link.sendDefault({{
      objectType: 'text',
      text: `{share_text}`,
      link: {{
        mobileWebUrl: 'https://chatbot-unse-noglitch.streamlit.app/',
        webUrl: 'https://chatbot-unse-noglitch.streamlit.app/'
      }},
      buttonTitle: '운세 보러가기'
    }});
  }}
</script>

<!-- 버튼 UI -->
<div style="text-align:center; margin-top: 20px;">
  <button onclick="sendKakao()" style="
      padding: 10px 20px;
      font-size: 16px;
      background-color: #FEE500;
      color: #3C1E1E;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      font-weight: bold;">
    💬 카카오톡으로 운세 공유하기
  </button>
</div>
""", height=100)
