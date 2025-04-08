import streamlit as st
from streamlit.components.v1 import html

st.title("🔗 카카오톡 공유 테스트")
st.write("아래 버튼을 누르면 카카오톡으로 공유가 시도됩니다.")

# 카카오 JavaScript 키 (반드시 해당 앱의 JS 키!)
kakao_js_key = "af66d0f1f7ad2f0028df6e6c72057eb6"  # 예: "e81bbaa2211fcf6024940d3cac85cc5b"

# 공유할 링크
share_url = "https://chatbot-unse-noglitch.streamlit.app"

# 공유 버튼 구성
html(f"""
<!-- Kakao SDK 불러오기 -->
<script src="https://developers.kakao.com/sdk/js/kakao.min.js"></script>
<script>
  // SDK 로드 후 초기화
  window.onload = function() {{
    if (!Kakao.isInitialized()) {{
      Kakao.init('{kakao_js_key}');
    }}
  }}

  function shareToKakao() {{
    if (!Kakao.isInitialized()) {{
      Kakao.init('{kakao_js_key}');
    }}
    Kakao.Link.sendDefault({{
      objectType: 'feed',
      content: {{
        title: '🔮 AI가 전해주는 오늘의 운세',
        description: '✨ 당신만의 오늘의 운세를 확인해보세요!',
        imageUrl: 'https://i.imgur.com/6OGP7l1.png',
        link: {{
          mobileWebUrl: '{share_url}',
          webUrl: '{share_url}'
        }}
      }},
      buttons: [
        {{
          title: '운세 보러가기',
          link: {{
            mobileWebUrl: '{share_url}',
            webUrl: '{share_url}'
          }}
        }}
      ]
    }});
  }}
</script>

<!-- 공유 버튼 UI -->
<div style="text-align:center; margin-top: 30px;">
  <button onclick="shareToKakao()" style="
    padding: 12px 20px;
    font-size: 16px;
    background-color: #FEE500;
    color: #3C1E1E;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-weight: bold;">
    💬 카카오톡으로 공유하기
  </button>
</div>
""", height=200)
