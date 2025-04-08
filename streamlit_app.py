from streamlit.components.v1 import html

html(f"""
<script src="https://developers.kakao.com/sdk/js/kakao.min.js"></script>
<script>
  Kakao.init("af66d0f1f7ad2f0028df6e6c72057eb6");  // 반드시 새 앱의 JS 키!

  function shareToKakao() {{
    Kakao.Link.sendDefault({{
      objectType: 'text',
      text: '✨ 새로운 주소에서 직접 공유 테스트 중!',
      link: {{
        mobileWebUrl: 'https://chatbot-unse-noglitch.streamlit.app',
        webUrl: 'https://chatbot-unse-noglitch.streamlit.app'
      }},
      buttonTitle: '운세 보러가기'
    }});
  }}
</script>

<div style="text-align:center; margin-top: 20px;">
  <button onclick="shareToKakao()" style="
    padding: 10px 20px;
    font-size: 16px;
    background-color: #FEE500;
    color: #3C1E1E;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-weight: bold;">
    💬 카카오톡 공유 테스트
  </button>
</div>
""", height=120)
