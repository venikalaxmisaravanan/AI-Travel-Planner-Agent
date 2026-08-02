import gradio as gr

from agent import chat


demo = gr.ChatInterface(
    fn=chat,
    title="🇮🇳 AI Travel Planner",
    description="Plan your next trip across India with an AI travel assistant."
)


if __name__ == "__main__":
    demo.launch(inbrowser=True)