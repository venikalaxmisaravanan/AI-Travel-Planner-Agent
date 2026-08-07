import gradio as gr

from agent import chat


demo = gr.ChatInterface(
    fn=chat,
    title="🌍 TravelMate AI",
    description="✈️Your AI Travel Planner for India✈️"
)

if __name__ == "__main__":
    demo.launch(
        inbrowser=True
    )