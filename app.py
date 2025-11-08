import gradio as gr
from model_pipeline import generate_lesson_plan, save_to_docx

def lesson_plan_from_image(image):
    caption, plan_text = generate_lesson_plan(image)
    docx_path = save_to_docx("AI-Generated Lesson Plan", plan_text)
    return caption, plan_text, docx_path


demo = gr.Interface(
    fn=lesson_plan_from_image,
    inputs=gr.Image(type="filepath", label="Upload Classroom / STEM Image"),
    outputs=[
        gr.Textbox(label="Scene Description"),
        gr.Textbox(label="Generated Lesson Plan", lines=20),
        gr.File(label="Download Lesson Plan (DOCX)")
    ],
    title="📚 AI Lesson Plan Generator",
    description="Upload a classroom or STEM activity image to auto-generate a full lesson plan (Objectives, Materials, Activities, Assessment)."
)

if __name__ == "__main__":
    demo.launch()
