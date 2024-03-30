from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_KEY"))



completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content":"Given the job description, generate {questions} relevant behavioral questions. Make sure you provide exactly {questions} questions.Ensure that the questions are directly related to the job role described and return the response as a list (array) of questions. Example Output: ['Qn1','Qn2',...] Job Description: {job_description}",
        },
    ],
)


qns=completion.choices[0].message.content
for item in qns.split("\n")[1:]:
    print(item)
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
