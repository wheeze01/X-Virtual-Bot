# Ahri AI Twitter Bot (X-Virtual-Bot)

Ahri AI Twitter Bot은 트위터에서 Ahri(아리)라는 캐릭터의 말투로 자동으로 트윗을 생성하고, 멘션을 감지하여 응답하는 챗봇입니다.

## 📌 주요 기능
- **자동 트윗 생성**: Ahri의 매력적이고 장난스러운 말투로 트윗을 자동 생성하여 게시합니다.
- **멘션 감지 및 응답**: 팬들의 멘션을 감지하고, Ahri의 성격을 반영한 답변을 생성하여 자동으로 응답합니다.
- **좋아요 기능**: Ahri를 언급한 트윗에 자동으로 좋아요를 누릅니다.
- **GPT 기반 텍스트 생성**: OpenAI의 GPT 모델을 사용하여 Ahri의 톤과 스타일에 맞춘 트윗과 답변을 생성합니다.

## 🛠 기술 스택
- **Python**
- **Tweepy**: 트위터 API와 상호작용
- **OpenAI API**: GPT 모델을 활용한 텍스트 생성
- **Random & Time 모듈**: 주기적인 실행을 위한 랜덤 시간 조절 및 지연 기능

## 🚀 실행 방법
### 1. 필수 라이브러리 설치
```bash
pip install tweepy openai
```

### 2. 환경 변수 설정
`.env` 파일을 생성하고, 다음과 같은 정보를 추가합니다:
```env
OPENAI_API_KEY=your_openai_api_key
BEARER_TOKEN=your_twitter_bearer_token
API_KEY=your_twitter_api_key
API_SECRET_KEY=your_twitter_api_secret_key
ACCESS_TOKEN=your_twitter_access_token
ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
```

### 3. 스크립트 실행
```bash
python bot.py
```

## 🔄 주요 기능 설명
- `generate_ai_tweet(prompt)`: OpenAI API를 사용해 Ahri 스타일의 트윗을 생성
- `post_tweet(content)`: 트윗을 자동으로 게시
- `reply_to_mentions()`: 멘션을 감지하고 Ahri 스타일로 응답
- `main()`: 모든 기능을 순환 실행하며 지속적으로 트윗과 멘션 응답 수행

## 📄 라이선스
MIT License

## 📧 문의

프로젝트와 관련된 질문이나 제안 사항이 있으시면 아래의 이메일로 연락해주세요.

- 이메일: fcsolution11@kangwon.ac.kr
