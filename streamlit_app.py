html(f"""
<script src="https://developers.kakao.com/sdk/js/kakao.min.js"></script>
<script>
  window.onload = function() {{
    if (!Kakao.isInitialized()) {{
      Kakao.init("{kakao_app_key}");
    }}
  }};

  function shareToKakao() {{
    if (!Kakao.isInitialized()) {{
      Kakao.init("{kakao_app_key}");
    }}
    Kakao.Link.sendDefault({{
      objectType: 'text',
      text: '✨ AI가 알려주는 오늘의 운세!',
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
