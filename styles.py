import gradio as gr

theme = gr.themes.Soft(
    primary_hue="emerald",
    secondary_hue="blue",
    neutral_hue="slate",
    radius_size="lg",
    spacing_size="lg",
)

css = """
.gradio-container{
    background:#f5f7fb;
}

h1{
    text-align:center;
}

footer{
    display:none;
}

.message.user{
    border-radius:14px;
}

.message.bot{
    border-radius:14px;
}

#title{
    text-align:center;
    margin-bottom:10px;
}

#subtitle{
    text-align:center;
    color:#555;
    margin-bottom:25px;
}
"""