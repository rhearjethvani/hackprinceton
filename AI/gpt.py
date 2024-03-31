from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_KEY"))


questions=2
job_description = """
About the job
We are

At Synechron, we believe in the power of digital to transform businesses for the better. Our global consulting firm combines creativity and innovative technology to deliver industry-leading digital solutions. Synechron's progressive technologies and optimization strategies span end-to-end Artificial Intelligence, Consulting, Digital, Cloud & DevOps, Data, and Software Engineering, servicing an array of noteworthy financial services and technology firms. Through research and development initiatives in our FinLabs we develop solutions for modernization, from Artificial Intelligence and Blockchain to Data Science models, Digital Underwriting, mobile-first applications and more. Over the last 20+ years, our company has been honored with multiple employer awards, recognizing our commitment to our talented teams. With top clients to boast about, Synechron has a global workforce of 14,700+, and has 48 offices in 19 countries within key global markets.
Our challenge

We are looking for a skilled react.js developer to join our front-end development team. In this role, you will be responsible for developing and implementing user interface components using React.js concepts and workflows such as Redux, Flux, and Webpack.
The Role

Responsibilities:

Meeting with the development team to discuss user interface ideas and applications.
Reviewing application requirements and interface designs.
Identifying web-based user interactions.
Developing and implementing highly responsive user interface components using react concepts.
Writing application interface codes using JavaScript following react.js workflows.
Troubleshooting interface software and debugging application codes.
Developing and implementing front-end architecture to support user interface concepts.
Monitoring and improving front-end performance.
Requirements: 

You are: 

Strong experience with JavaScript, ReactJS
Experience with OAuth2, Azure Application Registration
Familiar with Figma (for designs)
In-depth knowledge of JavaScript, CSS, HTML, and front-end languages.
Knowledge of REACT tools including React.js, Webpack, Enzyme, Redux, and Flux.
Experience with user interface design.
It would be great if you also had:

Banking/ Financial experience.

"""
def generate_job_questions(questions,number):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Given the job description, generate {questions} relevant behavioral questions. Make sure you provide exactly {questions} questions.Ensure that the questions are directly related to the job role described and return the response as a list (array) of questions. Example Output: ['Qn1','Qn2',...] Job Description: {job_description}",
            },
        ],
    )
    qns = completion.choices[0].message.content
    return qns


def generate_education_questions(content):
    # Prompt for generating questions for verbal answers
    completion_verbal = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f"Based on the content provided below, generate 1 question that should be answered verbally by the students. The question should assess their understanding of the material. Content: {content}",
            },
        ],
    )
    qns_verbal = completion_verbal.choices[0].message.content
    return qns_verbal

# print(generate_job_questions(questions, 2))
# print(
#     generate_education_questions(
#         """Princeton University, located in Princeton, New Jersey, is one of the oldest and most prestigious universities in the United States. Founded in 1746 as the College of New Jersey, it was later renamed Princeton University in 1896. Princeton is renowned for its commitment to excellence in teaching and research across a wide range of disciplines.

# The university's picturesque campus spans over 500 acres and features a unique blend of historic and modern architecture. Notable landmarks include Nassau Hall, the university's oldest building, which served as the capital of the United States for a brief period during the Revolutionary War.

# Princeton University is consistently ranked among the top universities in the world. Its academic programs are renowned for their rigor and innovation, attracting talented students and faculty from around the globe. The university offers undergraduate and graduate programs in the arts and humanities, social sciences, natural sciences, engineering, and more.

# Beyond academics, Princeton offers a vibrant campus life with numerous student organizations, cultural events, and athletic teams. The university is a member of the Ivy League, known for its competitive athletics and rich tradition.

# With a commitment to service and leadership, Princeton University prepares students to make a positive impact on the world. Its alumni include Nobel laureates, Rhodes Scholars, Supreme Court justices, and leaders in various fields, making Princeton a beacon of intellectual excellence and innovation.

# """,
#         10,
#     )
# )
