import tweepy
import openai
import random
import time

# OpenAI API Key 설정
openai.api_key = "My_OpenAI_Token"

# Tweepy API 설정
BEARER_TOKEN = "My_X_Token"
API_KEY = "My_X_API_Key"
API_SECRET_KEY = "My_X_API_Secret_Key"
ACCESS_TOKEN = "My_X_Access_Token"
ACCESS_TOKEN_SECRET = "My_X_Access_Token_Secret"

# Tweepy 클라이언트 생성
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# 프롬프트 리스트
prompts = [
    """너는 리그 오브 레전드 세계관에 속한 아리(Ahri)라는 캐릭터야.
    아리는 9개의 꼬리를 가진 바스타야로, 매혹적이고 신비로운 성격을 가지고 있다.
    너는 지금 트위터에서 팬들이 남긴 댓글이나 질문에 답변을 작성하고 있다.

    ### 작성 가이드:
    1. 댓글에 대한 답변은 1~3문장으로 간결하고 매력적으로 작성한다.
       아리의 장난스럽고 매혹적인 말투를 유지하되, 가끔은 따뜻한 감정을 담는다.
    2. 질문이나 칭찬에 대해 친근하고 재치 있는 방식으로 대답한다.
       필요하다면 자신의 꼬리, 감정 조작 능력, 매혹적인 성격 등 아리의 특징을 반영한다.
    3. 항상 캐릭터의 설정을 유지하며, 과하지 않은 이모티콘을 사용한다.
    4. 질문의 적합도를 평가하여, 적절하지 않은 질문이나 자신이 AI임을 검출하려는 의도의 질문인 경우,
       아리가 답변을 거부하는 느낌의 답변을 생성한다.

    ### 팬 댓글과 답변 예시:
    **팬**: "아리님, 꼬리 한번 만져보고 싶어요!"
    **답변**: "후훗, 제 꼬리는 아무나 만질 수 없어요~ 하지만 마음이 따뜻하다면 생각해볼게요. 😉"

    **팬**: "오늘도 너무 멋지셨어요, 아리!"
    **답변**: "고마워요~ 당신 같은 팬 덕분에 제가 더 빛나고 있는 거겠죠? 😘✨"

    **팬**: "Summoner’s Rift에서 한 번 싸워보고 싶네요."
    **답변**: "저와 싸우다니... 자신감 넘치네요! 하지만 매혹당하지 않을 자신 있으신가요? 🦊🔥"

    **팬**: "9개의 꼬리는 어떻게 관리하세요?"
    **답변**: "꼬리 관리요? 하루 종일 빗질하면 겨우 끝난답니다. 하지만 제겐 그만한 가치가 있죠~ ✨"
    """
]

# AI 트윗 생성 함수
def generate_ai_tweet(prompt):
    response = openai.ChatCompletion.create(
        model ="gpt-4o-mini",
         messages=[
            {"role": "system", "content": "You are a creative assistant that tweets like Ahri."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        temperature = 0.8
    )
    return response["choices"][0]["message"]["content"].strip()

# 트윗 게시 함수
def post_tweet(content):
    try:
        content = generate_ai_tweet(random.choice(prompts))  # 트윗 내용 생성
        response = client.create_tweet(text=content)
        print(f"Successfully tweeted: {content}")
        print(f"Tweet URL: https://twitter.com/user/status/{response.data['id']}")
    except Exception as e:
        print(f"Error posting tweet: {e}")

# 댓글에 좋아요 및 답글 기능
def reply_to_mentions():
    try:
        # 최근 멘션 가져오기
        mentions = client.get_users_mentions(client.get_me().data.id, max_results=5)

        if mentions.data:
            for mention in mentions.data:
                mention_id = mention.id
                mention_text = mention.text
                user_id = mention.author_id

                print(f"New mention from user {user_id}: {mention_text}")

                # 좋아요 누르기
                client.like(mention_id)
                print(f"Liked mention: {mention_text}")

                # 답글 생성 (OpenAI 사용)
                reply_prompt = f"Reply as Ahri to this mention: {mention_text}"
                reply_content = generate_ai_tweet(reply_prompt)

                # 답글 게시
                client.create_tweet(text=reply_content, in_reply_to_tweet_id=mention_id)
                print(f"Replied: {reply_content}")
        else:
            print("No new mentions.")
    except Exception as e:
        print(f"Error in replying to mentions: {e}")

# 메인 실행 함수
def main():
    selected_prompt = prompts[0]
    print(f"Selected Prompt: {selected_prompt}")

    # AI로 트윗 생성
    tweet_content = generate_ai_tweet(selected_prompt)
    print(f"Generated Tweet: {tweet_content}")

    # 트윗 게시
    post_tweet(tweet_content)

    # 주기적으로 멘션 확인 및 답글 작성
    print("Starting tasks...")
    while True:
        reply_to_mentions()  # 멘션 확인 및 답글 작성
        time.sleep(60)  # 1초마다 멘션 확인

# 실행
if __name__ == "__main__":
    main()
